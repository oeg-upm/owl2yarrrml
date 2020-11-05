import argparse
import sys
import yaml
import copy
import datetime
from owlready2 import *


def translate():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ontology", required=True, help="Input ontology file owl path file")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    args = parser.parse_args()
    if len(sys.argv) == 5:
        try:
            ontology = os.path.basename(args.ontology)
            output_path = str(args.output)

        except ValueError:
            print("No input the correct arguments, run pip3 translate.py -h to see the help")
            sys.exit()
    else:
        print("No input the correct arguments, run pip3 translate.py -h to see the help)")
        sys.exit()

    onto_path.append(os.path.abspath(ontology).replace(ontology, ""))
    onto = get_ontology(ontology).load()

    template = inityarrrml()

    constructMapping(template, onto)

    writeOutput(template, output_path)


def inityarrrml():
    template = yaml.load(open("template.yaml"), Loader=yaml.FullLoader)
    return template


def constructMapping(template, onto):

    base_iri = onto.base_iri
    for c in list(onto.classes()):
        template['prefixes']['ns'] = base_iri
        triplesmapTemplate = copy.deepcopy(template['mappings']['triplesmap0'])
        triplesmapTemplate['po'][0][1] = c.iri.replace(base_iri, 'ns:')
        del triplesmapTemplate['po'][1]
        class_name = c.iri.replace(base_iri, '')
        pos = 1
        for d in list(onto.data_properties()):
            property_name = d.iri.replace('\'', '').replace(base_iri, 'ns:')
            for domains in d.domain:
                if domains == c:
                    for ranges in d.range:
                        datatype = dataType(ranges)
                        if datatype is not None:
                            triplesmapTemplate['po'].insert(pos, [property_name, '$()', datatype.replace('\'', '')])
                        else:
                            triplesmapTemplate['po'].insert(pos, [property_name, '$()'])
                        pos = pos + 1

        template['mappings']['triplesMap' + class_name.capitalize()] = triplesmapTemplate

    for c in list(onto.classes()):
        for triplesmap in dict(template['mappings']):
            if template['mappings'][triplesmap]['po'][0][1] == (c.iri.replace(base_iri, 'ns:')):
                join_template = template['mappings']['triplesmap0']['po'][1]
                generate_ref_object_maps(triplesmap, join_template, template, c, onto)

    del template['mappings']['triplesmap0']



def findTriplesMap(mapping, base_iri, range):
    ref_triples_map = ""
    for triplesMap in dict.keys(mapping['mappings']):
        if mapping['mappings'][triplesMap]['po'][0][1] == (range.iri.replace(base_iri, 'ns:')):
            ref_triples_map = triplesMap
    return ref_triples_map

def generate_ref_object_maps(triplesmap, join_template, template, c, onto):

    for o in list(onto.object_properties()):
        for domain in o.domain:
            if domain == c:
                for range in o.range:
                    triples_map_parent = findTriplesMap(template, onto.base_iri, range)
                    join_template['p'] = o.iri.replace(onto.base_iri, 'ns:')
                    join_template['o'][0]['mapping']=triples_map_parent
                    template['mappings'][triplesmap]['po'].append(join_template)



def writeOutput(mapping, output):
    dumped_yaml = str(yaml.dump(mapping, default_flow_style=None, sort_keys=False)).replace("'\"", '"').replace("\"'", ' " ').replace('\'', '')
    with open(output, "w") as output_stream:
       output_stream.write(dumped_yaml)

def dataType(type):

    if type == float:
        return "xsd:float"
    elif type == int:
        return "xsd:integer"
    elif type == bool:
        return "xsd:boolean"
    elif type == datetime.date:
        return "xsd:date"
    elif type == datetime.time:
        return "xsd:time"
    elif type == datetime.datetime:
        return "xsd:dateTime"
    else:
        return None




if __name__ == "__main__":
    translate()
