#!/bin/bash
target=`ls $(pwd) | grep wasm`
echo $target
# exit 0
lldb -- wasmtime -g $target
