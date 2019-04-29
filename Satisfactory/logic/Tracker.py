class Tracker:
    def __init__(self):
        self.mats = {}
        self.recipes = []

    def add_mats(self,materialName,quantity):
        if not materialName in self.mats:
            self.mats[materialName] = quantity
        else:
            self.mats[materialName] += quantity

    def add_recipe(self,recipe):
        self.recipes.append(recipe)

    def merge(self,tracker):
        for k,v in tracker.mats:
            self.add(k,v)
