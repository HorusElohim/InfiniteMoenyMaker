#!/usr/bin/env bash

# Set Paths
imm_path=$(git rev-parse --show-toplevel)
scripts=$imm_path/scripts

# Source lib
source $scripts/lib.sh

log "Creating a new python3.9 environment"
cd $imm_path
python3.9 -m venv venv
cd -
