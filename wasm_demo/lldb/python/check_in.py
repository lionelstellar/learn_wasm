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
    section_dir = os.path.join(wasm_home, project, "python/sections")
    mem_dir = os.path.join(wasm_home, project, "python/mem_output")
    
    section_list = os.listdir(section_dir)
    mem_list = os.listdir(mem_dir)
    
    for mem_elem in mem_list:
        mem_block = read_block(os.path.join(mem_dir, mem_elem))
        for sec_elem in section_list:
            sec_block = read_block(os.path.join(section_dir, sec_elem))
            if sec_block in mem_block:
                print(sec_elem, "in", mem_elem)
    

if __name__ == "__main__":
    main()