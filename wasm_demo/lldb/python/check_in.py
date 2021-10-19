#!/usr/bin/env python3
import configparser
import os
config = configparser.ConfigParser()
config.read('config')
wasm_home = config['DEFAULT']['wasm_demo']
project = config['DEFAULT']['project']
wasm_bin = config['DEFAULT']['wasm_bin']

def read_block(file):
    with open(file, 'rb') as f:
        content = f.read()
    return content

def check_in(src_file, dest_file):
    src = read_block(src_file)
    dest = read_block(dest_file)
    return src in dest

def main():
    
    
    dest_file = os.path.join(wasm_home, project, wasm_bin)
    src_file = os.path.join(wasm_home, project, "python/sections/Elem")

    print(check_in(src_file, dest_file))
    

if __name__ == "__main__":
    main()