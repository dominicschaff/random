#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <sys/signal.h>

long long total, end, max, start;
char *string = "dramatis personae claudius king of denmark marcellus officer";
char *letter = "abcdefghijklmnopqrstuvwxyz ";

static void signal_handler(int signum)
{
    int i;
    switch (signum) {
        case SIGHUP:
            for (i = 0; i < max;i++){
                printf("%c", string[i]);
            }
            printf("\n");
            end = time(NULL);
            if (end > start)
                printf("%10lld : %20lld : %10lld k/s : %lld\n", max, total, total/(end-start), end-start);
            break;
    }
}

static void setup_signal_handlers()
{
    struct sigaction act;

    act.sa_handler = &signal_handler;
    sigemptyset(&act.sa_mask);
    act.sa_flags = 0;

    sigaction(SIGHUP, &act, NULL);
}


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
    int l;
    start = time(NULL);
    total = 0;
    max = 0;
    setup_signal_handlers();
    for(;;){
        l=0;
        for (;*(letter + (xorshf96()%27)) == *(string + l++););
        total+=l;
        if (l>max){
            max = l;
        }
    }
}