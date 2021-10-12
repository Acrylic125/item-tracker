import resourceRegistry
from Inventory import Inventory


class RecipeResource:
    def __init__(self, resourceID: str, amount: int):
        self.resourceID = resourceID
        self.amount = amount

    def getResource(self):
        return resourceRegistry.getResource(self.resourceID)


class RecipeTemporaryInventory:
    def __init__(self, inventory: Inventory):
        self.temporaryInventory = Inventory(dict(inventory.contents))


class Recipe:
    def __init__(self, resourcesRequired: [RecipeResource]):
        self.resourcesRequired = resourcesRequired

    def canConvert(self, inventory: Inventory):
        for resourceItem in self.resourcesRequired:
            if inventory.getAmountByID(resourceItem.resourceID) < resourceItem.amount:
                return False
        return True

    def convert(self, inventory: Inventory, amount = 1):
        for resourceItem in self.resourcesRequired:
            resourceID = resourceItem.resourceID
            inventoryAmount = inventory.getAmountByID(resourceID)
            requirementAmount = (resourceItem.amount * amount)
            needed = requirementAmount - inventoryAmount
            if needed <= 0:
                inventory.removeItemAmountByID(resourceID, requirementAmount)
            else:
                resource = resourceRegistry.getResource(resourceID)
                if resource.recipe is None or not resource.recipe.convert(inventory, needed):
                    return False
                inventory.removeItemAmount(resource, requirementAmount)
        return True



