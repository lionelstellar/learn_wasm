## Install RUNTIME

### 1.安装wasmtime（https://github.com/bytecodealliance/wasmtime）

安装

```bash
$ wget https://wasmtime.dev/install.sh
$ bash install.sh
```

测试

```
$ wasmtime
wasmtime 0.29.0
Wasmtime WebAssembly Runtime
```



## Install toolchain

### 1. emscripten（编译器，官方文档https://emscripten.org/）

安装

```bash
$ git clone git://github.com/emscripten-core/emsdk.git
$ cd emsdk
$ ./emsdk install latest
$ ./emsdk activate latest
$ source ./emsdk_env.sh
```

添加环境变量

```bash
$ source "/home/jiangyikun/learn_wasm/toolchain/emsdk/emsdk_env.sh"

## 如果不想每次打开新的shell都要source一遍，可以把上面这个source执行的结果写入到/etc/profile
```

测试

```bash
$ emcc
emcc: error: no input files
```

### 2. clang-11（编译器）

on page https://github.com/WebAssembly/wasi-sdk/releases

下载对应平台的sdk压缩包，解压后不需安装直接课使用



添加环境变量到/etc/profile

```bash
#wasi-sdk
export WASI_SDK_HOME=/path to wasi-sdk-12.0/
export PATH=$PATH:$WASI_SDK_HOME/bin/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$WASI_SDK_HOME/share/wasi-sysroot/lib/wasm32-wasi/
export SYSROOT=$WASI_SDK_HOME/share/wasi-sysroot
```

测试

```bash
$ clang-11
clang-11: error: no input files
```



### 3. WABT（wasm与wat格式互换，及objdump等二进制工具）

安装

```bash
$ git clone --recursive https://github.com/WebAssembly/wabt
$ cd wabt
$ git submodule update --init

$ mkdir build
$ cd build
$ cmake ..
$ cmake --build .
```

添加环境变量到/etc/profile

```bash
#WABT
export PATH=$PATH:/home/jiangyikun/learn_wasm/toolchain/wabt/build
```

测试

```bash
$ wasm-objdump
wasm-objdump: expected filename argument.
Try '--help' for more information.
```


