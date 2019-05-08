# encoding=utf-8
import os
import platform
import logging


if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('Logging to:', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='a',
)

logging.debug('Debug message')
logging.info('Common info')
logging.warning('Warning message')

# Local Result of This Demo:
# Logging to: C:\Users\Administrator\test.log
