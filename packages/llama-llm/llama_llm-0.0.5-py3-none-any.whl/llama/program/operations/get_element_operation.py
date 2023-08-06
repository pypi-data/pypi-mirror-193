
from llama.program.value import Value

from llama.program.util.type_to_dict import type_to_dict

import json

class GetElementOperation(Value):
    def __init__(self, input_value, type, element_index):
        super().__init__(type)
        self.element_index = element_index
        self.input_value = input_value

    def to_dict(self):
        input_value = type_to_dict(self.input_value)
        return {
            "name" : "GetElementOperation",
            "input_value" : input_value,
            "type" : json.loads(self.type.schema_json()),
            "element_index" : self.element_index,
        }

