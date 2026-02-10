from typing import Protocol, Any, List
from abc import ABC, abstractmethod


class DataProcessor(Protocol):
    def process(self, data: Any):
        ...


class NumberProcessor:
    def process(self, data: Any) -> str:
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return f"Number: {data}"
        else:
            return "Number: (invalid)"


class TextProcessor:
    def process(self, data: Any):
        bold = str(data).upper()
        return f"Text: {bold}"


class BoolProcessor:
    def process(self, data: Any):
        if isinstance(data, bool):
            return f"Bool: {data}"
        else:
            return "Bool: (invalid)"


class ProcessingPipeline:
    def __init__(self):
        self.processors: List[DataProcessor] = []

    def add_processor(self, processor: DataProcessor) -> 'ProcessingPipeline':
        self.processors.append(processor)
        return self

    def run(self, data: Any) -> List[str]:
        result = [processor.process(data) for processor in self.processors]
        return result


if __name__ == '__main__':

    pipeline = (ProcessingPipeline().add_processor(TextProcessor()).add_processor(NumberProcessor()))
    results = pipeline.run(42)
    for r in results:
        print(r)