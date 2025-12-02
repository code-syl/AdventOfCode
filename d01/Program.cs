var lines = File.ReadAllLines("./example.txt");
var commands = lines.Select(l =>
{
    var direction = l.Substring(0,1) == "L" ? Direction.Left : Direction.Right;
    var steps = Convert.ToInt32(l.Substring(1));
    return (Direction: direction, Steps: steps);
});

var start = 50;
var max = 99;
var current = start;
var password = 0;

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

    Console.WriteLine(current);
}


enum Direction
{
    Left,
    Right
};