#!/usr/bin/env bash

function log() {
  echo -e $@
}

function check_cmd_exist() {
  if ! command -v $1 &>/dev/null; then
    echo "-1"
  else
    echo "0"
  fi
}

function check_dir_exist() {
  if [[ -d "$1" ]]; then
    echo "0"
  else
    echo "-1"
  fi
}

function check_python_pkg_exist() {
  pkg=$1
  version=$2
  result=$(python3.9 -m pip show $pkg)
  if [[ "$result" == *"$version"* ]]; then
    echo "0"
  else
    echo "-1"
  fi
}