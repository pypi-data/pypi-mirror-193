import logging
import ipyparams
from pathlib import Path
from IPython.display import display, HTML
from uuid import uuid4


class DisplayLogsHandler(logging.Handler):
    def emit(self, record):
        message = self.format(record)
        display(message)
        
        
class HTMLLogsFormatter(logging.Formatter):
    level_colors = {
        logging.DEBUG: 'lightgray',
        logging.INFO: 'dodgerblue',
        logging.WARNING: 'goldenrod',
        logging.ERROR: 'crimson',
        logging.CRITICAL: 'firebrick'
    }
    
    def __init__(self):
        super().__init__(
            '【 <span style="font-weight: bold; color: {levelcolor}">{levelname}</span> 】 '
            '{message}',
            style='{'
        )
    
    def format(self, record):
        record.levelcolor = self.level_colors.get(record.levelno, 'black')
        return HTML(super().format(record))


class FancyLogger:    
    def __init__(self, default_log_level='INFO'):
        self._logger = logging.getLogger(str(uuid4())) # we don't want to be able to reuse this logger anywhere else
        self._console_handler = DisplayLogsHandler()
#         self._file_handler = logging.FileHandler(f'{Path(ipyparams.notebook_name).stem}.log')
        self._console_handler.setFormatter(HTMLLogsFormatter())
#         self._file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self._logger.addHandler(self._console_handler)    
#         self._logger.addHandler(self._file_handler) 
        self.set_log_level(default_log_level)
        
    def _parse_log_level(self, log_level):
        if  log_level.upper() == 'DEBUG':
            return logging.DEBUG, 'DEBUG'
        elif  log_level.upper() == 'INFO':
            return logging.INFO, 'INFO'
        elif  log_level.upper() == 'WARNING':
            return logging.WARNING, 'WARNING'
        elif  log_level.upper() == 'ERROR':
            return logging.ERROR, 'ERROR'
        elif  log_level.upper() == 'CRITICAL':
            return logging.CRITICAL,'CRITICAL'
        else:
            raise ValueError(f'{log_level} is an invalid log level. Valid: DEBUG/INFO/WARNING/ERROR/CRITICAL')
        
    @property
    def log_level(self):
        return self._log_level_name
    
    def set_log_level(self, log_level):
        self._log_level, self._log_level_name = self._parse_log_level(log_level)
        self._logger.setLevel(self._log_level)
        
    def log(self, message):
        self._logger.log(self._log_level, message)
        
    def info(self, message):
        self._logger.info(message)
        
    def warn(self, message):
        self._logger.warning(message)
    
    def error(self, message):
        self._logger.error(message)
    
    def crit(self, message):
        self._logger.critical(message)