FROM nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y build-essential tree htop

WORKDIR /app

# Installing minconda into the JetsonNano Image
RUN wget --quiet -O anaconda3.sh https://repo.anaconda.com/miniconda/Anaconda3-2021.04-Linux-aarch64.sh &&\
    DEBIAN_FRONTEND=noninteractive sh anaconda3.sh -b -p /opt/anaconda3 &&\
    rm -f anaconda3.sh

# Add conda to path
ENV PATH="/opt/anaconda3/bin:${PATH}"

# Check conda version
RUN conda --version

# Udpate coda
RUN  conda update -n base conda

# Init conda shell
RUN conda init bash

# Copy IMM
COPY ./ /app/imm

RUN cd /app/imm && python -m pip install . --use-feature=in-tree-build

# Make sure we use the virtualenv:
ENV PATH=$PATH:"/app/venv/bin"

# # Pass parameters to imm script
ENTRYPOINT [ "imm" ]