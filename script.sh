#!/bin/bash

echo 'hello world' > ./hello.txt
geth account import ./hello.txt
rm ./hello.txt

