from llama.program.value import Value

class GetArgumentOperation(Value):
    def __init__(self, type, input_value_index):
        super().__init__(type)
        self.input_value_index = input_value_index

    def to_dict(self):
        return {
            "name" : "GetArgumentOperation",
            "index" : self.input_value_index
        }

