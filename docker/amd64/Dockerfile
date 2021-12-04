FROM nvcr.io/nvidia/pytorch:21.11-py3

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y build-essential tree htop

WORKDIR /app

# Copy IMM
COPY ./ /app/imm

# Copy API yml config
Copy .api.yml /app

RUN cd /app/imm && python3.8 -m pip install . --use-feature=in-tree-build

# # Pass parameters to imm script
ENTRYPOINT [ "imm" ]