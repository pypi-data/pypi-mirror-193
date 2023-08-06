from llama.program.value import Value

import json


class CallOperation(Value):
    def __init__(self, target_function, input_value, output_value):
        super().__init__(get_type(output_value))
        self.target_function = target_function
        self.input_value = input_value

    def to_dict(self):
        if isinstance(self.input_value, Value):
            input_value = self.input_value.index
        else:
            input_value = {
                "data": self.input_value.dict(),
                "type": json.loads(type(self.input_value).schema_json()),
            }

        return {
            "name": "CallOperation",
            "function_name": self.target_function.name,
            "input_value": input_value,
        }


def get_type(output_value):
    if type(output_value) == tuple:
        return (value.type for value in output_value)

    return output_value.type
