all:
	afl-gcc -I $(KREMLIN_HOME)/include $(wildcard *.c) -o fuzzed
fuzzing:
	rm -rf testcases; mkdir testcases; python3 genTestCases.py && afl-fuzz -i testcases/ -o out/ ./fuzzed