#!/usr/bin/env bash

# Set Paths
imm_path=$(git rev-parse --show-toplevel)
scripts=$imm_path/scripts
dependencies=$scripts/dependencies

# Source lib
source $scripts/lib.sh

# Ready to go ;)
log "Installation IMM has started ..."

log "Checking existence python3.9"
if [[ "$(check_cmd_exist python3.9)" != "0" ]]; then
  log "python3.9 is not installed "
  $dependencies/python3.9.sh
else
  log "python3.9 already installed "
fi

log "Checking existence python environment"
if [[ "$(check_dir_exist $imm_path/venv)" != "0" ]]; then
  log "python env is not created yet "
  $dependencies/py_env.sh
else
  log "python env is already created"
fi

log "Checking existence torch"
if [[ "$(check_python_pkg_exist torch "1.10.0+cu113")" != "0" ]]; then
  log "torch is not installed"
  $dependencies/torch.sh
else
  log "torch is already installed"
fi