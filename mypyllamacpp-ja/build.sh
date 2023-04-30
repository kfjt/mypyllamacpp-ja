#!/bin/bash
SCRIPT_DIR=$(cd $(dirname $0) ; pwd)/
pushd $SCRIPT_DIR
docker build -t mypyllamacpp-ja:latest .
popd
