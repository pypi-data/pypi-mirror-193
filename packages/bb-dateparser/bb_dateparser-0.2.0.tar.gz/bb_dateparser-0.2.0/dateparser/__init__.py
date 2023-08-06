__version__ = '0.1.0'

import logging
from bblogger.logger import BBLogger, getLogger

if logging.getLoggerClass() != BBLogger:
    log = getLogger(__name__, level = 3, appname = "DateParser")

from .dateparser import DateParser

__all__ = [ 'DateParser' ]
