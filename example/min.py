from pyecore.resources import ResourceSet, URI
from pyecore.resources.xmi import XMIResource

from example import EXAMPLE


def main():
    for _ in range(2):
        # Read the original file
        resources = ResourceSet()
        resources.metamodel_registry['http://www.example.org/EXAMPLE'] = EXAMPLE
        resource = resources.get_resource(URI('min.example'))
        example = resource.contents[0]
        # Write the loaded model back
        resource = XMIResource(URI('min.example'))
        resource.append(example)
        resource.save()

if __name__ == "__main__":
    main()
