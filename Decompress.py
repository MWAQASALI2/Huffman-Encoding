""" 0: Get Frequency table from the Json file
1: Convert the binary file into a long binary string
2: Rebuild the huffman tree using the frequency table
3: Read the binary string and use the huffman tree to convert it into a string
4: Write to a text file
"""
from Compression import Insertsingletons,Build_Huffman_Tree,lstinitialisation,lstenqueue,lstdequeue,Node
import json

def GetFrequencyTable(Frequenciesjson):
    file=open(Frequenciesjson,"r")
    FrequencyTable=json.load(file)
    file.close()
    return FrequencyTable


#Binary byte to integer to a long binary string
def BinaryFiletoBinaryString(compressedfile):
    file=open(compressedfile,"rb")
    binarystring=""
    byte=file.read(1)
    while byte:
        integer=byte[0]
        binarystring+=bin(integer)[2:].zfill(8) # integer to binary string remove first 2 then fill zeros to make its length 8
        byte=file.read(1)
    file.close()    
    return binarystring


def Reconstruct_Huffman_Tree(BinaryCompressedFile):
    lst=lstinitialisation()
    FrequencyTable=GetFrequencyTable(BinaryCompressedFile[0:len(BinaryCompressedFile)-4]+".json")
    Insertsingletons(FrequencyTable,lst)
    Huffman_Tree=Build_Huffman_Tree(lst)
    return Huffman_Tree

def Binary_String_To_Text(Huffman_Tree,binarystring):
    string=""
    i=0
    node=Huffman_Tree
    while node.data!=chr(0): #Run the loop until you meet the psuedo EOF character in the tree which you would have met by traversing the binary string
        direction=binarystring[i]
        if direction=="0":
            node=node.left
        if direction=="1":
            node=node.right
        if node.data!=None and node.data!=chr(0):
            string+=node.data
            node=Huffman_Tree
        i+=1
    return string

def Write_Text_To_File(string,binarydecompressfile):
    file=open(binarydecompressfile[0:len(binarydecompressfile)-4]+"uncompressed"+".txt","w",encoding="utf-8")
    file.write(string)
    file.close()


def Decompress_Whole(BinaryCompressedFile):#This compressedFile is the binary file
    Huffman_Tree=Reconstruct_Huffman_Tree(BinaryCompressedFile)
    binarystring=BinaryFiletoBinaryString(BinaryCompressedFile)
    string=Binary_String_To_Text(Huffman_Tree,binarystring)
    Write_Text_To_File(string,BinaryCompressedFile)
    Originalfile=open(BinaryCompressedFile[0:len(BinaryCompressedFile)-4]+".txt","r",encoding="utf-8")
    Uncompressedfile=open(BinaryCompressedFile[0:len(BinaryCompressedFile)-4]+"uncompressed"+".txt","r",encoding="utf-8")
    Originalstring=""
    Uncompressedstring=""
    for line in Originalfile:
        Originalstring+=line
    for line in Uncompressedfile:
        Uncompressedstring+=line
    Originalfile.close()
    Uncompressedfile.close()
    if Originalstring==Uncompressedstring:
        return "Uncompressed and original file match"
    else:
        return"Uncompressed and original file do not  match"
        



        