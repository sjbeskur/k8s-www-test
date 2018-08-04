#!/bin/bash

aws ecr get-login --no-include-email | bash

aws ecr describe-repositories

docker tag www-test:v2 <aws-repo-url>/<repo-name>:www-test

docker push <aws-repo-url>/<repo-name>:www-test

