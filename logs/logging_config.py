log_config = {
    'version': 1,
    'formatters': {
        'common_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%d-%m-%Y %H:%M',
        },
    },
    'handlers': {
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'common_formatter'
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'formatter': 'common_formatter',
            'filename': 'logs/errors.log',
            'delay': True,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'stream_logger': {
            'handlers': ['stream_handler'],
            'level': 'INFO',
        },
        'file_logger': {
            'handlers': ['file_handler'],
            'level': 'DEBUG',
        },
    },
}
