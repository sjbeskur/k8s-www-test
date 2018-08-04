#!/usr/bin/env python
import re
import subprocess
import json
import sys

def execute_cmd(cmd):
  proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  comm = proc.communicate()

  if comm[1] != '':
    print(comm[1].rstrip('\n'))
    exit(-1)

  return comm[0]

def publish_to_aws():
  ecr_response = execute_cmd('aws ecr describe-repositories').rstrip('\n')
  ecr_json = json.loads(ecr_response)

  print  "\nAWS Reposdiscovered for zone: "

  repos = []
  for uri in ecr_json["repositories"]:
    repos.append( uri["repositoryUri"] )

  for idx , r in enumerate(repos,0):
    print str(idx) + ") -> " + r

  print  "\nSelect a repo to publish to: "
  selection = sys.stdin.readline()
  pos = int(selection)

  tag_cmd = "docker tag www-test:{0} {1}:{2}"

  print  "\nEnter a docker tag: "
  tag = sys.stdin.readline()

  print  "\nTagging image with: " + tag_cmd.format(tag, repos[pos], tag)
  execute_cmd(tag_cmd.format(tag, repos[pos],tag))

  push_cmd = "docker push {0}:{1}"
  print  "\nPublishing image to: " + repos[pos] + "with tag: "  + tag
  execute_cmd(tag_cmd.format(tag, repos[pos]))


if __name__ == "__main__":
  publish_to_aws()





