#!/bin/bash

while [ $? == 0 ]
  do
    docker images -qf dangling=true | xargs docker rmi 2>&1 | awk '$1=="Error" {print$NF}' | xargs docker rm
  done
