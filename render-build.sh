#!/usr/bin/env bash
set -o errexit  # stop on error

# Install the libheif development library
apt-get update
apt-get install -y libheif-dev

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
