from PIL import Image
from Compression import Node,lstinitialisation,lstenqueue,lstdequeue,Insertsingletons,Build_Huffman_Tree,Build_Encoding_Map,MakeBinaryFile
import json
'''Exact same pipeline except we count how many times each rgb value appears so like how many times 240 appears
Then Builds Huffman tree then encoding map then encodes and saves it in a binary file
Then stores the frequency table and image size width and length in a json file 
Psuedo eof here too
For png and bmp
'''



def rgbvalue_frequency_count(Image_name):#We count how many times does each rgb value appear like how many times 43 appears etc
    image=Image.open(Image_name)
    image=image.convert("RGB")
    lst=list(image.getdata())#List of tuples[(240,90,2),(32,54,43).....] Contains RGB values
    frequencytable={}
    for rgbtuple in lst:
        for value in rgbtuple:
            if value not in frequencytable:
                frequencytable[value]=1
            else:
                frequencytable[value]+=1
    frequencytable[256]=1 #Psuedo Eof 256 as rgb values between 0-255
        
    return (frequencytable,image.size) #Returning image size as a header component which will be used later to reconstruct the image


def Encode(Image_name,Encoding_Map):
    image=Image.open(Image_name)
    image=image.convert("RGB")
    lst=list(image.getdata())
    BinaryList=[]
    for rgbtuple in lst:
        for value in rgbtuple:
            BinaryList.append(Encoding_Map[value]) 
    BinaryList.append(Encoding_Map[256])
    BinaryString="".join(BinaryList)

    return BinaryString

def SaveHeader(frequencytable,size,Image_name):#Header includes frequency table, size and image_format

    dictionary={}
    dictionary["frequencytable"]=frequencytable
    dictionary["size"]=size
    dictionary["image_format"]=Image_name[len(Image_name)-4:len(Image_name)]

    file=open(Image_name[0:len(Image_name)-4]+".json","w")
    json.dump(dictionary,file)
    file.close()





def Compress_Image_Whole(Image_name):
    frequencytable,size=rgbvalue_frequency_count(Image_name)
    lst=lstinitialisation()
    Insertsingletons(frequencytable,lst)
    Huffman_Tree=Build_Huffman_Tree(lst)
    Encoding_Map={}
    Build_Encoding_Map(Huffman_Tree,"",Encoding_Map)
    Binary_String=Encode(Image_name,Encoding_Map)
    MakeBinaryFile(Binary_String,Image_name)
    SaveHeader(frequencytable,size,Image_name)



















