#!/bin/bash

PYTHON=$(which python3)
if [ -z "$PYTHON" ]; then
    echo "No python3 found, make sure you have python3 installed"
    exit 1
fi

$PYTHON -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt