#!/bin/bash
set -e

VERSION_FILE="./version"
VERSION=$(cat $VERSION_FILE)

PROJECT="web_rbl"

build() {
    echo $new_version
    echo "Current Version: ${VERSION}"
    
    new_version=$VERSION

    if [ -z $new_version ]; then
        echo "Input New Version:"
        read new_version
    fi

    echo 'Container building..'
    docker build -t $PROJECT:$new_version .
    echo "$new_version" > $VERSION_FILE

    if [ -z $update_latest ]; then
        echo "Update latest? [y/N]"
        read update_latest
    fi

    if [ "$update_latest" == "y" ] || [ "$update_latest" == "Y" ];then
        docker tag $PROJECT:$new_version $PROJECT:latest
    fi
}

upload(){
    docker push  $1
}

help(){
    echo "Functions:"
    echo "build()"
    echo "* new_version"
    echo "* update_latest"
}

build
