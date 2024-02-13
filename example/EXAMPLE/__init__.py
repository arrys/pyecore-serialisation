
from .EXAMPLE import getEClassifier, eClassifiers
from .EXAMPLE import name, nsURI, nsPrefix, eClass
from .EXAMPLE import Example


from . import EXAMPLE

__all__ = ['Example']

eSubpackages = []
eSuperPackage = None
EXAMPLE.eSubpackages = eSubpackages
EXAMPLE.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
