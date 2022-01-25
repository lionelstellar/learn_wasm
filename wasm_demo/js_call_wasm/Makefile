CC=emcc
all:
	$(CC) demo.c -Os -s WASM=1 -s SIDE_MODULE=1 -o demo.wasm
clean:
	rm *.wasm 
