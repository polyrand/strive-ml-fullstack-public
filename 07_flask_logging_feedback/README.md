# Models running in a web application

## Python packages and dependencies

[pip-tools](https://pypi.org/project/pip-tools/)

```bash
pip-compile -v --output-file requirements/main.txt requirements/main.in
pip-compile -v --output-file requirements/dev.txt requirements/dev.in  # --allow-unsafe
```

```bash
pip-compile -v --upgrade --output-file requirements/main.txt requirements/main.in
pip-compile -v --upgrade --output-file requirements/dev.txt requirements/dev.in
```

## Code formatting, linting, style and best practices

[black](https://github.com/psf/black#installation-and-usage)

[flake8](https://flake8.pycqa.org/en/latest/)

## SQL Review

## HTTP basics

## The cloud

## URLs

## Environment

Variables / configuration

## Logging

Some things that may be useful to log:

* Input image statistics (color distribution, size (pixes, MB...)
* Results!!  (VERY IMPORTANT)

## Performance

Possible bottlenecks:

* Network
* ML model

## Feedback

* Implement a button so that users can give feedback to the results. We also need to keep track of the results (generate an ID).
