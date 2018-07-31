#!/bin/bash

docker tag www-test:latest <repo-url>/<repo name>:www-test

docker push <repo-url>/<repo name>:www-test

