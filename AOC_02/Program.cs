namespace AOC_02
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<CodeRange> Codes = GetData();

            // part1
            ulong result1 = 0;
            for (int i = 0; i < Codes.Count; i++)
            {
                result1 += Codes[i].CountWrongCodes1();
            }

            Console.WriteLine("RESULT1: " + result1);

            // part2
            ulong result2 = 0;
            for (int i = 0; i < Codes.Count; i++)
            {
                result2 += Codes[i].CountWrongCodes2();
            }

            Console.WriteLine("RESULT2: " + result2);
        }

        static List<CodeRange> GetData()
        {
            Console.WriteLine("File Path:");
            string filepath = Console.ReadLine();
            StreamReader sr = new StreamReader(filepath);

            List<string> lines = new List<string>();
            while (!sr.EndOfStream)
            { 
                lines.Add(sr.ReadLine());
            }
            sr.Close();

            List<CodeRange> output = new List<CodeRange>();

            for (int i = 0; i < lines.Count; i++)
            { 
                string[] ranges = lines[i].Split(',');
                for (int j = 0; j < ranges.Length; j++)
                {
                    if (ranges[j].Length > 3)
                    {
                        string[] parts = ranges[j].Split("-");
                        output.Add(new CodeRange(ulong.Parse(parts[0]), ulong.Parse(parts[1])));
                    }
                }
            }

            return output;
        }
    }
}
