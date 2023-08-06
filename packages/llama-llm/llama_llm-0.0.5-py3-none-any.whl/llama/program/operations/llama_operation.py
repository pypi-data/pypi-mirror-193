
from llama.program.value import Value

from llama.program.util.type_to_dict import type_to_dict

import json

class LlamaOperation(Value):
    def __init__(self, input_value, output_type, *args, **kwargs):
        super().__init__(output_type)
        self.input_value = input_value
        self.args = {
            "args" : args,
            "kwargs" : kwargs
        }

    def to_dict(self):
        input_value = type_to_dict(self.input_value)

        return {
            "name" : "LlamaOperation",
            "input_value" : input_value,
            "type" : json.loads(self.type.schema_json()),
            "args" : self.args
        }


