#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <errno.h>
int make_num(char input[2]){
    char num1, num2;
    num1 = input[0];
    num2 = input[1];
    num1 = num1 - 48; // convert to integer
    num2 = num2 - 48;
    return (num1*10+num2);

}

int find_val(char result[2], FILE *input) {
    char cur;
    int index = 0;
    int total = 0;
    cur = getc(input);
    while (cur != EOF) {
        if (cur == '\n') {
            index = 0;
            total = total + make_num(result);
        } else if (isdigit(cur)) {
            result[index] = cur;
            if (index == 0) {
                index++;
                result[index] = cur;
            } 
        }
        cur = getc(input);

    }
    return total;

}

int main (int argc, char* argv[]) {
  if (argc != 2) {
    fprintf(stderr, "Usage: %s filename\n", argv[0]);
    return EXIT_FAILURE;
  }

  FILE * stream = fopen(argv[1], "r");
  if (stream == NULL) {
    fprintf(stderr, "%s: Cannot open %s: %s\n", argv[0], argv[1], strerror(errno));
    return EXIT_FAILURE;
  }

  char arr[2];
  int ans;
  ans = find_val(arr, stream);
  printf("Answer is %d  ", ans);
  return 0;
}