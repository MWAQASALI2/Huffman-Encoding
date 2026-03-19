""" 0: Get Frequency table from the Json file
1: Convert the binary file into a long binary string
2: Rebuild the huffman tree using the frequency table
3: Read the binary string and use the huffman tree to convert it into a string
4: Write to a text file
"""
from Compression import Insertsingletons,Build_Huffman_Tree,pqinitialisation,pqenqueue,pqdequeue,Node
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
        binarystring+=bin(integer[2:].zfill(8))
        byte=file.read(1)
    file.close()
    return binarystring


def Reconstruct_Huffman_Tree(Frequenciesjson):
    pq=pqinitialisation()
    FrequencyTable=GetFrequencyTable(Frequenciesjson)
    Insertsingletons(FrequencyTable,pq)
    Huffman_Tree=Build_Huffman_Tree(pq)
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

def Write_Text_To_File(string):
    file=open("Textuncompressed.txt","w")
    file.write(string)
    file.close()



        