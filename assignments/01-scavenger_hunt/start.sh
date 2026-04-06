#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: bash start.sh <your PID>"
    exit 1
fi

PID=$(echo "$1" | tr '[:lower:]' '[:upper:]')

if ! echo "$PID" | grep -qE '^[A-Z][0-9]{8}$'; then
    echo "Error: PID should be a letter followed by 8 digits (e.g., A12345678)."
    exit 1
fi

echo ""
echo "Welcome, $PID."
echo ""

# Download and extract the filesystem if not already present
if [ ! -d "filesystem" ]; then
    echo "Downloading filesystem data..."
    wget -q https://f000.backblazeb2.com/file/jeldridge-data/017-filesystem/filesystem.tar.gz
    echo "Verifying download..."
    EXPECTED="03712a9c90de30ca2deae56500ae3fd16df84e50"
    ACTUAL=$(sha1sum filesystem.tar.gz | cut -d' ' -f1)
    if [ "$ACTUAL" != "$EXPECTED" ]; then
        echo "Error: download integrity check failed."
        rm -f filesystem.tar.gz
        exit 1
    fi
    echo "Extracting..."
    tar xzf filesystem.tar.gz
    rm filesystem.tar.gz
fi

DIRS=(
    "filesystem/home/mcallister"
    "filesystem/home/thornton"
    "filesystem/home/gupta"
    "filesystem/home/oconnell"
    "filesystem/home/nakamura"
    "filesystem/home/petrov"
    "filesystem/home/lindqvist"
    "filesystem/home/mbeki"
    "filesystem/home/carroll"
    "filesystem/home/fontaine"
    "filesystem/home/reeves"
    "filesystem/home/ashworth"
    "filesystem/home/delacroix"
    "filesystem/home/huang"
    "filesystem/home/bergmann"
)

HASH=$(echo -n "$PID" | md5sum | tr -d ' -')
INDEX=$(( 16#${HASH:0:8} % 15 ))
DIR="${DIRS[$INDEX]}"

printf "Accessing haunted file system"
sleep 0.03; printf "."
sleep 0.03; printf "."
sleep 0.03; printf "."
sleep 0.05; printf "."
sleep 0.05; printf "."
sleep 0.05; printf "."
sleep 1; printf "."
sleep 1; printf "."
sleep 1; printf "."
sleep 0.05; printf "."
sleep 0.05; printf "."
sleep 0.05; printf "."
sleep 0.01; printf "."
sleep 0.01; printf "."
sleep 0.01; printf "."
sleep 0.05; printf "."
sleep 0.05; printf "."
sleep 0.05; printf "."
sleep 0.5
echo " done."
echo ""
echo "PHANTOM's trail begins at:"
echo ""
echo "  $DIR/"
echo ""
echo "There is a file in that directory with your first clue."
echo "You'll know it when you see it."
sleep 4
echo -n "Look carefully"
sleep 0.1; printf "."
sleep 0.1; printf "."
sleep 0.1; printf "."
sleep 2
echo ""
