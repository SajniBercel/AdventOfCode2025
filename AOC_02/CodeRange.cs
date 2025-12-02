using System.Security;

namespace AOC_02
{
    internal class CodeRange
    {
        ulong _codeA;
        ulong _codeB;

        public CodeRange(ulong a, ulong b)
        {
            _codeA = a; 
            _codeB = b;
        }

        #region part1
        public ulong CountWrongCodes1()
        {
            ulong count = 0;
            for (ulong i = _codeA; i <= _codeB; i++)
            {
                if(!Validate1(i))
                    count += i;
            }

            return count;
        }

        private bool Validate1(ulong code)
        {
            string Scode = code.ToString();

            if (Scode.Length % 2 == 1)
                return true;

            string partA = Scode.Substring(0,Scode.Length/2);
            string partB = Scode.Substring(Scode.Length / 2);

            if(partA.Equals(partB))
                return false;
            
            return true;
        }
        #endregion

        #region part2
        public ulong CountWrongCodes2()
        {
            ulong count = 0;
            for (ulong i = _codeA; i <= _codeB; i++)
            {
                for (int j = 1; j <= i.ToString().Length / 2; j++)
                {
                    if (!Validate2(i.ToString(), j))
                    {
                        count += i;
                        break;
                    }
                }
            }

            return count;
        }

        private bool Validate2(string code, int splitLen)
        {
            string split = code.Substring(0, splitLen);

            for (int i = splitLen; i < code.Length; i += splitLen)
            {
                string temp = "";

                if (i + splitLen <= code.Length)
                    temp = code.Substring(i, splitLen);
                else
                    temp = code.Substring(i);

                if (!split.Equals(temp))
                    return true;
            }

            return false;
        }
        #endregion

        public override string ToString()
        {
            return $"{_codeA} - {_codeB}";
        }
    }
}
