from abc import ABC, abstractmethod
from typing import Any, List


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
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")
            total = sum(data)
            average = total / len(data)
            return (f"Processed {len(data)} numeric values, "
                    f"sum={total}, avg={average}")
        except ZeroDivisionError:
            return "Error: Empty data list"
        except TypeError:
            return "Error: Only numeric values accepted"
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, list):
                return False
            if len(data) == 0:
                return False
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        except Exception:
            return False


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")
            total = len(data)
            words = data.split()
            total_words = len(words)
            return (f"Processed text: {total} characters, "
                    f"{total_words} words")
        except AttributeError:
            return "Error: Data is not a string"
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                return False
            if len(data) == 0:
                return False
            return True
        except Exception:
            return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")
            parts = data.split(": ")
            level = parts[0]
            message = parts[1] if len(parts) > 1 else ""
            if level == 'ERROR':
                return f"[ALERT] {level} level detected: {message}"
            return f"[{level}] {level} level detected: {message}"
        except AttributeError:
            return "Error: Data is not a string"
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                return False
            if ": " not in data:
                return False
            return True
        except Exception:
            return False


if __name__ == '__main__':

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Numeric Processor
    print("Initializing Numeric Processor...")

    num = NumericProcessor()

    data: List[int] = [1, 4, 5, 6]

    print(f"Processing data: {data}")

    if num.validate(data):
        print("Validation: Numeric data verified")
    result = num.process(data)
    print(num.format_output(result))

    print()

    # Text Processor
    print("Initializing Text Processor...")

    text = TextProcessor()

    text_data: str = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')

    if text.validate(text_data):
        print("Validation: Text data verified")

    result = text.process(text_data)
    print(text.format_output(result))

    print()

    # Log processor
    print("Initializing Log Processor...")

    error = LogProcessor()

    log_data: str = "ERROR: Connection timeout"
    print(f'Processing data: "{log_data}"')

    if error.validate(log_data):
        print("Validation: Log entry verified")

    result = error.process(log_data)
    print(error.format_output(result))

    print()

    # poliformismo
    print("=== Polymorphic Processing Demo ===")

    print("Processing multiple data types through same interface...")

    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    test_data: List[Any] = [[1, 2, 3],
                            "Hello World",
                            "INFO: System ready"]

    for i, (process, data) in enumerate(zip(processors, test_data), 1):
        try:
            if process.validate(data):
                res = process.process(data)
                print(f"Result {i}: {res}")
            else:
                print(f"Result {i}: Validation failed")
        except Exception as e:
            print(f"Result {i}: Error - {e}")

    print()

    print("Foundation systems online. Nexus ready for advanced streams.")
