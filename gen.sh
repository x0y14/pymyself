# c to assembly
# gcc -S -o ./assm/main.s ./assm/main.c
# assembly to object file
as -o ./assm/main.o ./assm/main.s
# object file to binary with linker
ld -o ./assm/main ./assm/main.o -macosx_version_min 11.0 -L /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/lib -lSystem