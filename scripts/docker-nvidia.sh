#!/usr/bin/env bash

# Set Paths
imm_path=$(git rev-parse --show-toplevel)
scripts=$imm_path/scripts

# Source lib
source $scripts/lib.sh

log "Installing docker-nvidia"

if [[ "$(check_cmd_exist docker)" != "0" ]]; then
  log "docker is not installed "
  sudo apt install curl -y
  curl https://get.docker.com | sh  && sudo systemctl --now enable docker
else
  log "docker already installed "
fi



log "Setting up NVIDIA Container Toolkit"
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
   && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
   && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update

sudo apt-get install -y nvidia-docker2

sudo systemctl restart docker

sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi