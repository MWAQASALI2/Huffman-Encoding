''' Compression.py takes a .txt file and produces a .bin file and a .json file.
Decompress.py takes a .bin file , finds the corresponding .json file and produces a .txt file.
So the compressed file is actually the .bin file but to decompress you need the .bin file along with the .json file so when calculating size of compressed 
files add the size of .bin and .json file.
'''
from Compression import Compress_Whole
from Decompress import Decompress_Whole
from os.path import getsize

option=""
while option!="C" and option!="D":
    option=input("To compress press C and to decompress press D: ").upper()
if option=="C":
    filename=input("Enter the file name to compress: ")
    Compress_Whole(filename)
elif option=="D":
    filename=input("Enter the compressed binary file name to Decompress: ")
    while filename[len(filename)-4:len(filename)]!=".bin":
        filename=input("Enter the compressed binary file name to Decompress: ")

    status=Decompress_Whole(filename)
    if status=="Uncompressed and original file match":
        jsonfile=filename[0:len(filename)-4]+".json"
        textfileoriginal=filename[0:len(filename)-4]+".txt"
        totalcompressedsize=(getsize(filename)+getsize(jsonfile))/1024 #binary file +jsonfile
        textfilesizeoriginal=getsize(textfileoriginal)/1024
        sizereduced=(((textfilesizeoriginal-totalcompressedsize)/textfilesizeoriginal)*100)
        print("Uncompressed and original file match")
        print("The size of the compressed files consists of json and binary file.")
        print("Original: "+str(round(textfilesizeoriginal,2))+"KB---------> "+"Compressed: "+str(round(totalcompressedsize,2))+"KB ("+str(int(sizereduced))+" % smaller"+")" )
    elif status =="Uncompressed and original file do not  match":
        print("Uncompressed and original file do not  match")


    



        





