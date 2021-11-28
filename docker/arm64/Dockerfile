FROM nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y build-essential tree htop

WORKDIR /app

# Fix ImportError: libcurand.so.10: cannot open shared object file: No such file or directory
RUN apt-get --yes install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
RUN git clone --branch v0.9.0 https://github.com/pytorch/vision torchvision
RUN export BUILD_VERSION=0.9.0
RUN pip3 install -e torchvision

# Copy IMM
COPY ./ /app/imm

RUN cd /app/imm && python3.6 -m pip install .

# # Pass parameters to imm script
ENTRYPOINT [ "imm" ]