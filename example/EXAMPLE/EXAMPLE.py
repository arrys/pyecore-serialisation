"""Definition of meta model 'EXAMPLE'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'EXAMPLE'
nsURI = 'http://www.example.org/EXAMPLE'
nsPrefix = 'EXAMPLE'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Example(EObject, metaclass=MetaEClass):

    values = EAttribute(eType=EDouble, unique=False, derived=False,
                        changeable=True, upper=-1, default_value=0.0)

    def __init__(self, *, values=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if values:
            self.values.extend(values)
