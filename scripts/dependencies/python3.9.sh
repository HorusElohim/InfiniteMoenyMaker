#!/usr/bin/env bash

# Set Paths
imm_path=$(git rev-parse --show-toplevel)
scripts=$imm_path/scripts

# Source lib
source $scripts/lib.sh

log "Installing python3.9"
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev \
  libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev -y

pushd /tmp
  wget https://www.python.org/ftp/python/3.9.9/Python-3.9.9.tgz
  tar -xf Python-3.9.9.tgz
  cd Python-3.9.9
  ./configure --enable-optimizations
  make -j $(($(nproc --all) - 2))
  sudo make altinstall
popd

python3.9 --version
python3.9 -m pip install --upgrade pip