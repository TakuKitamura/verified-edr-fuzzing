all:
	afl-gcc -I $(KREMLIN_HOME)/include $(wildcard *.c) -o fuzzed
fuzzing:
	rm -rf testcases; python3 genTestCases.py;