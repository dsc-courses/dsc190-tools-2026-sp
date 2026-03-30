#!/usr/bin/env bash
docker run -it --rm \
    -v dsc190-tools-starter-home:/home/student \
    -h dsc190-tools-starter \
    ghcr.io/dsc-courses/dsc190-tools-starter
