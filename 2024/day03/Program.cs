using System.Text.RegularExpressions;

const string file = "input.real";
var data = string.Join("", await File.ReadAllLinesAsync(file));
var findings = new List<Finding>();

// Part 1
var regex = MyMulRegex();
var matches = regex.Matches(data);
var sum = 0;
foreach (Match match in matches)
{
    var value = match.ToString();
    // remove redundant characters
    value = value!.TrimStart("mul(".ToCharArray());
    value = value.TrimEnd(')');
    var numbers = value.Split(',').Select(s => Convert.ToInt32(s)).ToList();
    var product = numbers[0] * numbers[1];
    sum += product;
    findings.Add(new Finding(match.Index, Type.Product, product));
}
Console.WriteLine($"Day 03 Part 1: {sum}.");

// Part 2
var doRegexMatches = MyDoRegex().Matches(data);
var dontRegexMatches = MyDontRegex().Matches(data);
foreach (Match match in doRegexMatches)
    findings.Add(new Finding(match.Index, Type.Do, 0));
foreach (Match match in dontRegexMatches)
    findings.Add(new Finding(match.Index, Type.Dont, 0));

var moreAccurateSum = 0;
var state = State.Enabled;
var orderedFindings = findings.OrderBy(f => f.Index).ToList();
foreach (var finding in orderedFindings)
{
    switch (finding.Type)
    {
        case Type.Do:
            state = State.Enabled;
            break;
        case Type.Dont:
            state = State.Disabled;
            break;
        case Type.Product:
            if (state == State.Enabled)
                moreAccurateSum += finding.Product!;
            break;
        default:
            throw new ApplicationException("Unknown error, shouldn't be possible!");
    }
}
Console.WriteLine($"Day 03 Part 2: {moreAccurateSum}.");

internal enum Type
{
    Do, 
    Dont,
    Product
}

internal enum State
{
    Enabled,
    Disabled
}

internal record Finding(int Index, Type Type, int Product);

partial class Program
{
    [GeneratedRegex(@"mul\([0-9]+,[0-9]+\)")]
    private static partial Regex MyMulRegex();
    
    [GeneratedRegex(@"don't\(\)")]
    private static partial Regex MyDontRegex();
    
    [GeneratedRegex(@"do\(\)")]
    private static partial Regex MyDoRegex();
}