from abc import ABC, abstractmethod
from typing import Any


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
        print('\nInitializing Numeric Processor...')
        return (f'Processing data: {data}')

    def validate(self, data: Any) -> bool:
        if isinstance(data, list) is not True:
            return False
        for d in data:
            if isinstance(d, int) is False:
                return False
        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print('\nInitializing Text Processor...')
        return (f'Processing data: "{data}"')

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) is True:
            return True
        else:
            return False

# class LogProcessor(DataProcessor):


if __name__ == '__main__':
    print('=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===')

    numeric_list: list = [1, 2, 3, 4, 5]
    numeric = NumericProcessor()

    print(numeric.process(numeric_list))

    if numeric.validate(numeric_list) is True:
        print('Validation: Numeric data verified')
    else:
        print('Not numeric only')

    print(numeric.format_output(
        f'Processed {len(numeric_list)} numeric values, '
        f'sum={sum(numeric_list)}, '
        f'avg={sum(numeric_list) / len(numeric_list)}'
        )
    )

    text_str: str = "Hello Nexus World"
    text = TextProcessor()

    print(text.process(text_str))

    if text.validate(text_str) is True:
        print('Validation: Text data verified')
    else:
        print('Not string only')

    print(text.format_output(
        f'Processed text: {len(text_str)} characters, '
        f'{len(text_str.split())} words'
    ))

    
