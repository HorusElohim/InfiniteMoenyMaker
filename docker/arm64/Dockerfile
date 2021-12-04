FROM nvcr.io/nvidia/l4t-pytorch:r32.6.1-pth1.9-py3

# Set working dir
WORKDIR /app

# Copy IMM
COPY ./ /app/imm

# Copy API yml config
Copy .api.yml /app

RUN cd /app/imm && python3.6 -m pip install .

# # Pass parameters to imm script
ENTRYPOINT [ "imm" ]