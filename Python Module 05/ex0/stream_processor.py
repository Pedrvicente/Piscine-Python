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
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        total = sum(data)
        average = total / len(data)
        return (f"Processed {len(data)} numeric values, "
                f"sum={total}, avg={average}")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return True
        return False

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        total = len(data)
        words = data.split()
        total_words = len(words)
        return (f"Processed Processed text: {total} characters, "
                f"{total_words} words")

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        parts = data.split(": ")
        level = parts[0]
        message = parts[1]
        return f"[ALERT] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


if __name__ == '__main__':

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Numeric Processor
    print("Initializing Numeric Processor...")

    num = NumericProcessor()

    data = [1, 4, 5, 6]
    num.process(data)
    print(f"Processing data: {data}")

    if num.validate(data):
        print("Validation: Numeric data verified")

    result = num.process(data)
    print(num.format_output(result))

    print()

    # Text Processor
    print("Initializing Text Processor...")

    text = TextProcessor()

    data = "Hello Nexus World"
    text.process(data)
    print(f"Processing data: {data}")

    if text.validate(data):
        print("Validation: Text data verified")

    result = text.process(data)
    print(text.format_output(result))

    print()

    # Log processor
    print("Initializing Log Processor...")

    error = LogProcessor()

    data = "ERROR: Connection timeout"
    error.process(data)
    print(f"Processing data: {data}")

    if error.validate(data):
        print("Validation: Log entry verified")

    result = error.process(data)
    print(error.format_output(result))

    print()

    # poliformismo
    print("=== Polymorphic Processing Demo ===")

    print("Processing multiple data types through same interface...")

    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    test_data = [[1, 2, 3], "Hello World", "INFO: System ready"]

    for i, (process, data) in enumerate(zip(processors, test_data), 1):
        if process.validate(data):
            res = process.process(data)
            print(f"Result {i}: {process.format_output(res)}")

    print()

    print("Foundation systems online. Nexus ready for advanced streams.")
