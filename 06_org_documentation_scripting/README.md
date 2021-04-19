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

Create a file called `dev.in` with the contents:

```
mkdocs
mkdocs-material
```

OR:

```bash
pip install mkdocs mkdocs-material
```

Now run:

```
mkdocs new docs
cd docs
```

Some extra mkdocs plugins:

```
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

Inside your `docs/docs` folder, you can create an `examples.md` and `models.md` files
and they will show up in your mkdocs site!

Production:

```bash
mkdocs build
```

That's it! This will generate a `site/` folder.

## netlify

[Drop](https://app.netlify.com/drop)

Copy the `site/` folder there.

However...

```bash
# this command may be interesting to run inside a GitHub repo
mkdocs gh-deploy --help
```

This will generate a `gh-pages` branch, GitHub will automatically generate
a static site with the contents there. You can use the generated URL to edit
your GitHub repo.

## pip-tools

https://github.com/jazzband/pip-tools

## environment variables

[12factor](https://12factor.net/) app

python-dotenv [pip](https://pypi.org/project/python-dotenv/) / [conda](https://anaconda.org/conda-forge/python-dotenv)
