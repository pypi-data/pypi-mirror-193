# dbt-models-explorer

DBT models explorer with output generator to check, analyze and document

## Features

- Read DBT Models Yml to objectcts and make relationships Analysis
- Rich Console Output
- Export to CSV Format

## Run Locally

Clone the project

```bash
  git clone https://github.com/catapimbas/dbt-models-explorer.git
```

Go to the project directory

```bash
  cd dbt-models-explorer
```

Install dependencies

```bash
  poetry install
```

Run

```bash
  poetry run dbt-models-explorer [<path-to-yml-models> <options>]
```

## Usage/Examples

### Rich outupt, default

```bash
poetry run dbt-models-explorer <path-to-yml-models>
```

### CSV outupt

```bash
poetry run dbt-models-explorer <path-to-yml-models> --format csv <filename>
```
