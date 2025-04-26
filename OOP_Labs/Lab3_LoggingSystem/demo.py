import log_filter
import log_handler
from logger import Logger

filters = [
        log_filter.SimpleLogFilter('IMPORTANT'),
        log_filter.SimpleLogFilter('INFO'),
        log_filter.RegexLogFilter(r'(ERROR|WARNING) \d+')
        ]

handlers = [
        log_handler.ConsoleLogHandler(),
        log_handler.FileLogHandler('logs/log.log'),
        log_handler.SocketLogHandler('localhost', 5140),
]

logger = Logger(filters, handlers)

messages = [
        'INFO: Test message',
        'WARNING: Thanks for attention lol',
        'ERROR 404: Resource not found',
        'DEBUG: Unreachable'
        ]

for msg in messages:
    logger.log(msg)