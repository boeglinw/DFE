#!/bin/bash

# get location of this script
HERE="$(dirname $0)"

# echo DFE.py is at $HERE

# select current python
PYTHON=`which pythonw`
DFE=$HERE/DFE.py

# run the code
$PYTHON $DFE





