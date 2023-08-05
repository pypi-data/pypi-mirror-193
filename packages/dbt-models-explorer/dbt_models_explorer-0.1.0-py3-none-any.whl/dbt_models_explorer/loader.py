import os
from dataclasses import dataclass
from typing import List

import yaml


@dataclass
class Column:
    name: str
    description: str
    props: List


@dataclass
class Table:
    name: str
    description: str
    columns: List[Column]


RUNTIME_ERRORS = []


def load_from_yaml(dir_path: str):
    for dirpath, _, filenames in os.walk(dir_path):
        for filename in filter(lambda name: name.endswith('.yml'), filenames):
            with open(os.path.join(dirpath, filename)) as f:
                try:
                    model_dict = yaml.safe_load(f)
                except yaml.YAMLError as e:
                    RUNTIME_ERRORS.append(e)
                    break
            for model in model_dict['models']:
                yield load_table(model)


def load_table(model_dict: dict):
    return Table(
        model_dict['name'],
        model_dict.get('description'),
        [Column(
            column['name'],
            column.get('description'),
            column.get('tests'))
         for column in model_dict['columns']])
