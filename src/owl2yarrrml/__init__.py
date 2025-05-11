
from .translate import *


def translate(ontology):
    template = init_yarrrml()
    construct_mapping(template, ontology)
    return template
