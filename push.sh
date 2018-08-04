#!/bin/bash

aws ecr get-login --no-include-email | bash
aws ecr describe-repositories

docker tag www-test:v2 855281110945.dkr.ecr.us-east-2.amazonaws.com/nmsrepo:www-test

docker push 855281110945.dkr.ecr.us-east-2.amazonaws.com/nmsrepo:www-test

