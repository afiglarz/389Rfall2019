#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define BUFF_SIZE 32
#define FLAG_SIZE 32
#define PASS_SIZE 16

int main(void) {
  int i, j, prompt_response;
  /* password for admin to provide to dump flag */
  char *password;

  /* seed random with time so that we can password */
  for (j = 0; j < 10; j++) {
    srand(time(0));
    password = calloc(1, PASS_SIZE+1);
    for (i = 0; i < PASS_SIZE; i++) {
      password[i] = rand() % ('z'-' ') + ' ';
    }
    password[PASS_SIZE] = 0;
    printf("%s", password);
    printf("\n");
    sleep(1);
    
  }
}
