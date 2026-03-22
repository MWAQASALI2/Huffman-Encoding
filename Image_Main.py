from ImageCompression import Compress_Image_Whole
from ImageDecompressor import Decompress_Image_Whole
from os.path import getsize
import json




option=""
while option!="C" and option!="D":
    option=input("To compress an image press C and to decompress press D: ").upper()
if option=="C":
    filename=input("Enter the file name to compress : ")
    Compress_Image_Whole(filename)
    print("DONE")
elif option=="D":
    filename=input("Enter the compressed binary file name to Decompress: ")
    while filename[len(filename)-4:len(filename)]!=".bin":
        filename=input("Enter the compressed binary file name to Decompress: ")
    status=Decompress_Image_Whole(filename)
    print("DONE")
    if status=="Original and Uncompressed image match!":
        jsonfile=filename[0:len(filename)-4]+".json"
        file=open(jsonfile,"r")
        Dictionary=json.load(file)
        Image_Format=Dictionary["image_format"]
        originalimage=filename[0:len(filename)-4]+Image_Format
        #uncompressedimage='Uncompressed'+filename[0:len(filename)-4]+Image_Format
        originalsize=getsize(originalimage)/1024
        compressedsize=(getsize(filename)+getsize(jsonfile))/1024
        sizereduced=(((originalsize-compressedsize)/originalsize)*100)
        print("Original and uncompressed files match")
        print("The size of the compressed files consists of json and binary file.")
        print("Original: "+str(round(originalsize,2))+"KB---------> "+"Compressed(json+binary): "+str(round(compressedsize,2))+"KB ("+str(int(sizereduced))+" % smaller"+")" )
    elif status =="Uncompressed and original file do not  match":
        print("Uncompressed and original file do not  match")


    

