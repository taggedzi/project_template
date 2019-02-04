# Project Template #

This project is simply my attempt to make some sort of standards (PEP) compliant boilerplate package template for a 
generic Python project.  I have pulled from multiple sources to generate this compilation.

What is included in this project:

* Basic support for Python2 and Python3.  
* Basic setup.py template with descriptions
* PyTest (pytest.ini)
* Tox (tox.ini)
* Git (.gitignore)

What is NOT included in this project:

* Pre-existing Project folder
* Integration for a CI testing framework or environment such as CircleCI/Jenkins/Travis. (All wonderful services)

I have attempted to be agnostic to platforms and vendors, and yet include the best in class tools 
(or best practice tools) as I understand them.

## How to Use ##

1. When you download this project you will want to add a folder to the `./src` directory that will contain your new
project. Do not forget your `./src/your_project/__init__.py` file!
1. You will want to modify your `./setup.py` to reflect your project. Detailed instructions included.
1. You will want to add your dependencies to `./requirements.txt` and `./requirements_dev.txt`
1. You will want to modify `./tox.ini` to include any test parameters you wish
1. **IF you want** to use `Sphinx` for documentation run the quickstart OR configure your Sphinx make scripts. (See Sphinx documentation.) IF you don't want to you use it you can remove references to it from `./requirements_dev.txt` and `./setup.py`

