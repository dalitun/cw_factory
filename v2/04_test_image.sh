#!/usr/bin/env bash

python --version

pip3 --version

IMG_ID=$(cat outputs-for-test/id.txt)

echo ${IMG_ID}

