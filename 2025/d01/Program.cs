var lines = File.ReadAllLines("./real.txt");
var commands = lines.Select(l =>
{
    var direction = l[..1] == "L" ? Direction.Left : Direction.Right;
    var steps = Convert.ToInt32(l.Substring(1));
    return (Direction: direction, Steps: steps);
});

var start = 50;
var max = 99;
var current = start;
var password = 0;

// Part 1
foreach (var command in commands)   
{
    switch (command.Direction)
    {
        case Direction.Left: 
                current = ((max + 1) + (current - command.Steps) % (max + 1)) % (max + 1); // cycle negatively (max 100)
                break;
        case Direction.Right:
                current = (current + command.Steps) % (max + 1); // cycle positively (max 100)
                break;
    }

    if (current == 0)
        password++;
}

Console.WriteLine($"Part 01: {password}");

current = start;
password = 0;

// Part 2
foreach (var command in commands)
{
    switch (command.Direction)
    {
        case Direction.Left:
            for (var i = 0; i < command.Steps; i++)
            {
                current--;
                if (current == 0) password++;
                if (current < 0) current = 99;
            }
            break;
        case Direction.Right:
            for (var i = 0; i < command.Steps; i++)
            {
                current++;
                if (current > 99) current = 0;
                if (current == 0) password++;
            }
            break;
    }
}

Console.WriteLine($"Part 02: {password}");


enum Direction
{
    Left,
    Right
};