#!/bin/bash

if command -V python python3
    then
        #cleanup si déjà installé
        if ls -a | grep ".venv"
        then 
            rm -rf .venv
        fi
        #creation venv + install requirements
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        echo "Server done"
        exit 0
    else
        echo "ERROR: python is not installed on this machine"
        exit 1
    fi
