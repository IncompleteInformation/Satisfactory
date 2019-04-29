from . Material import *

class Recipe:
    def __init__(self, name, inputs=None, outputs=None, factory=None):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.factory = factory

    def __repr__(self):
        return f'{self.name}: \n\tInputs: {self.inputs}\n\tOutputs: {self.outputs}\n\tFactory: {self.factory}'
