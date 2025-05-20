import log_filter
import log_handler


class Logger:
    def __init__(self,
                 filters: list[log_filter.LogFilterProtocol],
                 handlers: list[log_handler.LogHandlerProtocol]):
        self.filters = filters
        self.handlers = handlers
        
    def log(self, text: str):
        if all(filter_cls.match(text) for filter_cls in self.filters):
            for handler in self.handlers:
                handler.handle(text)
