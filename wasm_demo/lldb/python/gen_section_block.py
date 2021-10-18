#!usr/bin/env python3
import os
import subprocess
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
    wasm_home = "/home/jiangyikun/learn_wasm/wasm_demo/"
    file = os.path.join(wasm_home, "lldb/test.wasm")
    dest_dir = os.path.join(wasm_home, "lldb/python/sections")
    
    section_map = gen_section_map(file)

    for elem in section_map:
        if elem[0] != "Custom":
            dump_block(elem, file, dest_dir)
    

if __name__ == "__main__":
    main()