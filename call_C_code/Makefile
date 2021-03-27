all: call_adder

call_adder: adder.c
	gcc -shared -o adder.so -fPIC adder.c

run: call_adder.py
	python call_adder.py

clean:
	rm -rf adder.so