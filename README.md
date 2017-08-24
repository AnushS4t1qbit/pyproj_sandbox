# Overview
This project is designed to show how simple it is to get a unit testing framework
set up at the beginning of a python project.

By extension, we will also cover how to properly install a python project via pip, without having to manually fiddle with the PYTHONPATH env variable.

This guide is designed to give you the absolute basics to get started with TDD (test driven development)

There are other more advanced concepts which I have purposefully not included here. If you are comfortable with the material here, and want something more advanced, you're welcome to come find me, and I can point you in the right direction.


# Installation
run this command in the directory containing setup.py (which is where this README is located in):

`pip install .`

If you want to force a clean install, run this:

`pip install . -I`


# Running the Tests
This command will recursively find test files (any file that has 'test' in its name), and execute the tests inside

CAVEAT: Be sure that any folder containing test files has an empty __init__.py, otherwise this command won't find it

`python -m unittest discover`
