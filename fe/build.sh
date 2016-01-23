#!/bin/sh

set -ex

cd $(dirname $0)
ember build -e development -o dev
ember build -e production -o prod
docker build -t benstraub/fe:latest .
