import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alishbakiyani/MR_Lab_Alishba_Kiyani/week1/my_first_pkg/install/my_first_pkg'
