from Resource import Resource


class Inventory:
    def __init__(self, contents):
        self.contents = contents if contents is not None else {}

    def getAmountByID(self, resourceID: str):
        resourceAmount = self.contents.get(resourceID)
        if resourceAmount is None:
            self.contents[resourceID] = 0
            return 0
        return resourceAmount

    def getAmount(self, resource: Resource):
        return self.getAmountByID(resource.id)

    def addItemAmountByID(self, resourceID: str, amount: int):
        resourceAmount = self.getAmountByID(resourceID)
        self.contents[resourceID] = resourceAmount + amount

    def addItemAmount(self, resource: Resource, amount: int):
        self.addItemAmountByID(resource.id, amount)

    def removeItemAmountByID(self, resourceID: str, amount: int):
        self.addItemAmountByID(resourceID, -amount)

    def removeItemAmount(self, resource: Resource, amount: int):
        self.removeItemAmountByID(resource.id, amount)

