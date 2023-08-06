#!/usr/bin/bash
source $TOOLING_DIR/startwork/scripts/try_node.sh
source $TOOLING_DIR/startwork/scripts/try_python.sh

cd "$1"

if [[ -f "package.json" ]] #:/
    then try_node
    else echo "Not on a node project"
fi

if [[ -f "requirements.txt" ]] #:/
    then try_python "$2"
    else echo "Not on a python project"
fi
