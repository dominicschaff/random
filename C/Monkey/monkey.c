#include <stdlib.h>
#include <stdio.h>
#include <time.h>

static unsigned long x=123456789, y=362436069, z=521288629;

unsigned long xorshf96(void) {
unsigned long t;
    x ^= x << 16;
    x ^= x >> 5;
    x ^= x << 1;

   t = x;
   x = y;
   y = z;
   z = t ^ x ^ y;

  return z;
}

int main()
{
    int i;
    long l,max,t;
    long long total, end;
    long long start = time(NULL);
    FILE *f = fopen("Hamlet.txt", "rb");
    fseek(f, 0, SEEK_END);
    long fsize = ftell(f);
    fseek(f, 0, SEEK_SET);

    char *string = malloc(fsize + 1);
    if (fread(string, fsize, 1, f));
    fclose(f);

    string[fsize] = 0;
    char *letter = "abcdefghijklmnopqrstuvwxyz ";

    total = 0;
    max = 0;
    t=0;
    while(1){
        l=0;
        while (letter[xorshf96()%27] == string[l++]) ;
        total+=l;
        if (l>max){
            max = l;
            for (i = 0; i < max;i++){
                printf("%c", string[i]);
            }
            printf("\n");
        }
        if (t++>10000000) {
            t = 0;
            end = time(NULL);
            if (end > start)
                printf("%10ld : %20lld : %10lld k/s : %lld\n", max, total, total/(end-start), end-start);
        }
    }
}