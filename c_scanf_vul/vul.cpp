#define _CRT_SECURE_NO_DEPRECATE 0
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
    char buffer[80];

    cin >> setw(sizeof buffer) >> buffer;
    // scanf("%s", buffer);
    printf("Hello ");
    cout << buffer << endl;

    return 0;
}
