## Python classes

Abstractions.

**Project idea**

Create an abstraction around the database.

Create a class with a few methods to add or return data.

## black, flake8...

Installing dependencies.

Why are they useful?

## cookiecutter

It's important to have a project template. Having standards lets you and your team work together.

## mkdocs

To start you only need this:

```bash
pip install mkdocs mkdocs-material
mkdocs new docs
cd docs
```

Some extras:

```
# in your requirements.txt
markdown-include
mkdocs
mkdocs-markdownextradata-plugin
mkdocs-material
mkdocstrings
pymdown-extensions
```

Edit the `docs.yaml` file.

```yaml
theme:
   name: material
   language: en
plugins:
  - search
nav:
  - Introduction: 'index.md'
  - Examples: 'examples.md'
  - Models: 'models.md'
```

Development:

```bash
mkdocs serve
```

Production:

```bash
mkdocs build
```

That's it!

## netlify

[Drop](https://app.netlify.com/drop)

However...

```bash
# this command may be interesting to run inside a GitHub repo
mkdocs gh-deploy --help
```

## pip-tools

https://github.com/jazzband/pip-tools

## environment variables

[12factor](https://12factor.net/) app

python-dotenv [pip](https://pypi.org/project/python-dotenv/) / [conda](https://anaconda.org/conda-forge/python-dotenv)