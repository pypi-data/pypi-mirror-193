
from llama.program.value import Value

class ReturnOperation(Value):
    def __init__(self, output_value):
        super().__init__(get_type(output_value))
        self.output_value = output_value

    def to_dict(self):
        if type(self.output_value) == tuple:
            output_value = [value_to_dict(value) for value in self.output_value]
        else:
            output_value = value_to_dict(self.output_value)

        return {
            "name" : "ReturnOperation",
            "output_value" : output_value,
        }

def value_to_dict(value):
    if isinstance(value, Value):
        value = value.index
    else:
        value = value.dict()

    return value

def get_type(output_value):
    if type(output_value) == tuple:
        return (value.type for value in output_value)

    return output_value.type


