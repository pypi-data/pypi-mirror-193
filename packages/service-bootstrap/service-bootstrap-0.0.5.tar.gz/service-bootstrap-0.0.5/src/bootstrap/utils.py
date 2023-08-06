import os

import yaml
from string import Template


def load_yaml(file):
    with open(file, 'r') as f:
        content = f.read()
        template = Template(content)
        final_content = template.substitute(os.environ)
        return yaml.full_load(final_content)