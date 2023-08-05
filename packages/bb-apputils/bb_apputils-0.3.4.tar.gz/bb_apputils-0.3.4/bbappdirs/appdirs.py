import sys, os, json, tempfile, atexit, logging
from glob import glob
from datetime import datetime as dt
from os.path import ( dirname as DN,
                      expanduser,
                      isdir,
                      isfile,
                      join as JN )

log = None

class AppDirs:
    """
    Get system specific app directories
        - for initiating app configurations

        A temporary file is created and read for reading by other
      modules within the app.

      Module Data > 'expire' : expiration time in seconds
                    'name'   : application name
                    'logfile': logfile path
                    'logs'   : list of stored logs from SimpleLog
                    'time'   : initial AppDirs call time
                    'tmp'    : temporary file path
                    'shared' : shared dictionary data


        self.data['logs'] = [{ 'levelname': str(),
                               'level'    : int()
                               'time'     : datetime.timestamp(),
                               'msg'      : str(),
                               'formatted': str()  },
                                etc...  ]

    """
    data = {}

    def __init__( self, *,
                  name,
                  expire = 0,
                  unique = "",
                  simplelog = False,
                  loglevel = 0,
                  noerrors = False,
                  shared = {},
                  initial = False,
                  simplyfile = False ):
        """
        All keyword arguments:

          name = provide application name
              - required
          expire = set an expiration time in seconds
              - temporary file is abandoned/deleted if older than this time
              - expire <= 0 = no expiration
              - default = 0
          unique = provide a name or unique set of characters
              - prevent other programs or modules from unintentionally reading
                or deleting the wrong temp files
              - required with every call that wants to access this data
          simplelog = use SimpleLog instead of python's built-in logging module
              - default False
          loglevel = log level for SimpleLog
              - ignored for python's logging module
          noerrors = don't print logs at exit due to errors
          shared = data to share throughout the application
              - must be in dictionary format
          initial = Specify the initial call to force cleanup of temp files
              - default = False
          simplyfile = Prints all log messages to a logfile at exit
              - default False
              - only used if simplelog is used
              - keeps only 10 logs and deletes older ones
              - existing logs are appended and new logs are created 24 hours apart
              - the logfile is created in the users app directory:
                        '~/%(APPDIR)/BBAppDirs-%(date).log'

            SimpleLog is used for initial call. Subsequent calls, if the temp file
          is created, will load python's built-in logging module unless 'simplelog'
          is set to True.

        """
        global log
        tmp = None
        cb = self._fromSimpleLog
        log = SimpleLog( loglevel, log_to_data = cb )
        starttime = int( dt.now().timestamp() )

        self.data = { 'expire'   : int(expire),
                      'logerrors': False,
                      'loglevel' : loglevel,
                      'logs'     : [],
                      'name'     : name,
                      'noerrors' : noerrors,
                      'shared'   : shared,
                      'simplelog': simplelog,
                      'time'     : starttime,
                      'tmp'      : "",
                      'unique'   : unique }

        self.data['logfile'] = JN( self.getDir('log'), f"log-{starttime}" )

        if initial:
            newtmp = True
        else:
            newtmp = False
            try:
                tmp = sorted( glob( f'??????????-{name}{unique}*.pyconfig', root_dir = tempfile.gettempdir() ), reverse = True )[0]
                if expire > 0:
                    now   = dt.now()
                    init  = dt.fromtimestamp( int(tmp.split('-')[0] ))
                    delta = now - init
                    if delta.seconds > expire:
                        log.error( f"Temporary file has reached expiration set time of {expire} seconds", nosave = True )
                        tmp    = ""
                        newtmp = True

            except IndexError:
                log.debug(f"No temp files found for '{name}'", nosave = True )
                newtmp = True

        if tmp and not newtmp:
            try:
                with open( JN( tempfile.gettempdir(), tmp ), 'r' ) as f:
                    d = json.load(f)
                self.data = { **self.data, **d }

                if not self.data['simplelog']:
                    log = logging.getLogger(__name__)
                    while self.data['logs']:
                        L = self.data['logs'].pop(0)
                        log.log( L['level']*10, f"{L['msg']}\x1b[2;37m [repeated for records]\x1b[0m" )
                else:
                    log.level = self.data['loglevel']

                log.debug(f"Loaded existing temp data from '{tmp}'")

            except json.JSONDecodeError as E:
                log.error(f"{str(E)}")
                log.error( f"Error reading tmp file '{tmp}' - removing and recreating", nosave = True )
                tmp    = ""
                newtmp = True

        if newtmp:
            if not name:
                raise ValueError( "Initial call from application must include a name" )

            self.cleanTmp()
            atexit.register( self.onExit, tmp )

        if shared:
            self.addSharedData( **shared )

        self.save( self.data )

    def __call__(self, *args):
        if not args:
            log.error("No data key(s) given")
            return None

        d = self.data
        args = list(args)
        try:
            while args:
                d = d[args.pop(0)]
        except KeyError:
            log.error("Invalid data key(s)")
            return None

        return d

    @staticmethod
    def save(obj):
        nosave = { 'nosave': True }
        if isinstance( log, logging.getLoggerClass() ):
            nosave = {}

        with open( obj['tmp'], 'w' ) as f:
            json.dump( obj, f, separators = ( ',', ':' ))

        log.debug( f"Temporary file saved as '{obj['tmp']}'", **nosave )

    @staticmethod
    def getRuntime( obj ):
        now = dt.now()
        start = dt.fromtimestamp( self.data['start'] )
        delta = now - start

        secs, mins, hrs = delta.seconds, 0, 0
        if secs > 60:
            mins = int( secs / 60 )
            secs = secs % 60

        if mins > 60:
            hrs = int( mins / 60 )
            mins = mins % 60

        return { 'start'  : start.strftime('%A, %b %d, %Y @ %r'),
                 'end'    : now.strftime('%A, %b %d, %Y @ %r'),
                 'runtime': f"{hrs:02d}:{mins:02d}:{secs:02d}" }

    def _fromSimpleLog(self, level, **logdata):
        assert len(set([ 'levelname', 'msg', 'formatted', 'time' ]) & set(logdata)) == 4
        self.data['logs'].append({ 'level'    : level,
                                   'levelname': logdata['levelname'],
                                   'msg'      : logdata['msg'],
                                   'formatted': logdata['formatted'],
                                   'time'     : logdata['time'] })
        if 'errors' in logdata:
            self.data['logerrors'] = True

        if 'nosave' in logdata:
            return
        self.save( self.data )

    def addSharedData(self, **kwargs):
        """
        Add dictionary data to the tmp file to share with other modules during session
            - available using the __call__ method, first argument 'shared'
        """
        if isinstance( shared, dict ):
            self.data['shared'] = { **self.data['shared'], **shared }
        else:
            log.error("Shared data must be in dictionary form")
            return

        self.save( self.data )

    def cleanTmp(self):
        """
        Removes all temp files matching app name and unique id (if given) except the current
          file - self.data['tmp']
            - returns number of files removed
        """
        # NameError for os during atexit call???
        import os

        nosave = { 'nosave': True }
        if isinstance( log, logging.getLoggerClass() ):
            nosave = {}

        tmplist = []
        for i in range(9, 13):
            tmplist += sorted( glob( f"{'':?<{i}}-{self['name']}{self['unique']}*.pyconfig", root_dir = tempfile.gettempdir() ))
        if not tmplist:
            return 0

        count = 0
        while True:
            if len( tmplist ) <= 1:
                break

            T = tmplist.pop(0)
            os.remove( JN( tempfile.gettempdir(), T ))
            log.warning( f"Temporary file deleted - {T}", **nosave )
            count += 1

        return count

    def clearSharedData(self, *args):
        nosave = { 'nosave': True }
        if isinstance( log, logging.getLoggerClass() ):
            nosave = {}

        self.data['shared'] = {}
        log.info( "Clear shared data from temp file", **nosave )

        self.save( self.data )

    def getDir(self, _dir ):
        """
        Return user application directories
            _dir = 'cache' - user cache directory
                   'data'  - user app data directory
                   'log'   - log directory in user app data

            - creates directory if it doesn't exist
        """
        DIR = { 'darwin' : { 'cache': JN( expanduser('~'), "Library", "Application Support", self.data['name'], "cache" ),
                             'data' : JN( expanduser('~'), "Library", "Application Support", self.data['name'] ),
                             'log'  : JN( expanduser('~'), "Library", "Application Support", self.data['name'], 'logs' )},
                'windows': { 'cache': JN( expanduser('~'), "AppData", self.data['name'], "cache" ),
                             'data' : JN( expanduser('~'), "AppData", self.data['name'] ),
                             'log'  : JN( expanduser('~'), "AppData", self.data['name'], 'logs' )},
                'linux'  : { 'cache': JN( expanduser('~'), ".cache" , self.data['name'] ),
                             'data' : JN( expanduser('~'), ".config", self.data['name'] ),
                             'log'  : JN( expanduser('~'), ".config", self.data['name'], 'logs' )}}

        d = DIR[ sys.platform ][ _dir ]
        os.makedirs( d, exist_ok = True )

        return d

    def getLogfile(self):
        logdir = DN( self.data['logfile'] )

        if not self.hasLogfile():
            loglist = sorted( os.listdir( logdir ), reverse = True )
            date = dt.fromtimestamp( self.data['time'] ).strftime('%A, %b %d, %Y - %r')

            while len( loglist ) >= 10:
                os.remove( JN( logdir, loglist.pop(0) ))

            with open( self.data['logfile'], 'w' ) as f:
                f.write( f"# {self.data['name']} Log - {date}\n\n" )

        return logfile

    def getAppName(self):
        return self.data['name']

    def getTmpFile(self):
        return self.data['tmp']

    def getStartTime(self):
        return dt.fromtimestamp( self.data['time'] )

    def hasLogFile(self):
        if isfile( self.data['logfile'] ):
            return True
        return False

    def onExit(self):
        """
        Called on exit to clean up tempfiles
        """

        # NameError for os during atexit call???
        import os

        nodata = { 'nodata': True }
        nosave = { 'nosave': True }
        if isinstance( log, logging.getLoggerClass() ):
            nodata = {}
            nosave = {}

        with open( tmpfiles[0], 'r' ) as f:
            self.data = json.load(f)

        self.cleanTmp()
        try:
            os.remove( self['tmp'] )
            log.debug( f"Removed current temp file - '{self['tmp']}'", **nosave )
        except Exception as E:
            log.error( f"{str(E)}", **nosave )

        if not isinstance( log, logging.getLoggerClass() ):
            if self.print_log_on_exit and self.data['logerrors'] and self.data['loglevel'] == 0:
                log_msgs = [ i['formatted'] for i in sorted( logs, key = lambda x: x['time'] )]
                sys.stderr.write('\n')
                for i in log_msgs:
                    sys.stderr.write(f"{i}\n")

            if self.data['simplefile'] and self.data['logs']:
                time = dt.fromtimestamp( int( self.data['time']/86400 ) * 86400 ).timestamp()
                file = JN(DN( self.data['logfile'] ), f"BBAppDirs-{time}.log" )
                with open( file, 'a+' ) as f:
                    if not f.tell():
                        f.write( f"" )
                    for i in self.data['logs']:
                        f.write( f"" )

        rt = self.getRuntime( self.data )
        log.info( "Process completed", **nosave )
        log.info( f"Started: {rt['start']}", **nosave )
        log.info( f"Ended: {rt['end']}", **nosave )
        log.info( f"Total Runtime: {rt['runtime']}", **nosave )
        log.info( "Exiting now...", **nosave )

