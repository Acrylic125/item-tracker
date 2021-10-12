class Resource:
    def __init__(self, id: str, recipe):
        self.id = id
        self.recipe = recipe

    def hasRecipe(self) -> bool:
        return self.recipe is not None

