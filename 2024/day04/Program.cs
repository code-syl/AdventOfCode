// Prepare the matrix

using System.Text.RegularExpressions;

const string file = "input.real";
var data = await File.ReadAllLinesAsync(file);
var matrix = data.Select(d => d.ToCharArray()).ToArray();
const string xmas = "XMAS";

// Part 1
var o = 0;
for (var y = 0; y < matrix.Length; y++)
{
    for (var x = 0; x < matrix[0].Length; x++)
    {
        if (matrix[y][x] != 'X')
            continue;

        var found = SearchForWordAt(matrix, y, x, xmas, out var occurrences);
        if (found)
            o += occurrences;
    }
}
Console.WriteLine($"Day 04 Part 1: {o}");

// Part 2
// The A in the XMAS cross is always in the middle,
// thus we do not need to check the outer wall.
o = 0;
for (var y = 1; y < matrix.Length - 1; y++)
{
    for (var x = 1; x < matrix[0].Length - 1; x++)
    {
        if (matrix[y][x] != 'A')
            continue;
        
        if (IsMiddleOfXmasCross(matrix, y, x))
            o++;
    }
}
Console.WriteLine($"Day 04 Part 2: {o}");

return;

bool IsMiddleOfXmasCross(char[][] grid, int y, int x)
{
    /*
     * The four possible patterns are:
     *    M*S     M*M     S*M     S*S
     *    *A*     *A*     *A*     *A*
     *    M*S     S*S     S*M     M*M
     */

    /*if (grid[y - 1][x - 1] == 'M' && grid[y - 1][x + 1] == 'S' && grid[y + 1][x - 1] == 'M' &&
        grid[y + 1][x + 1] == 'S')
        return true;
    if (grid[y - 1][x - 1] == 'M' && grid[y - 1][x + 1] == 'M' && grid[y + 1][x - 1] == 'S' &&
        grid[y + 1][x + 1] == 'S')
        return true;
    if (grid[y - 1][x - 1] == 'S' && grid[y - 1][x + 1] == 'M' && grid[y + 1][x - 1] == 'S' &&
        grid[y + 1][x + 1] == 'M')
        return true;
    if (grid[y - 1][x - 1] == 'S' && grid[y - 1][x + 1] == 'S' && grid[y + 1][x - 1] == 'M' &&
        grid[y + 1][x + 1] == 'M')
        return true;*/

    // Simplified version of above
    var solutions = new[] { "MSMS", "MMSS", "SMSM", "SSMM" };
    var word = new string(new[] { grid[y - 1][x - 1], grid[y - 1][x + 1], grid[y + 1][x - 1], grid[y + 1][x + 1] });
    
    return solutions.Contains(word);
}

bool SearchForWordAt(char[][] grid, int y, int x, string word, out int occurrences)
{
    occurrences = 0;
    
    // Re-check first character
    if (grid[y][x] != word[0])
        return false;
    
    // Directions
    var dirX = new[] { -1, 0, 1, -1, 1, -1, 0, 1 };
    var dirY = new[] { -1, -1, -1, 0, 0, 1, 1, 1 };

    var wordLength = word.Length;

    
    for (var direction = 0; direction < dirX.Length; direction++)
    {
        int i;
        var currentX = x + dirX[direction];
        var currentY = y + dirY[direction];
        
        for (i = 1; i < wordLength; i++)
        {
            // Bounds check
            if (currentX >= grid[0].Length || currentX < 0 ||
                currentY >= grid.Length || currentY < 0)
                break;

            if (grid[currentY][currentX] != word[i])
                break;
            
            // Move in the direction
            currentX += dirX[direction];
            currentY += dirY[direction];
        }

        if (i == wordLength)
            occurrences++;
    }

    return occurrences > 0;
}