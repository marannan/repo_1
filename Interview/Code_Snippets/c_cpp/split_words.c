#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int split(char *str, char *arr[10]){
    int beginIndex = 0;
    int endIndex;
    int maxWords = 10;
    int wordCnt = 0;

    while(1){
        while(isspace(str[beginIndex])){
            ++beginIndex;
        }
        if(str[beginIndex] == '\0')
            break;
        endIndex = beginIndex;
        while (str[endIndex] && !isspace(str[endIndex])){
            ++endIndex;
        }
        int len = endIndex - beginIndex;
        char *tmp = calloc(len + 1, sizeof(char));
        memcpy(tmp, &str[beginIndex], len);
        arr[wordCnt++] = tmp;
        beginIndex = endIndex;
        if (wordCnt == maxWords)
            break;
    }
    return wordCnt;
}

int main(void) {
    char *arr[10];
    int i;
    int n = split("1st 2nd 3rd", arr);

    for(i = 0; i < n; ++i){
        puts(arr[i]);
        free(arr[i]);
    }

    return 0;
}