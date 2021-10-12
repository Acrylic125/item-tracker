import Inventory
import Recipe
import Resource
import resourceRegistry

iron = Resource.Resource('iron', None)
carbon = Resource.Resource('carbon', None)
steelPlating = Resource.Resource('steelPlating', Recipe.Recipe([
    Recipe.RecipeResource(iron.id, 3),
    Recipe.RecipeResource(carbon.id, 2),
]))
reinforcedSteelPlating = Resource.Resource('reinforcedSteelPlating', Recipe.Recipe([
    Recipe.RecipeResource(iron.id, 5),
    Recipe.RecipeResource(carbon.id, 3),
    Recipe.RecipeResource(steelPlating.id, 1),
]))


resourceRegistry.registerResources([
    iron, carbon, steelPlating, reinforcedSteelPlating
])

inventory = Inventory.Inventory({})
inventory.addItemAmount(iron, 7)
inventory.addItemAmount(carbon, 5)

print(reinforcedSteelPlating.recipe.convert(inventory))
