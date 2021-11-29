FROM nvcr.io/nvidia/pytorch:21.11-py3

# Set working dir
WORKDIR /app

# Copy IMM
COPY ./ /app/imm

# Install IMM
RUN cd /app/imm && python3.8 -m pip install . --use-feature=in-tree-build

# # Pass parameters to imm script
ENTRYPOINT [ "imm" ]
