#!/bin/bash

pushd www
npm install
npm run build
dotnet publish --output ../target -r linux-x64
popd

docker build -t www-test . -f Dockerfile_publish
