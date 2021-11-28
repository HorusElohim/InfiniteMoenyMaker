FROM nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y build-essential tree htop

WORKDIR /app

# Copy IMM
COPY ./ /app/imm

RUN cd /app/imm && python3.6 -m pip install .

# # Pass parameters to imm script
ENTRYPOINT [ "imm" ]