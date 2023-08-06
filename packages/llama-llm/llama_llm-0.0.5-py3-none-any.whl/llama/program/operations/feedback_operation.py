
from llama.program.value import Value
from llama.types.type import Type
from llama.types.context import Context

from llama.program.util.type_to_dict import type_to_dict

import json

class FeedbackType(Type):
    result: bool = Context("The result of the feedback test")

class FeedbackOperation(Value):
    def __init__(self, on, to, good_examples=[], bad_examples=[]):
        super().__init__(FeedbackType)
        self.on = on
        self.to = to
        self.good_examples = good_examples
        self.bad_examples = bad_examples

    def to_dict(self):
        return {
            "name" : "FeedbackOperation",
            "on" : self.on,
            "to" : self.to,
            "good_examples" : [type_to_dict(example) for example in self.good_examples],
            "bad_examples" : [type_to_dict(example) for example in self.bad_examples],
            "type" : json.loads(self.type.schema_json()),
        }



