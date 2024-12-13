using System.Text.RegularExpressions;

// Prepare data
const string file = "input.real";
var data = await File.ReadAllLinesAsync(file);
var rules = new List<Rule>();
var sequences = new List<List<int>>();

foreach (var line in data)
{
    if (string.IsNullOrWhiteSpace(line))
        continue;

    var ruleRegex = RuleRegex();
    if (ruleRegex.IsMatch(line))
    {
        var numbers = line.Split('|').Select(n => Convert.ToInt32(n)).ToArray();
        rules.Add(new Rule(numbers[0], numbers[1]));
        continue;
    }

    var sequence = line
        .Split(',', StringSplitOptions.RemoveEmptyEntries)
        .Select(n => Convert.ToInt32(n))
        .ToList();
    sequences.Add(sequence);
}

// Part 1
// Out of the sequences, get the valid sequences
// A sequence is valid if the numbers are in the right order
// The order is ruled by the rules
// A rule consists of two numbers, the first needing to be printed before the second
//      example: 47|53 == the number 47 in the sequence needs to be printed before 53
var validSequences = new List<List<int>>();
var invalidSequences = new List<List<int>>();

foreach (var sequence in sequences)
{
    var applicableRules =
        rules.Where(r => sequence.Contains(r.First) && sequence.Contains(r.Second));
    var valid = false;
    
    foreach (var rule in applicableRules)
    {
        var indexOfFirst = sequence.IndexOf(rule.First);
        var indexOfSecond = sequence.IndexOf(rule.Second);

        if (indexOfFirst > indexOfSecond)
        {
            valid = false;
            invalidSequences.Add(sequence);
            break;
        }

        valid = true;
    }

    if (valid)
        validSequences.Add(sequence);
}

// Get the middle number of all valid sequences and sum
var sum = 0;
foreach (var sequence in validSequences)
{
    var length = sequence.Count;
    var middle = (int)Math.Ceiling(length / 2D);
    sum += sequence[middle - 1];
}
Console.WriteLine($"Day 05 Part 1: {sum}");

// Part 2
// Get the invalid sequences 
// Make them valid
// Get the middle item and sum of all middle items



return;

internal record Rule(int First, int Second);

partial class Program
{
    [GeneratedRegex(@"(\d)\|(\d)")]
    private static partial Regex RuleRegex();
}