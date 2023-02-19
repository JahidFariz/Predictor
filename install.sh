#!/bin/bash -e
clear; echo "> sudo apt update;"; sudo apt update; echo; apt list --upgradable -a; echo; echo "> sudo apt install python3;"; sudo apt install python3; echo; echo "> sudo apt autoremove;"; sudo apt autoremove; echo;

if [ -f "./requirements.txt" ]; then
    python3 -m pip install -r requirements.txt; echo;
fi

if [ -f "./__main__.py" ]; then
    python3 -m isort ./__main__.py; black ./__main__.py; echo; pyinstaller ./__main__.py -n "Predictor" --icon="./predictive-chart.png" --add-data="./predictive-chart.png:./" --add-data="./venv/lib/python3.*/site-packages/pyfiglet/fonts/*:./pyfiglet/fonts/" -Fy; echo;
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