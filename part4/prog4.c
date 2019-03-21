#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/resource.h>
#include "check.h"

int x[5] = {1,2,3,4,5};
//double c = 10.0;

void allocate()
{
    int i;
    int *p;
    for(i =1 ; i<1000000 ; i++)
    {
      p = malloc(500 * sizeof(int));
      if(func(i)) { free (p);}
    }
}

void allocate1()
{
  int i;
  int *p;
  for (i=1 ; i<10000 ; i++)
  {
    p = malloc(1000 * sizeof(int));
    if(i & 1)
      free (p);
  }
}

void allocate2()
{
  int i;
  int *p;
  for (i=1 ; i<300000 ; i++)
  {
    p = malloc(10000 * sizeof(int));
    free (p);
  }
}

//int getrusage(int, struct rusage); 

int main(int argc, char const *argv[]) {
  int i;
  int *p;
  struct rusage usage;
  struct timeval ustart, uend, sstart,send;
  printf("Executing the code ......\n");
  getrusage(RUSAGE_SELF, &usage);
  ustart = usage.ru_utime;
  sstart = usage.ru_stime;

  allocate();

  for (i=0 ; i<10000 ; i++)
  {
    p = malloc(1000 * sizeof(int));
    free (p);
  }

  getrusage(RUSAGE_SELF, &usage);
  uend = usage.ru_utime;
  send = usage.ru_stime;
  
  printf("User CPU start time: %ld.%lds\n", ustart.tv_sec, ustart.tv_usec); 
  printf("System CPU start time: %ld.%lds\n", sstart.tv_sec, sstart.tv_usec); 
  printf("User CPU end time: %ld.%lds\n", uend.tv_sec, uend.tv_usec); 
  printf("System CPU end time: %ld.%lds\n", send.tv_sec, send.tv_usec);  
  printf("Maximum RSS: %ld KB\n", usage.ru_maxrss);
  printf("Signals Received: %ld\n", usage.ru_nsignals);
  printf("Voluntary Context Switches: %ld\n", usage.ru_nvcsw);
  printf("Involuntary Context Switches: %ld\n", usage.ru_nivcsw); 
  
  printf("Program execution successfull\n");
  return 0;
}
