#!/bin/bash

VENV_PATH=".venv"

if [ ! -d $VENV_PATH ];
then
  python3 -m venv .venv
  . .venv/bin/activate
  pip3 install --upgrade pip
  pip3 install -r requirements.txt
else
  . .venv/bin/activate
fi

pytest
python3 main.py
