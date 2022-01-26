## buffer_overflow
使用wat2wasm二进制工具将demo.wat字节码文件转化为demo.wasm二进制文件（https://github.com/WebAssembly/wabt）
```bash
./wat_gen_wasm.sh
```
运行服务让浏览器访问test.htm
```bash
./start_server.sh
```