// Get and prepare data
const string file = "input.real";

var data = await File.ReadAllLinesAsync(file);
var column1 = new List<long>();
var column2 = new List<long>();

foreach (var row in data)
{
    var split = row.Split(Array.Empty<char>(), StringSplitOptions.RemoveEmptyEntries);
    column1.Add(Convert.ToInt64(split[0]));
    column2.Add(Convert.ToInt64(split[1]));
}

column1.Sort();
column2.Sort();

// Part 1
var part1 = 0L;
for (var i = 0; i < column1.Count; i++)
{
    var difference = Math.Abs(column2[i] - column1[i]);
    part1 += difference;
}

Console.WriteLine($"Day 01 Part 1: {part1}.");

// Part 2
var part2 = 0L;
for (var i = 0; i < column1.Count; i++)
{
    var occurrence = column2.Count(n => n == column1[i]);
    var product = column1[i] * occurrence;
    part2 += product;
}

Console.WriteLine($"Day 01 Part 2: {part2}.");