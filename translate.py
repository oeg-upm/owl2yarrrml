import argparse
import yaml
import copy
from owlready2 import *


def translate():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ontology", required=True, help="Input ontology file owl path file")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    args = parser.parse_args()
    if len(sys.argv) == 5:
        try:
            ontology = str(args.ontology)
            output_path = str(args.output)

        except ValueError:
            print("No input the correct arguments, run pip3 translate.py -h to see the help")
            sys.exit()
    else:
        print("No input the correct arguments, run pip3 translate.py -h to see the help)")
        sys.exit()

    # onto_path.append(os.path.abspath(ontology).replace(ontology, ""))
    onto = get_ontology("file://" + os.path.abspath(ontology)).load()

    template = init_yarrrml()

    construct_mapping(template, onto)

    write_output(template, output_path)


def init_yarrrml():
    template = yaml.load(open("template.yaml"), Loader=yaml.FullLoader)
    return template


def construct_mapping(template, onto):
    base_iri = onto.base_iri
    prefixes = generate_prefixes(template,onto)
    for c in list(onto.classes()):
        template['prefixes'][onto.name] = base_iri
        triplesmapTemplate = copy.deepcopy(template['mappings']['triplesmap0'])
        triplesmapTemplate['po'][0][1] = c.iri.replace(c.namespace.base_iri, prefixes[c.namespace.base_iri] + ":")
        del triplesmapTemplate['po'][1]
        class_name = c.iri.replace(c.namespace.base_iri, '')
        pos = 1
        superclasses = []
        get_superclasses(c, onto, superclasses)
        for d in list(onto.data_properties()):
            property_name = d.iri.replace('\'', '').replace(d.namespace.base_iri, prefixes[d.namespace.base_iri] + ":")
            for domains in d.domain:
                if domains == c or domains in superclasses:
                    for ranges in d.range:
                        datatype = get_data_type(ranges)
                        if datatype is not None:
                            triplesmapTemplate['po'].insert(pos, [property_name, '$()', datatype.replace('\'', '')])
                        else:
                            triplesmapTemplate['po'].insert(pos, [property_name, '$()'])
                        pos = pos + 1

        template['mappings']['triplesMap' + class_name.capitalize()] = triplesmapTemplate
    for c in list(onto.classes()):
        for triplesmap in dict(template['mappings']):
            if template['mappings'][triplesmap]['po'][0][1] == (c.iri.replace(c.namespace.base_iri, prefixes[c.namespace.base_iri] + ":")):
                join_template = template['mappings']['triplesmap0']['po'][1]
                generate_ref_object_maps(triplesmap, join_template, template, c, onto,prefixes)

    del template['mappings']['triplesmap0']


def generate_prefixes(template, onto):
    prefixes = {}
    for c in list(onto.classes()):
        template['prefixes'][c.namespace.name] = c.namespace.base_iri
        prefixes[c.namespace.base_iri] = c.namespace.name
    for dp in list(onto.data_properties()):
        template['prefixes'][dp.namespace.name] = dp.namespace.base_iri
        prefixes[dp.namespace.base_iri] = dp.namespace.name
    for do in list(onto.object_properties()):
        template['prefixes'][do.namespace.name] = do.namespace.base_iri
        prefixes[do.namespace.base_iri] = do.namespace.name
    return prefixes


def find_triplesmap(mapping, base_iri, range, onto):
    ref_triples_map = ""
    for triplesMap in dict.keys(mapping['mappings']):
        if mapping['mappings'][triplesMap]['po'][0][1] == (range.iri.replace(base_iri, onto.name)):
            ref_triples_map = triplesMap
    return ref_triples_map


def generate_ref_object_maps(triplesmap, join_template, template, c, onto, prefixes):
    for o in list(onto.object_properties()):
        for domain in o.domain:
            if domain == c:
                for range in o.range:
                    if type(range) is not owlready2.entity.ThingClass:
                        for r in range.Classes:
                            if r is owlready2.entity.ThingClass:
                                create_join_condition(template, onto, join_template, o, triplesmap, r, prefixes)
                    else:
                        if range.iri != "http://www.w3.org/2002/07/owl#Thing":
                            create_join_condition(template, onto, join_template, o, triplesmap, range, prefixes)


def create_join_condition(template, onto, join_template, o, triplesmap, range,prefixes):
    triples_map_parent = find_triplesmap(template, onto.base_iri, range, onto)
    join = copy.deepcopy(join_template)
    join['p'] = o.iri.replace(o.namespace.base_iri, prefixes[o.namespace.base_iri] + ":")
    join['o'][0]['mapping'] = triples_map_parent
    template['mappings'][triplesmap]['po'].append(join)


def get_superclasses(c, onto, superclasses):
    for superclass in c.is_a:
        if superclass in list(onto.classes()):
            superclasses.append(superclass)
            get_superclasses(superclass, onto, superclasses)

def write_output(mapping, output):
    dumped_yaml = str(yaml.dump(mapping, default_flow_style=None, sort_keys=False)).replace("'\"", '"').replace("\"'",
                                                                                                                ' " ').replace(
        '\'', '')
    with open(output, "w") as output_stream:
        output_stream.write(dumped_yaml)


def get_data_type(type):
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
