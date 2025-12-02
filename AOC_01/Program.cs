namespace AOC_01
{
    internal class Program
    {
        static int CurrentCode = 50;
        static void Main(string[] args)
        {
            Console.WriteLine("FilePath:");
            string path = Console.ReadLine();
            List<int> angles = GetData(path);

            // part1:
            CurrentCode = 50;
            int count1 = 0;
            for (int i = 0; i < angles.Count; i++)
            {
                CurrentCode = (CurrentCode + angles[i]) % 100; // xd
                if (CurrentCode == 0) count1++;
            }
            Console.WriteLine("RESULT: " + count1);

            // part2
            CurrentCode = 50;
            int count2 = 0;
            for (int i = 0; i < angles.Count; i++)
            {
                count2 += Rotate(angles[i]);
            }
            Console.WriteLine(count2);
        }

        static int Rotate(int angle)
        {
            int count = 0;
            while (angle > 0)
            {
                CurrentCode++;
                angle--;

                if (CurrentCode == 100) CurrentCode = 0;
                if (CurrentCode == 0) count++;
            }
            while (angle < 0)
            {
                CurrentCode--;
                angle++;

                if (CurrentCode == -100) CurrentCode = 0;
                if (CurrentCode == 0) count++;
            }
            
            CurrentCode = CurrentCode % 100;
            
            return count;
        }

        static List<int> GetData(string path)
        { 
            List<int> output = new List<int>();
            StreamReader sr = new StreamReader(path);
            while (!sr.EndOfStream)
            {
                int multip = 1;
                string line = sr.ReadLine();
                if (line == null)
                    return output;

                if (line[0] == 'L')
                    multip = -1;
                output.Add(int.Parse(line.Substring(1)) * multip);
            }

            return output;
        }
    }
}
