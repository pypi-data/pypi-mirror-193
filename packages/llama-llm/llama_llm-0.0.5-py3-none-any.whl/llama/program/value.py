import asyncio
from typing import List
from llama.program.util.run_ai import query_run_program

class Value:
    def __init__(self, type, data=None):
        self.type = type
        self.data = data
        self.function = None
        self.index = None

    def get_field(self, name):
        if self.data is None:
            self._compute_value()

        return self.data._get_attribute_raw(name)

    def set_function(self, function):
        self.function = program

    def __str__(self):
        if self.data is None:
            self._compute_value()

        return str(self.data)

    def _compute_value(self):
        params = {
            "program": self.function.program.to_dict(),
            "requested_value": self.index,
        }
        
        response = query_run_program(params)

        response.raise_for_status()
        self.data = self.type.parse_obj(response.json()["data"])



def gen_multiple_values(values: List[Value]):
    program = values[0].function.program.to_dict()
    params = {
        "program": program,
        "requested_value": [v.index for v in values],
    }
    
    response = query_run_program(params)
    response.raise_for_status()
    for i, v in enumerate(values):
        v.data = v.type.parse_obj(response.json()[i]["data"])
    return values




