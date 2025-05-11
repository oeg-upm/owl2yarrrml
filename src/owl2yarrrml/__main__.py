from . import translate
import argparse
import sys
import yaml
import os
import tempfile
from rdflib import Graph
from owlready2 import World


# Inline load_ontology logic
def load_ontology(path_or_url: str):
    """
    Load ontology from a local file path or URL.
    Supports Turtle by converting via rdflib, otherwise uses Owlready2 directly.
    """
    world = World()
    ext = path_or_url.split('.')[-1].lower()

    if ext in ("ttl", "turtle"):
        # Parse Turtle to RDF/XML using rdflib
        g = Graph()
        g.parse(path_or_url, format="turtle")
        with tempfile.NamedTemporaryFile(suffix=".owl", delete=False) as tmp:
            tmp_path = tmp.name
            g.serialize(destination=tmp_path, format="xml")
        onto = world.get_ontology(f"file://{tmp_path}").load()
    else:
        # Assume RDF/XML, OWL/XML, N-Triples, etc.
        # Prepend file:// for local paths if needed
        if not path_or_url.startswith(("http://", "https://", "file://")):
            path_or_url = "file://" + os.path.abspath(path_or_url)
        onto = world.get_ontology(path_or_url).load()
    return onto

def parsing_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ontology", required=True, help="Input ontology file owl path file")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    args = parser.parse_args()
    if len(sys.argv) == 5:
        try:
            ontology = load_ontology(str(args.ontology))
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
    ontology, output_path = parsing_arguments()
    mapping = translate(ontology)
    write_results()