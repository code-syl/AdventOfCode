// Get and prepare data
const string file = "input.real";
var data = await File.ReadAllLinesAsync(file);
var reports = data
    .Select(r => r
        .Split(' ', StringSplitOptions.RemoveEmptyEntries)
        .Select(n => Convert.ToInt32(n)))
    .Select(report => report.ToList())
    .ToList();

// Part 1
var numberOfSafeReports = reports.Count(r => r.IsSafe(out _));
Console.WriteLine($"Day 02 Part 1: {numberOfSafeReports}.");

// Part 2
numberOfSafeReports = reports.Count(r => r.IsSafeWithDampener());
Console.WriteLine($"Day 02 Part 2: {numberOfSafeReports}.");

return;

public static class ReportExtensions
{
    public enum State
    {
        Increasing = 1,
        Decreasing = -1,
        Same = 0
    }
    
    public static bool IsSafe(this List<int> report, out int? badIndex)
    {
        badIndex = null;
        if (report.Count == 1)
            return true;

        var previous = report[0];
        var previousStateChange = State.Same;
        
        
        for (var i = 1; i < report.Count; i++)
        {
            var difference = Math.Abs(previous - report[i]);
            if (difference > 3)
            {
                badIndex = i;
                return false;
            }

            if (previous == report[i])
            {
                badIndex = i;
                return false;
            }

            if (previous > report[i])
            {
                if (previousStateChange == State.Increasing)
                {
                    badIndex = i;
                    return false;
                }

                previousStateChange = State.Decreasing;
            }

            if (previous < report[i])
            {
                if (previousStateChange == State.Decreasing)
                {
                    badIndex = i;
                    return false;
                }

                previousStateChange = State.Increasing;
            }

            previous = report[i];
        }
        
        return true;
    }

    public static bool IsSafeWithDampener(this List<int> report)
    {
        if (report.IsSafe(out var badIndex))
            return true;

        if (badIndex is null)
            throw new ApplicationException("Unknown error, if badIndex is null, should've returned true");

        for (var i = 0; i < report.Count ; i++)
        {
            var tempReport = new List<int>(report);
            tempReport.RemoveAt(i);
            if (tempReport.IsSafe(out _))
                return true;
        }

        return false;
    }
}