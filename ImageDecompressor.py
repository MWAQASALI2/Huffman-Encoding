import json
from Decompress import BinaryFiletoBinaryString
from Compression import lstinitialisation,lstenqueue,lstdequeue,Insertsingletons,Build_Huffman_Tree
from PIL import Image

'''From the binary file find corresponding json file and get Frequency table ,size and format.
Recostruct huffman tree from Frequency table
Convert the binary file to binary string then to pixels using huffman tree now a list of rgb values
then convert to image here you use size and format.
'''


def GetFrequencytable_size_and_format(jsonfile):
    file=open(jsonfile,"r")
    Dictionary=json.load(file)
    FrequencyTable=Dictionary["frequencytable"]
    size=Dictionary["size"]
    IntgerFrequencyTable={}
    image_format=Dictionary["image_format"]

    for key,value in FrequencyTable.items():
        IntgerFrequencyTable[int(key)]=value
    return (IntgerFrequencyTable,size,image_format)

def Reconstruct_Huffman_Tree_integerkeys(IntegerFrequencyTable):
    lst=lstinitialisation()
    Insertsingletons(IntegerFrequencyTable,lst)
    Huffman_Tree=Build_Huffman_Tree(lst)
    return Huffman_Tree

def BinaryString_to_pixels(BinaryString,HuffmanTree):
    lst=[]
    i=0
    node=HuffmanTree
    while node.data!=256:
        direction=BinaryString[i]
        if direction=="0":
            node=node.left
        elif direction=="1":
            node=node.right
        
        if node.left==None and node.right==None and node.data!=256: #No children and not equal to 256 
            lst.append(node.data)
            node=HuffmanTree
        i+=1
    return lst #The list contains rgb values [23,73,42,43,83,54]

def Write_pixels_to_image(pixels,size,binaryfile,image_format):
    listoftuples=[]
    for pixel in range(0,len(pixels),3):
        rgbtuple=tuple([pixels[pixel],pixels[pixel+1],pixels[pixel+2]])
        listoftuples.append(rgbtuple)
    uncompressedimage=Image.new("RGB",tuple(size))
    uncompressedimage.putdata(listoftuples)
    uncompressedimage.save("Uncompressed"+binaryfile[0:len(binaryfile)-4]+image_format) #Image format is either png or bmp
    return "Uncompressed"+binaryfile[0:len(binaryfile)-4]+image_format


def Decompress_Image_Whole(BinaryCompressedfile):
    IntegerFrequencyTable,size,image_format=GetFrequencytable_size_and_format(BinaryCompressedfile[0:len(BinaryCompressedfile)-4]+".json")
    Huffman_Tree=Reconstruct_Huffman_Tree_integerkeys(IntegerFrequencyTable)
    Binary_String=BinaryFiletoBinaryString(BinaryCompressedfile)
    listofpixels=BinaryString_to_pixels(Binary_String,Huffman_Tree)
    uncompressed_image_name=Write_pixels_to_image(listofpixels,size,BinaryCompressedfile,image_format)

#Verifying if both images match or not
    original_image_name=BinaryCompressedfile[0:len(BinaryCompressedfile)-4]+image_format
    uncompressedimage=Image.open(uncompressed_image_name)
    uncompressedimage=uncompressedimage.convert("RGB")
    uncompressedimage=list(uncompressedimage.getdata())

    originalimage=Image.open(original_image_name)
    originalimage=originalimage.convert("RGB")
    originalimage=list(originalimage.getdata())
    if uncompressedimage==originalimage:
        return "Original and Uncompressed image match!"
    else:
        "Original and uncompressed image do not match!"






    















