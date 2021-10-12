import Resource

resources = {}


def getResource(resourceID: str):
    return resources[resourceID]


def registerResource(resource: Resource):
    resources[resource.id] = resource


def registerResources(resources: [Resource]):
    for resource in resources:
        registerResource(resource)
