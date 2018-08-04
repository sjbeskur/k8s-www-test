#!/bin/bash
mkdir target/

docker build -t www-test-build .
docker run -it --rm  -v $PWD/target:/target www-test-build

docker build -t www-test . -f build/Dockerfile.msft-dotnet