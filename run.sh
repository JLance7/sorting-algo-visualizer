#!/bin/bash

VENV_PATH=".venv"

if [ ! -d $VENV_PATH ];
then
  python3 -m venv .venv
  pip3 install --upgrade pip
  pip3 install -r requirements.txt
fi

python3 main.py
