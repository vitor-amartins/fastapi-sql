import logging
import sys
from os import environ

logger = logging.getLogger('logger')
logger.setLevel(environ.get('LOG_LEVEL', 'INFO'))

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s"))

logger.addHandler(console_handler)
