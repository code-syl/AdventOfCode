var lines = File.ReadAllLines("input.example");

var banks = lines.Select(l =>
{
    return l.ToCharArray().Select(c => c - '0');
}).ToArray();
var sum = 0;

// Part 1

foreach (var b in banks)
{
    var bank = b.ToArray();

    // walk from left to right per array - 1 to get the highest digit
    var current = 0;
    var highest = 0;

    for (var i = current; i < bank.Length - 1; i++)
    {
        if (bank[i] == 9)
        {
            highest = bank[i];
            current = i + 1;
            break;
        }

        if (bank[i] > highest) {
            highest = bank[i];
            current = i;
        }
    }

    // then continue where left off till end or 9
    if (highest != 9) current++;
    var first = highest;
    highest = 0;
    for (var i = current; i < bank.Length; i++)
    {
        if (bank[i] == 9)
        {
            highest = bank[i];
            break;
        }

        if (bank[i] > highest) highest = bank[i];
    }

    var second = highest;
    sum += Convert.ToInt32($"{first}{second}");
}

Console.WriteLine($"Part 1: {sum}");