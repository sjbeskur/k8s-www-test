#!/bin/bash

pushd www
npm install
npm run build
dotnet publish --output ../target -r linux-x64 # linux-musl-x64 # use this one for alpine linux
popd

docker build -t www-test . -f Dockerfile.msft-dotnet
