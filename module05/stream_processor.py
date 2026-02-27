from abc import ABC, abstractmethod
from typing import Any

class DataError(Exception):
    pass


class NumericError(DataError):
    pass


class TextError(DataError):
    pass


class LogError(DataError):
    pass


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f'Output: {result}')


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            raise NumericError("The list does not contain only numerical values.")

        return (
            f'Processed {len(data)} numeric values, '
            f'sum={sum(data)}, '
            f'avg={sum(data) / len(data)}'
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list) is not True:
            return False
        for d in data:
            if isinstance(d, int) is False:
                return False
        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            raise TextError('The text is not a string')

        return (
            f'Processed text: {len(data)} characters, '
            f'{len(data.split())} words'
        )


    def validate(self, data: Any) -> bool:
        if isinstance(data, str) is not True:
            return False
        else:
            return True


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if self.validate(data) is not True:
            raise LogError("Invalid log format.")

        level, message = data.split(":", 1)
        level = level.strip()
        message = message.strip()

        return f'[{level}] {level} level detected: {message}'

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        if ":" not in data:
            return False
        return True


if __name__ == '__main__':
    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===')

    numeric_list: list = [1, 2, 3, 4, 5]
    numeric = NumericProcessor()
    print('\nInitializing Numeric Processor...\n'
              f'Processing data: {numeric_list}'
        )

    try:
        print('Validation: Numeric data verified')
        result = numeric.process(numeric_list)
        print(numeric.format_output(result))
    except NumericError as err:
        print(f'Error: {err}')


    text_str: str = "Hello Nexus World"
    text = TextProcessor()
    print(
        '\nInitializing Text Processor...\n'
        f'Processing data: {text_str}'
    )

    try:
        print('Validation: Text data verified')
        result = text.process(text_str)
        print(text.format_output(result))
    except TextError as err:
        print(f'Error: {err}')


    log_text: str = "ERROR: Connection timeout"
    log = LogProcessor()
    print(
        '\nInitializing Log Processor...\n'
        f'Processing data: {log_text}'
    )

    try:
        print('Validation: Log entry verified')
        result = log.process(log_text)
        print(log.format_output(result))
    except LogError as err:
        print(f'Error: {err}')


    poly = [NumericProcessor(), TextProcessor(), LogProcessor()]
    data = [[2, 2, 2], 'Hello Word!z', 'INFO: System ready']
    print(
        '\n=== Polymorphic Processing Demo ===\n'
        'Processing multiple data types through same interface...'
    )

    for pol, dat in zip(poly, data):
        res = pol.process(dat)
        print(pol.format_output(res))

    print('\nFoundation systems online. Nexus ready for advanced streams.')
