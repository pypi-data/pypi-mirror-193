
<p align="center">
    <em>Define data in YAML format and load it into a relational database using SQLAlchemy✨</em>
</p>

<p align="center">
<a href="https://github.com/yezz123/sql-fixture/actions/workflows/test.yml" target="_blank">
    <img src="https://github.com/yezz123/sql-fixture/actions/workflows/test.yml/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/yezz123/sql-fixture">
    <img src="https://codecov.io/gh/yezz123/sql-fixture/branch/main/graph/badge.svg"/>
</a>
</p>

## Features

TODO

## Installation

You can add sql-fixture in a few easy steps. First of all, install the dependency:

```shell
$ pip install sql_fixture

---> 100%

Successfully installed sql_fixture
```

## Development 🚧

### Setup environment 📦

You should create a virtual environment and activate it:

```bash
python -m venv venv/
```

```bash
source venv/bin/activate
```

And then install the development dependencies:

```bash
# Install dependencies
pip install -e .[test,lint]
```

### Run tests 🌝

You can run all the tests with:

```bash
bash scripts/test.sh
```

> Note: You can also generate a coverage report with:

```bash
bash scripts/test_html.sh
```

### Format the code 🍂

Execute the following command to apply `pre-commit` formatting:

```bash
bash scripts/format.sh
```

Execute the following command to apply `mypy` type checking:

```bash
bash scripts/lint.sh
```

## License

This project is licensed under the terms of the MIT license.
