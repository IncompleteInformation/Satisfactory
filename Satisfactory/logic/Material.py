class Material:
    def __init__(self,name):
        self.name = name
        self.recipes = []
    def __eq__(self, other):
        if isinstance(other, Material):
            return self.name == other.name
        else:
            return self.name == other
    # def __repr__(self):
    #     return self.__class__.__name__
