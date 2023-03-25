#!/usr/bin/env bash

set -x
set -e

apt-get update && apt-get install git -y
pip3 install "git+https://github.com/openai/whisper.git" 
apt-get install -y ffmpeg
