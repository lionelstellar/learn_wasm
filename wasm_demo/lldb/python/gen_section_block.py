#!/usr/bin/python3

"""
根据静态wasm二进制生成各个section的二进制块，放入section_dir目录
"""

import os
import subprocess
import configparser
config = configparser.ConfigParser()
config.read('config')
wasm_home = config['DEFAULT']['wasm_demo']
project = config['DEFAULT']['project']
wasm_bin = config['DEFAULT']['wasm_bin']
wasm_file = os.path.join(wasm_home, project, wasm_bin)
section_dir = os.path.join(wasm_home, project, "python/sections")
if not os.path.isdir(section_dir):
    os.mkdir(section_dir)


def gen_section_map(file):
    cmd = "wasm-objdump -h {}".format(file)
    mem_list = []
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    info = out.stdout.read().decode()
    mapping = info.split("Sections:")[-1].strip()
    
    section_map = []

    for line in mapping.split("\n"):
        tmp = []    # tmp中item的格式为tag, start_addr, size
        list = line.strip().split(" ")
        
        tag, start_msg, end_msg, size_msg = list[0], list[1], list[2], list[3][1:-1]
        print(tag, start_msg, end_msg, size_msg)
        tmp.append(tag)
        tmp.append(int(start_msg.split("=")[1], 16))
        tmp.append(int(size_msg.split("=")[1], 16))
        section_map.append(tmp)
    
    return section_map

def dump_block(item, file, dest_dir):
    tag, start, size = item
    with open(file, 'rb') as f:
        f.seek(start)
        block = f.read(size)
    with open("{}/{}".format(dest_dir, tag), 'wb') as f:
        f.write(block)

def main():
    
    
    section_map = gen_section_map(wasm_file)

    for elem in section_map:
        if elem[0] != "Custom":
            dump_block(elem, wasm_file, section_dir)
    

if __name__ == "__main__":
    main()