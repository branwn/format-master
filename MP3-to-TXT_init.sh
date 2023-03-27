#!/usr/bin/env bash

set -x
# set -e

apt-get update && apt-get install git -y
apt-get install -y ffmpeg

pip3 install "git+https://github.com/openai/whisper.git" --no-cache-dir
