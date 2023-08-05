import csv
from typing import Iterable

from rich.console import Console
from rich.table import Table as RichTable

from .loader import RUNTIME_ERRORS, Table

console = Console()


def print_relationships(tables: Iterable[Table]):
    rich_table = RichTable(title=('Relationships'), show_lines=True)
    rich_table.add_column('Table name', style="bold green")
    rich_table.add_column('Column', style="bold green")
    rich_table.add_column('Ref table', style="bold blue")
    rich_table.add_column('Field', style="bold blue")
    for table in tables:
        for column in table.columns:
            if column.props:
                for prop in column.props:
                    if isinstance(prop, dict):
                        for attr in prop:
                            if 'relationships' in attr:
                                rel = prop['relationships']
                                rich_table.add_row(
                                    table.name, column.name, rel['to'], rel['field'])
    console.print(rich_table)


def write_csv(tables: Iterable[Table], filename: str = 'relationships.csv'):
    with open(filename, 'w') as fp:
        writer = csv.writer(fp, delimiter=',')
        writer.writerow(['Table name', 'Column', 'Ref table', 'Field', ])
        for table in tables:
            for column in table.columns:
                if column.props:
                    for prop in column.props:
                        if isinstance(prop, dict):
                            for attr in prop:
                                if 'relationships' in attr:
                                    rel = prop['relationships']
                                    writer.writerow([table.name, column.name,
                                                     rel['to'], rel['field']])
