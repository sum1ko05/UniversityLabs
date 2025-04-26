from person import Person, CommonAgeValidator, NameValidator, PropertyLogger
from logger.logger import Logger
from logger.log_filter import SimpleLogFilter
from logger.log_handler import ConsoleLogHandler, FileLogHandler


person = Person("Marisa", 19)
logger = PropertyLogger(Logger([SimpleLogFilter('Info'), SimpleLogFilter('Error')],
                                      [ConsoleLogHandler(), FileLogHandler('logs/log.log')]))
person.add_property_changed_listener(logger)
    
age_validator = CommonAgeValidator()
name_validator = NameValidator()
person.add_property_changing_listener(age_validator)
person.add_property_changing_listener(name_validator)
    
person.name = "Reimu"     # Valid
person.age = 20         # Valid
    
person.age = -5         # Invalid
person.name = "123"     # Invalid
person.age = 150        # Invalid
person.name = "A"       # Invalid