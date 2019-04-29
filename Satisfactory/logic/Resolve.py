from . AssignRecipes import AssignRecipes
from . Tracker import Tracker

class Resolve:
    def __init__(self):
        self.graph = AssignRecipes()
    def get_material(self, materialName):
        for m in self.graph.materials:
            if m == materialName:
                return m

    def is_atomic(self,recipe):
        for material, _ in recipe.inputs.items():
            material = self.get_material(material)
            if material.recipes != []:
                return False
        return True

    # def resolve_it(self, materialName, materialQuantity=1):
    #     trackers = []
    #     material = self.get_material(materialName)
    #     if material.recipes == []:
    #         print(f'{material.name} is already Atomic')
    #         return
    #
    #     recipe = material.recipes[0]
    #         tracker = Tracker()
    def locked(self,tracker):
        print(tracker.recipes)
        for recipe in tracker.recipes:
            if not self.is_atomic(recipe): return False
        return True

    def resolve_rec(self, materialName, materialQuantity=1, tracker=None):
        material = self.get_material(materialName)
        if material.recipes == []:
            if tracker is not None:
                pass
                # print(tracker.mats)
        else:
            for recipe in [material.recipes[0]]:
                # print(f'{recipe.name} atomic: {self.is_atomic(recipe)}')
                if tracker is None:
                    tracker=Tracker()
                tracker.add_recipe(recipe)
                for mat, quantity in recipe.inputs.items():
                    tracker.add_mats(mat,quantity)
                    # print(mat, material.name, recipe.name)
                    self.resolve_rec(mat, quantity, tracker)
