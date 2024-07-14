#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

enum ERROR
{
    ERROR_READ_FILE = -1,
    ERROR_BAD_ARGUMENT = -2,
    ERROR_MEMORY_ALLOCATION = -3,
};

typedef struct Present
{
    int Length;
    int Width;
    int Height;
} Present;

int countLines(FILE* file)
{
    int counter = 0;

    for(;;)
    {
        const int bufferSize = 65535;
        char buffer[bufferSize];
        const size_t size = fread(buffer, 1, bufferSize, file);

        if (ferror(file))
        {
            return ERROR_READ_FILE;
        }

        size_t i = 0;
        char previous = 'a';
        for (i = 0; i < size; i++)
        {
            previous = buffer[i];
            if (buffer[i] == '\n')
            {
                counter++;
            }
        }

        if (feof(file))
        {
            if (previous != '\n')
            {
                counter++;
            }

            break;
        }
    }

    return counter;
}

int getPresentDimensions(FILE* file, Present* array, const int* size)
{
    if (ferror(file))
    {
        return ERROR_READ_FILE;
    }

    char* line = NULL;
    size_t lineLength = 0;

    for (int i = 0; i <= *size && (getline(&line, &lineLength, file)) != -1; i++)
    {
        int dimensions[3];
        const char* token = strtok(line, "x");

        for (int j = 0; j < 3; j++)
        {
            if (token != NULL)
            {
                dimensions[j] = atoi(token);
            }

            token = strtok(NULL, "x");
        }

        array[i].Length = dimensions[0];
        array[i].Width = dimensions[1];
        array[i].Height = dimensions[2];
    }

    return 0;
}

int getRequiredWrappingPaperTotal(const Present* presents, const int* numberOfPresents, int* solution)
{
    int total = 0;
    for (int i = 0; i < *numberOfPresents; i++)
    {
        const int areas[3] =
        {
            (2 * presents[i].Length * presents[i].Width),
            (2 * presents[i].Width * presents[i].Height),
            (2 * presents[i].Height * presents[i].Length)
        };
        const int surfaceArea = areas[0] + areas[1] + areas[2];
        int smallestArea = INT32_MAX;

        for (int j = 0; j < 3; j++)
        {
            if (areas[j] < smallestArea)
            {
                smallestArea = areas[j];
            }
        }

        total += surfaceArea + (smallestArea / 2);
    }

    *solution = total;
    return 0;
}

int main(const int argc, char** argv)
{
    if (argc != 2)
    {
        printf("Please use a file as the first argument.\nUsage: %s <file>\n", argv[0]);
        return ERROR_BAD_ARGUMENT;
    }

    FILE* file = fopen(argv[1], "r");
    const int lines = countLines(file);
    fclose(file);

    if (lines < 0)
    {
        return ERROR_READ_FILE;
    }

    Present* presents = calloc(lines, sizeof(Present));
    if (presents == NULL)
    {
        fprintf(stderr, "Memory for presents was unable to be allocated!");
        return ERROR_MEMORY_ALLOCATION;
    }

    file = fopen(argv[1], "r");
    const int result = getPresentDimensions(file, presents, &lines);
    int solution = -1;
    if (result >= 0)
    {
        getRequiredWrappingPaperTotal(presents, &lines, &solution);
        printf("Part 1: %d\n", solution);
    }

    fclose(file);
    free(presents);
    return 0;
}