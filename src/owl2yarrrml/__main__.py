import argparse
import sys
import yaml
import os
from .translate import translate
import owlready2

def parsing_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ontology", required=True, help="Input ontology file owl path file")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    args = parser.parse_args()
    if len(sys.argv) == 5:
        try:
            ontology = owlready2.get_ontology("file://" + os.path.abspath(str(args.ontology))).load()
            output_path = str(args.output)
            return ontology, output_path
        except ValueError:
            print("No input the correct arguments, run pip3 translate.py -h to see the help")
            sys.exit()
    else:
        print("No input the correct arguments, run pip3 translate.py -h to see the help)")
        sys.exit()


def write_results():
    dumped_yaml = str(yaml.dump(mapping, default_flow_style=None, sort_keys=False)).replace("'\"", '"').replace(
        "\"'", ' " ').replace('\'', '')
    with open(output_path, "w") as output_stream:
        output_stream.write(dumped_yaml)

if __name__ == "__main__":
    # Allow execution via: python -m owl2yarrrml -i ontology.owl -o mapping.yaml
    ontology, output_path = parsing_arguments()
    mapping = translate(ontology)
    write_results()