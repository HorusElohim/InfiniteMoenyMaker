#! /bin/bash

echo -e "[IMM] Docker build started"
echo -e "[IMM] Detection architecture..."
architecture=$(dpkg --print-architecture)

if [[ $architecture == "amd64" ]]; then
  echo -e "[IMM](amd64)"
  dockerfile=docker/amd64/Dockerfile
fi

if [[ $architecture == "arm64" ]]; then
  echo -e "[IMM](arm64)"
  dockerfile=docker/arm64/Dockerfile
fi

echo -e "[IMM] Dockerfile used: $dockerfile"
docker build -t imm -f $dockerfile .
