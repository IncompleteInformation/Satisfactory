from . Materials import Materials
from . Recipes import Recipes
# [print(type(o)) for o in globals()]
class AssignRecipes:
    def __init__(self):
        self.materials = Materials()
        self.recipes = Recipes()
        # [print(type(m)) for m in self.materials]
        # [print(type(m)) for m in self.recipes]
        for r in self.recipes:
            for m in self.materials:
                if r.name[:-1] == m.name:
                    m.recipes.append(r)
