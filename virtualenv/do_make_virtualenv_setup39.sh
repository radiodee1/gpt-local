#!/usr/bin/env bash

# sudo may not be needed here
pip3 install --user virtualenv
pip3 install --user virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
mkdir -p $WORKON_HOME
export VIRTUALENVWRAPPER_PYTHON=$(which python3.9)
source $(which virtualenvwrapper.sh)

mkvirtualenv gptj39 --python $(which python3.9)

## type `deactivate` to exit ##
