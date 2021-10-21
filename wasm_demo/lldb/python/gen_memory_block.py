#!/usr/bin/env python3
"""
dump wasmtime进程的内存空间，放入output_dir目录
"""
import os
import subprocess
import configparser
import shutil


config = configparser.ConfigParser()
config.read('config')
wasm_home = config['DEFAULT']['wasm_demo']
project = config['DEFAULT']['project']
wasm_bin = config['DEFAULT']['wasm_bin']
block_size = config['DEFAULT']['block_size']
wasm_file = os.path.join(wasm_home, project, wasm_bin)
output_dir = os.path.join(wasm_home, project, "python/mem_output")
if os.path.isdir(output_dir):
    shutil.rmtree(output_dir)

if not os.path.isdir(output_dir):
    os.mkdir(output_dir)


# 查找正在被调试的wasmtime进程
def get_pid():
    cmd = "ps -ef | grep wasmtime"
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    info = out.stdout.read().decode()
    
    ret_list = []
    for line in info.split("\n"):
        if "lldb" not in line:
        #if "-g" in line and "lldb" not in line:
            for elem in line.split(" "):
                if elem:
                    ret_list.append(elem)
    
    # print(ret_list)
    pid = ret_list[1]
    return pid

def get_proc_maps(pid):
    cmd = "cat /proc/{}/maps".format(pid)
    mem_list = []
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    info = out.stdout.read().decode()

    ret_list = []
    interval_list = []
    for line in info.split("\n"):
        if ".so" not in line and "v" not in line:
            # print(line)
            tmp = []
            for elem in line.split(" "):
                if elem:
                    tmp.append(elem)
            
            if tmp:
                ret_list.append(tmp)
                interval_list.append(tmp[0])
    
    return interval_list, ret_list

def check_between(addr, interval_list):
    for elem in interval_list:
        addr_start, end_addr = elem.split("-")

        start = int(addr_start, 16)
        end = int(end_addr, 16)
        if start < addr and addr < end:
            return start, end

def dump_block(pid, start, end, output):
    size = end - start
    print("dump size: {}".format(size))
    # if size > 3000000:
    #     print("oversize:", size)
    #     return

    with open("/proc/%s/mem" % pid, 'rb') as f:
        f.seek(start)
        block = f.read(size)
    with open(output, 'wb') as f:
        f.write(block)

def dump_rt_mem(interval_list, pid):
    
    for elem in interval_list:
        output = "{}/{}".format(output_dir, elem)
        start_addr, end_addr = elem.split("-")
        start = int(start_addr, 16)
        end = int(end_addr, 16)
        dump_block(pid, start, end, output)
        print("[*] dump memory ok, pid={}, interval={}".format(pid, elem))

def main():
    
    pid = get_pid()
    interval_list, detail_list = get_proc_maps(pid)
    # start, end = check_between(0x00007ffff7fe6181, interval_list)
    # dump_block(pid, start, end, output)
    print(interval_list)
    dump_rt_mem(interval_list, pid)
    




if __name__ == "__main__":
    main()
