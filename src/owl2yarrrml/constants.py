


YAML_TEMPLATE = """
prefixes:
  xsd: http://www.w3.org/2001/XMLSchema#
  rr: http://www.w3.org/ns/r2rml#
  rml: http://semweb.mmlab.be/ns/rml#
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  ql: http://semweb.mmlab.be/ns/ql#
  rdfs: http://www.w3.org/2000/01/rdf-schema#
  foaf: http://xmlns.com/foaf/0.1/
  schema: http://schema.org/
  dc: http://purl.org/dc/elements/1.1/
  skos: http://www.w3.org/2004/02/skos/core#


mappings:
  triplesmap0:
    sources:
      - []
    s: http://$()
    po:
      - [a, class]
      - p: predicate
        o:
          - mapping: triplesmap2
            condition:
              function: equal
              parameters:
                - [str1, $()]
                - [str2, $()]
"""

##############################################################################
#############################   YARRRML CONSTANTS  ###########################
##############################################################################

YARRRML_PREFIXES = 'prefixes'
YARRRML_SOURCES = 'sources'
YARRRML_TABLE = 'table'
YARRRML_ACCESS = 'access'
YARRRML_QUERY = 'query'
YARRRML_REFERENCE_FORMULATION = 'referenceFormulation'
YARRRML_QUERY_FORMULATION = 'queryFormulation'
YARRRML_ITERATOR = 'iterator'
YARRRML_CREDENTIALS = 'credentials'
YARRRML_TYPE = 'type'
YARRRML_USERNAME = 'username'
YARRRML_PASSWORD = 'password'

YARRRML_STRUCTURE_DEFINER = 'structureDefiner'
YARRRML_SOFTWARE_SPECIFICATION = 'softwareSpecification'
YARRRML_PROGRAMMING_LANGUAGE = 'programmingLanguage'
YARRRML_SOFTWARE_REQUIREMENTS = 'softwareRequirements'

YARRRML_MAPPINGS = 'mappings' # used for mappings in conditions and mappings main key
YARRRML_MAPPING = 'mapping'

YARRRML_SUBJECTS = 'subjects'
YARRRML_AUTHORS = 'authors'
YARRRML_GRAPHS = 'graphs'

YARRRML_PREDICATEOBJECT = 'predicateobjects'

YARRRML_PREDICATES = 'predicates'
YARRRML_OBJECTS = 'objects'
YARRRML_VALUE = 'value'
YARRRML_DATATYPE = 'datatype'
YARRRML_LANGUAGE = 'language'

YARRRML_CONDITION = 'condition'
YARRRML_EQUAL = 'equal'
YARRRML_JOIN = 'join'
YARRRML_PARAMETERS = 'parameters' #used for conditions and functions

YARRRML_LITERAL = "literal"
YARRRML_IRI = '~iri'
YARRRML_LANG = '~lang'
YARRRML_BLANK = 'blank'

YARRRML_QUOTED = 'quoted'
YARRRML_NON_ASSERTED = 'quotedNonAsserted'

YARRRML_TARGETS = 'targets'
YARRRML_SERIALIZATION = 'serialization'
YARRRML_COMPRESSION = 'compression'

YARRRML_FUNCTION = 'function'

YARRRML_PARAMETER = 'parameter'

YARRRML_GATHER = 'gather'
YARRRML_GATHER_AS = 'gatherAs'
YARRRML_GATHER_AS_OPTIONS = ["alt","bag","seq","list"]
YARRRML_EMPTY = 'empty'
YARRRML_STRATEGY = 'strategy'

YARRRML_MAPPING_KEYS = [YARRRML_MAPPINGS, YARRRML_MAPPING]
YARRRML_SUBJECT_KEYS = [YARRRML_SUBJECTS]
YARRRML_POM_KEYS = [YARRRML_PREDICATEOBJECT]
YARRRML_GRAPH_KEYS = [YARRRML_GRAPHS]
YARRRML_PREDICATE_KEYS = [YARRRML_PREDICATES]
YARRRML_OBJECT_KEYS = [YARRRML_OBJECTS]
YARRRML_FUNCTION_KEYS = [YARRRML_FUNCTION]
YARRRML_PARAMETERS_KEYS = [YARRRML_PARAMETERS]
YARRRML_PARAMETER_KEYS = [YARRRML_PARAMETER]
YARRRML_VALUE_KEYS = [YARRRML_VALUE]
