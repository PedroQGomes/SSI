#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main (char *argv[])
{
    int fd;
    int i=0;
    fd = open("/diretoriaMount/teste.txt",O_CREAT | O_TRUNC | O_WRONLY);

    for(i=0 ;i<10;i++)
    {
        write(fd,"a",1);
    }
    close(fd);
    return 0;

}