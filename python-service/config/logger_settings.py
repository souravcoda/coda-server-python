# application logger
# ==============================================================================
import sys
import logging
from logging.config import dictConfig

from config import settings 
LOG_FILE_MAX_BYTES = settings.LOG_FILE_MAX_BYTES

logging_config = dict(
    version=1,
    disable_existing_loggers=False,
    formatters={
        'verbose': {
            'format': ("[%(asctime)s] %(levelname)s "
                       "[%(name)s:%(lineno)s] %(message)s"),
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    handlers={
        'application': {'class': 'logging.handlers.RotatingFileHandler',
                     'formatter': 'verbose',
                     'level': logging.DEBUG,
                     'filename': 'logs/application_error.log',
                     'maxBytes': LOG_FILE_MAX_BYTES,
                     'backupCount': 7},
        'load_testing': {'class': 'logging.handlers.RotatingFileHandler',
                     'formatter': 'verbose',
                     'level': logging.DEBUG,
                     'filename': 'logs/load_testing.log',
                     'maxBytes': LOG_FILE_MAX_BYTES,
                     'backupCount': 7},
        'streaming_process': {'class': 'logging.handlers.RotatingFileHandler',
                     'formatter': 'verbose',
                     'level': logging.DEBUG,
                     'filename': 'logs/streaming_process.log',
                     'maxBytes': LOG_FILE_MAX_BYTES,
                     'backupCount': 7},
        'kafka_producer_log': {'class': 'logging.handlers.RotatingFileHandler',
                     'formatter': 'verbose',
                     'level': logging.DEBUG,
                     'filename': 'logs/producer.log',
                     'maxBytes': LOG_FILE_MAX_BYTES,
                     'backupCount': 7},
        'kafka_consumer_log': {'class': 'logging.handlers.RotatingFileHandler',
                     'formatter': 'verbose',
                     'level': logging.DEBUG,
                     'filename': 'logs/consumer.log',
                     'maxBytes': LOG_FILE_MAX_BYTES,
                     'backupCount': 7},
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
    },
    loggers={
        'application_logger': {
            'handlers': ['application', 'console'],
            'level': logging.DEBUG
        },
        'kafka_producer_logger': {
            'handlers': ['kafka_producer_log', 'console'],
            'level': logging.DEBUG
        },
        'kafka_consumer_logger': {
            'handlers': ['kafka_consumer_log', 'console'],
            'level': logging.DEBUG
        },
        'streaming_process_logger': {
            'handlers': ['streaming_process', 'console'],
            'level': logging.DEBUG
        },
        'load_testing_logger': {
            'handlers': ['load_testing', 'console'],
            'level': logging.DEBUG
        }

    }
)

dictConfig(logging_config)

application_logger = logging.getLogger('application_logger')
streaming_process_logger = logging.getLogger('streaming_process_logger')
kafka_producer_logger = logging.getLogger('kafka_producer_logger')
kafka_consumer_logger = logging.getLogger('kafka_consumer_logger')
load_testing_logger = logging.getLogger('load_testing_logger')