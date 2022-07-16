#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// gcc bofbof.c -o bofbof -fno-stack-protector -no-pie


int main(int argc, char* argv[]) {
    
    int grade = 9;
    int protector_bof = 0xdeadbeef;
    char code[16];

    printf("Please enter your student code:\n> ");
    scanf("%s", code);
    if(protector_bof != 0xdeadbeef) {
        printf("What are you trying to do ??? My protector is 0x%x now -_-\n", protector_bof);
    } else {
        if(grade < 10)
            printf("Your grade is %d ! Oh no road to 2B...\n", grade);
        else if(grade > 20)
            printf("%d, more than 20 ?! Suspicious...\n", grade);
        else if(grade < 20)
            printf("%d ? Try to get 20 !\n", grade);
        else {
            printf("You got 20 ! Congratz, here is your shell\n");
            setreuid(geteuid(), geteuid());
            system("/bin/bash");
        }
    }
    return 0;
}