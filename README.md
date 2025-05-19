# Transforming your ontology into YARRRML mappings
This script generates a YARRRML template from the input ontology. The transformations made are:

| Ontology        |                                                                                                           Mapping                                                                                                           |
|-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| 
| Class           |                                                                                  TriplesMap + Simple PredicateObjectMap (rdf:type, class)                                                                                   | 
| Data Property   |                                                        Simple PredicateObjectMap in the TriplesMap corresponding to the class defined in the domain of the property                                                         | 
| Object Property | Join PredicateObjectMap in the TriplesMap corresponding to the class defined in the domain of the property and where the parentTriplesMap is the TriplesMap corresponding to the class defined in the range of the property | 

## How to execute it

### Execution from CLI
The input ontology can be serialized in NTRIPLES, RDF/XML or Turtle
```bash
python3 -m pip install owl2yarrrml
python3 -m owl2yarrrml -i paht/ontology.xml -o ouput_path/mapping.yml
```

### Execution as a library
The ontology has to be provided in RDF/XML.
```python
import owl2yarrrml
import owlready2
ontology=owlready2.get_ontology("file://path/to/my/ontology.xml").load()
yarrrml_content = owl2yarrrml.translate(ontology)

```

## Authors
CiTIUS - Universidade de Santiago de Compostela (2023-now) and Ontology Engineering Group - Universidad Politécnica de Madrid (2020-2023):
- [David Chaves-Fraga](mailto:david.chaves@usc.es)