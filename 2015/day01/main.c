#include <stdio.h>
#include <stdlib.h>

int partOne(const char* fileName, int* solution);
int partTwo(const char* fileName, int* solution);
int changeFloor(const char* direction, int* floor);

enum ERROR
{
    ERROR_READ_FILE = -1,
    ERROR_BAD_ARGUMENT = -2,

    ERROR_SANTALESS_BASEMENT = -90
};

int main(const int argc, char** argv)
{
    if (argc != 2)
    {
        printf("Please use a file as the first argument.\nUsage: %s <file>\n", argv[0]);
        return ERROR_BAD_ARGUMENT;
    }

    int solution = 0;
    int result = partOne(argv[1], &solution);
    if (result >= 0)
    {
        printf("The solution to part 1 is: %d\n", solution);
    }

    result = partTwo(argv[1], &solution);
    if (result >= 0)
    {
        printf("The solution to part 2 is: %d\n", solution);
    }

    return 0;
}

int partOne(const char* fileName, int* solution)
{
    FILE* file = fopen(fileName, "r");
    if (file == NULL)
    {
        printf("Couldn't open the file: %s", fileName);
        return ERROR_READ_FILE;
    }

    char direction;
    int floor = 0;
    while (direction != EOF)
    {
        direction = fgetc(file);
        changeFloor(&direction, &floor);
    }

    fclose(file);
    *solution = floor;
    return 0;
}

int partTwo(const char* fileName, int* solution)
{
    FILE* file = fopen(fileName, "r");
    if (file == NULL)
    {
        printf("Couldn't open the file: %s", fileName);
        return ERROR_READ_FILE;
    }

    int position = 1;
    char direction;
    int floor = 0;
    while (direction != EOF)
    {
        direction = fgetc(file);
        changeFloor(&direction, &floor);

        if (floor < 0)
        {
            fclose(file);
            *solution = position;
            return 0;
        }

        position++;
    }

    fclose(file);
    printf("Santa did not reach the basement :-(.");
    *solution = -1;
    return ERROR_SANTALESS_BASEMENT;
}

int changeFloor(const char* direction, int* floor)
{
    switch (*direction)
    {
    case '(':
        (*floor)++;
        break;
    case ')':
        (*floor)--;
        break;
    default:
        ; // do nothing
    }

    return 0;
}