#!/bin/bash -e
clear; echo "> sudo apt update;"; sudo apt update; echo; apt list --upgradable -a; echo; echo "> sudo apt install python3;"; sudo apt install python3; echo; echo "> sudo apt autoremove;"; sudo apt autoremove; echo;

if [ -f "./requirements.txt" ]; then
    python3 -m pip install -r requirements.txt; echo;
fi

if [ -f "./constants.py" ]; then
    python3 -m isort ./constants.py; python3 -m black ./constants.py; echo; python3 -m pylint ./constants.py; echo;
fi

if [ -f "./__main__.py" ]; then
    python3 -m isort ./__main__.py; python3 -m black ./__main__.py; echo; python3 -m pylint ./__main__.py; echo; pyinstaller ./__main__.py -n "Predictor" --add-data="./assets/*:./assets/" --add-data="./venv/lib/python3.*/site-packages/pyfiglet/fonts/*:./pyfiglet/fonts/" --hidden-import="PIL._tkinter_finder" --hidden-import="sklearn.metrics._pairwise_distances_reduction._datasets_pair" --hidden-import="sklearn.metrics._pairwise_distances_reduction._middle_term_computer" -Fy; echo;
fi

if [ -d "./build" ]; then
    rm -rv ./build; echo;
fi

if [ -f "./Predictor.spec" ]; then
    rm -fv ./Predictor.spec; echo;
fi

if [ -f "./dist/Predictor" ]; then
    ./dist/Predictor;
fi

exit;