class SimpleLog:
    """
    SimpleLog

      A simple logger. Is used during initial call to AppDirs to give the application
    the chance to initiate python's logging module before loading it here.

    """
    CB = None

    def __init__(self, level = 0, *, log_to_data = None):
        """
        Initiate SimpleLog

          *args
            - level = 0: off [default]
                      1: debug
                      2: info
                      3: warning
                      4: error
                      5: critical

          **kwargs:
            - log_to_data = callback function to write log data to temp file

            Similar to the standard built-in logging, messages from set level and above
          will be displayed. Level set to 0 will turn SimpleLog off. This does not effect
          python's built-in logging module.

        """
        try:
            assert level >= 0 and level <= 5
            self.level = level
        except:
            self.level = 3
            self.critical("Invalid log level for SimpleLog")
            self.warning("Setting log level to 0 (off)")
            self.level = 0

        self.CB = log_to_data

    def debug(self, _str, **kwargs):
        self._log( "\x1b[2;37m", 'debug', _str, **kwargs )

    def info(self, _str, **kwargs):
        self._log( "\x1b[0;36m", 'info', _str, **kwargs )

    def warning(self, _str, **kwargs):
        self._log( "\x1b[1;33m", 'warning', _str, **kwargs )

    def error(self, _str, errors = True, **kwargs):
        self._log( "\x1b[0;31m", 'error', _str, **kwargs )

    def critical(self, _str, errors = True, **kwargs):
        self._log( "\x1b[1;31m", 'critical', _str, **kwargs )

    def _log(self, col, L, _str, **kwargs):
        levels = { 'debug'   : 1,
                   'info'    : 2,
                   'warning' : 3,
                   'error'   : 4,
                   'critical': 5 }

        formatted = f"{col}  [{L.upper()}]\x1b[0;3m {_str}\x1b[0m"
        T = dt.now()

        if 'nodata' in kwargs:
            pass
        elif self.CB:
            time = int( T.timestamp() )
            self.CB( levels[L],
                     levelname = L.upper(),
                     msg = _str,
                     time = time,
                     formatted = formatted,
                     **kwargs )

        if self.level > 0 and self.level <= levels[L]:
            sys.stderr.write(f"{col}  [{L}]\x1b[0;3m {_str}\x1b[0m")
