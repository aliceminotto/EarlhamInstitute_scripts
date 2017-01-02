#!bin/bash

STATUS=$1

echo "${STATUS}"

jobs-list | awk -v var="${STATUS}" '{if ($2 == var) print $1}' | xargs -L1 jobs-delete
