#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// gcc format.c -o format -fno-stack-protector -no-pie

int main(int argc, char* argv[]) {

    if(argc < 2) {
        printf("Usage: %s <NAME>", argv[0]);
        return -1;
    }
    char * SECRET = "CTF101{5c1eb9a99fdfbc7d4d70599cacd15ba2}";
    int a = 0xdeadbeef;
    char * b = "Hello!";
    int c = -1;

    printf("Hello ");
    printf(argv[1]);

    return 0;
}