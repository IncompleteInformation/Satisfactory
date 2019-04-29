# from Satisfactory.logic import Material
# from Satisfactory.logic import Materials
# from Satisfactory.logic import Recipes
# from Satisfactory.logic import AssignRecipes
from Satisfactory.logic import Resolve
# [print(o) for o in globals()]
# x = Material()

# print (x)
# print(dir(IronIngot))
# [print(o) for o in globals()]
# print(dir(IronPlate))
# print(Materials.IronPlate.recipes.inputs)
# x=Materials()
# [print(eval(f'x.{o}.name')) for o in dir(x) if eval(f'isinstance(x.{o}, Material)')]
# [print(eval(f'x.{o} == "Power"')) for o in dir(x) if eval(f'isinstance(x.{o}, Material)')]
# x=Recipes()
# [print(m) for m in x]
# x=AssignRecipes()
# [print(m.name) for m in x.materials]
# [print(m) for m in x.recipes]
x=Resolve()
x.resolve_rec('SteelBeam')

# x.resolve_it('IronOre')
