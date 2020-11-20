# Transforming your ontology to YARRRML mappings
This script generates a YARRRML template from the input ontology. The transformations made are:

| Ontology        | Mapping           
| ------------- |:-------------:| 
| Class     | TriplesMap + Simple PredicateObjectMap (rdf:type, class) | 
| Data Property     | Simple PredicateObjectMap in the TriplesMap corresponding to the class defined in the domain of the property      | 
| Object Property | Join PredicateObjectMap in the TriplesMap corresponding to the class defined in the domain of the property and where the parentTriplesMap is the TriplesMap corresponding to the class defined in the range of the property | 

## How to execute it
In order to avoid problems, we recommend that the input ontology follows RDF/XML syntax

```python
python3 -m pip install -r requirements.txt
python3 translate.py -i ontology.xml -o mapping.yml
```
