#!/bin/bash
mkdir target/

docker build -t www-test-build .
docker run -it --rm  -v $PWD:/target www-test-build /bin/sh -c "cp www.tar.gz /apps"

docker build -t www-test . -f Dockerfile.msft-dotnet