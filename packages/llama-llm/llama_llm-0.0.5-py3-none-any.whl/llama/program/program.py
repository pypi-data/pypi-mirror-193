from llama.program.function import Function
from llama.program.util.type_to_dict import type_to_dict


class Program:
    """Internal representation of a program that can be executed by the Llama
    large language model engine.

    Each program has a unique name (within your account).

    """

    def __init__(self, name):
        self.name = name
        self.main = Function(program=self, name="main")
        self.functions = {"main": self.main}
        self.examples = []

    def add_data(self, examples):
        self.examples.extend(examples)

    def add_metric(self, metric):
        self.add_operation(metric)

    def to_dict(self):
        dict_object = {
            "name": self.name,
            "functions": {
                name: function.to_dict() for name, function in self.functions.items()
            },
            "examples": [
                {
                    "input": type_to_dict(example["input"]),
                    "output": type_to_dict(example["output"]),
                }
                for example in self.examples
            ],
        }

        return dict_object
