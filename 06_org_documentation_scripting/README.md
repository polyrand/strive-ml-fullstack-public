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

# Exercises for the afternoon

## script

1. turn the 1.train.ipython notebook into a python script

The script can have the following options:

```
--download-data
--train --epochs INT (it should have a default)
--optimizer STRING
--load-weights STRING
    
# extra work:
# load the data URL from an environment variable (using a .env file and the python-dotenv package)
```

Then you can run the script like:

```
python3 train.py --download-data --train --epochs 3 --optimizer sgd --load-weights my_weigths.pth
```

**Don't worry if you can't implement all the options**

2. keep writing the documentation
    * `data.md`: explain what your data is. Is it balanced? What's the source?
    * `organization.md`: explain how you would organize the project.
    * `running.md`: explain how to run your script.
    
3. Work on the database abstraction we mentioned.
    * decide what columns your `users` database will have.
    * implement the 2 missing methods
    * make sure they work!

## environment variables

python-dotenv [pip](https://pypi.org/project/python-dotenv/) / [conda](https://anaconda.org/conda-forge/python-dotenv)

**Interesting read**

[12factor](https://12factor.net/) app
