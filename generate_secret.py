#!/usr/bin/env python

import re
import subprocess

def execute_cmd(cmd):
  proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  comm = proc.communicate()

  if comm[1] != '':
    print(comm[1].rstrip('\n'))
    exit(-1)

  return comm[0]

def generate_secret_key():
  login_cmd = execute_cmd('aws ecr get-login --no-include-email').rstrip('\n')
  creds = re.sub(r"(-e none\ |docker login\ |-u\ |-p\ )", '', login_cmd).split(' ')
  generate_secret_cmd = "kubectl create secret docker-registry {0} --docker-username={1} --docker-password={2} --docker-server={3} --docker-email=YOUR_EMAIL_ADDRESS"
  execute_cmd(generate_secret_cmd.format('YOUR_SECRET_KEY_NAME', creds[0], creds[1], creds[2].replace('https://', '')))

if __name__ == "__main__":
  generate_secret_key()

# keeping cred fresh 
# https://medium.com/@xynova/keeping-aws-registry-pull-credentials-fresh-in-kubernetes-2d123f581ca6