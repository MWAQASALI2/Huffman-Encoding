from Compression import Compress_Whole
from Decompress import Decompress_Whole
option=""
while option!="C" and option!="D":
    option=input("To compress press C and to decompress press D: ").upper()
if option=="C":
    filename=input("Enter the file name to compress: ")
    Compress_Whole(filename)
elif option=="D":
    filename=input("Enter the file name to Decompress: ")
    Decompress_Whole(filename)



