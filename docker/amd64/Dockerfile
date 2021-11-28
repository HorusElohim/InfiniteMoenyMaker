FROM nvcr.io/nvidia/pytorch:21.11-py3

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y build-essential tree htop

WORKDIR /app

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