import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

import idatool.breakpoints

if __name__ == '__main__':
    breakpoints = idatool.breakpoints.Util()
    breakpoints.Add("FunctionTree", "Pointer")
    breakpoints.Save()
    breakpoints.Exit()