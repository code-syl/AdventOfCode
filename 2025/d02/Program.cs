using System.Globalization;
using System.Text.RegularExpressions;

var input = File.ReadAllLines("input.real")[0];
var ranges = input.Split(",").Select(r =>
{
    var split = r.Split("-");
    return new {Min = Convert.ToInt64(split[0]), Max = Convert.ToInt64(split[1])};
});

// Part 1
var sum = 0L;

foreach (var range in ranges)
{
    for (var i = range.Min; i <= range.Max; i++)
    {
        var digits = i == 0L ? 1 : (i > 0L ? 1 : 2) + (int)Math.Log10(Math.Abs((double)i));
        if (digits % 2 != 0) continue;

        var split = SplitIntegerInTwo(i, digits);
        if (split.Left == split.Right) sum += i;
    }
}

Console.WriteLine($"Part 1: {sum}");

// Part 2
sum = 0L;

foreach (var range in ranges)
{
    for (var i = range.Min; i <= range.Max; i++)
    {
        // regex to the rescue
        if (IsMadeOfRepeatingDigits(i)) sum += i;
    }
}

Console.WriteLine($"Part 2: {sum}");


static (long Left, long Right) SplitIntegerInTwo(long n, int digits)
{
    var k = digits / 2;
    var pow = 1;

    for (var i = 0; i < k; i ++) pow *= 10;
    
    var abs = Math.Abs(n);
    var left = abs / pow;
    var right = abs % pow;

    if (n < 0) left = -left;

    return (left, right);
}

static bool IsMadeOfRepeatingDigits(long n)
{
    if (n < 10) return false;
    
    var s = Math.Abs(n).ToString();
    return IsRepeatingDigits().IsMatch(s);
}

partial class Program
{
    [GeneratedRegex(@"^(\d+)\1+$")]
    private static partial Regex IsRepeatingDigits();
}