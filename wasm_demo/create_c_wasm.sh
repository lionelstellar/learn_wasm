#!/bin/bash
if [ $# != 1 ]; then
    echo "invalid args, please input the project name that you wanna create"
    exit 1
fi
project=$1
echo "creating project: "$project


cp -r skeleton $project
cd $project
sed -i "s/{}/${project}/g" Makefile
sed -i "s/{}/${project}/g" run.sh
