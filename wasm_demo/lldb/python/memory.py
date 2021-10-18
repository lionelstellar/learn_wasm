#!/usr/bin/env python3
import os
import subprocess

# 查找正在被调试的wasmtime进程
def get_pid():
    cmd = "ps -ef | grep wasmtime"
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    info = out.stdout.read().decode()
    
    ret_list = []
    for line in info.split("\n"):
        if "-g" in line and "lldb" not in line:
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
        if ".so" not in line:
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
        addr_start, addr_end = elem.split("-")

        start = int(addr_start, 16)
        end = int(addr_end, 16)
        

        if start < addr and addr < end:
            return start, end

def dump_block(pid, start, end, output):
    size = end - start
    with open("/proc/%s/mem" % pid, 'rb') as f:
        f.seek(start)
        block = f.read(size)
    with open(output, 'wb') as f:
        f.write(block)

def main():
    

    output = "/home/jiangyikun/learn_wasm/wasm_demo/lldb/output/block"
    pid = get_pid()
    interval_list, detail_list = get_proc_maps(pid)
    start, end = check_between(0x00007ffff7fe6181, interval_list)
    dump_block(pid, start, end, output)

if __name__ == "__main__":
    main()
