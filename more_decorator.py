# encoding=utf-8
import os
import platform
from time import sleep
from functools import wraps
import logging

# As follows, without any basic config, the logging message would not be written into any log file, but popped up to the screen.
# logging.basicConfig()

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='a',
)

log = logging.getLogger('retry')


def retry(f):
    @wraps(f)
    def wrapper_function(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except Exception:
                log.exception('Attempt %s/%s failed: %s', attempt, MAX_ATTEMPTS, (args, kwargs))
                sleep(10 * attempt)
        log.critical('All %s attempts failed: %s', MAX_ATTEMPTS, (args, kwargs))
    return wrapper_function


counter = 0


@retry
def save_to_database(arg):
    print('Write to a database or make a network call or etc.')
    print('This will be automatically retried only if exception is thrown.')
    global counter
    counter += 1
    # This will throw an exception in the 1st call
    # and will work fine in the 2nd call (i.e. a retry)
    if counter < 2:
        raise ValueError(arg)


# print('Counter:', counter)
# print('__name__:', __name__)  # __main__

if __name__ == '__main__':
    save_to_database('Some bad value')
