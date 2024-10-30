#include <stdio.h>
#include "search.h"

int main()
{
    char filename[] = "../SourceText/data1-1MB.txt";
    char pattern[] = "../SourceText/pattern1.txt";
  
    struct FileData fd;
    //readSourceFile(filename,&fd,FILE_LOAD_LINES,SOURCE_LINE_SIZE);
    readSourceFile(filename,&fd,FILE_LOAD_SPLIT_ONELINE,SOURCE_LINE_SIZE);

    struct FileData pat;
    readSourceFile(pattern,&pat,FILE_LOAD_LINES,SEARCH_LINE_SIZE);

    printf("Read %ld lines for %ld characters in source, %ld lines for %ld chars in search\n",fd.lines,fd.length,pat.lines,pat.length);

    //printf("CAR in CARNIVAL %d\n",Search("CARNIVAL","CAR"));
    //printf("CAR in APPLECART %d\n",Search("APPLECART","CAR"));
    //printf("CAR in TREEHOUSE %d\n",Search("TREEHOUSE","CAR"));

    //Search(fd.data[4500],pat.data[0]);


    for(long p=0; p<pat.lines; ++p)
    {
        //printf("P=%ld ",p);
        for(long l=0; l<fd.lines; ++l)
        {
            //printf("L=%ld ",l);
            long s = Search(fd.data[l],fd.linesize,pat.data[p],pat.linesize,SEARCH_MODE_FIRST);
            if (s>=0)
                printf("%s,%ld,%ld\n",pat.data[p],l,s);
        }
    }

    for(long p=0; p<pat.lines; ++p)
    {
        long count = 0;
        for(long l=0; l<fd.lines; ++l)
        {
            count += Search(fd.data[l],fd.linesize,pat.data[p],pat.linesize,SEARCH_MODE_COUNT);
        }
        printf("%s = %ld\n",pat.data[p],count);
    }


    return 0;
}