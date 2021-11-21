#!/usr/bin/env bash

# Set Paths
imm_path=$(git rev-parse --show-toplevel)
scripts=$imm_path/scripts

# Source lib
source $scripts/lib.sh

python3.9 -m pip torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio==0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html