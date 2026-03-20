""" To compress we use disparity between frequencies and use variable length encoding Less bits for frequent characters and vice versa
1: Count frequencies and create a dictionary
2:Make a list of binary trees using characters and frequencies
3:Convert all the binary trees into a single huffman tree
4:Build an encoding map
5:Encode the data(Use the encoding map to convert the strings to new binary representations)
6: Write the binary string to a binary file
7:Store the frequency table in a json file , used in decompression to reconstruct the Huffman tree
"""
import json


class Node:
    def __init__(self,character,frequency):
        self.data=character
        self.frequency=frequency
        self.left=None
        self.right=None



def text_frequency_count(file_name):
    file=open(file_name,"r")
    frequencies={}
    for line in file:
        for char in line:
            if char not in frequencies:
                frequencies[char]=1
            else:
                frequencies[char]+=1

    #Adding the psuedo end of file character
    frequencies[chr(0)]=1 # chr(0) is Null
    file.close()

    return frequencies



def lstinitialisation():
    lst=[]
    return lst

def lstenqueue(lst,node):
    lst.append(node)

    
    


def lstdequeue(lst):
    lowestfreq=lst[0].frequency
    lowestfreqindex=0
    for i in range(1,len(lst)):
        if lst[i].frequency<lowestfreq:
            lowestfreq=lst[i].frequency
            lowestfreqindex=i
    lowestfreqnode=lst[lowestfreqindex]
    lst.pop(lowestfreqindex)
    return lowestfreqnode




def Insertsingletons(frequencies,lst):
    for character,frequency in frequencies.items():
        obj=Node(character,frequency)
        lstenqueue(lst,obj)   


def Build_Huffman_Tree(lst):
    while len(lst)!=1:
        low=lstdequeue(lst)
        newlow=lstdequeue(lst)
        internalnode=Node(None,low.frequency+newlow.frequency)
        internalnode.left=low
        internalnode.right=newlow
        lstenqueue(lst,internalnode)
    return lstdequeue(lst) #This is the huffman or mapping tree

def Build_Encoding_Map(node,binary,encodingmap):
    if node.left is None and node.right is None:
        encodingmap[node.data]=binary
    else:
        Build_Encoding_Map(node.left,binary+"0",encodingmap)
        Build_Encoding_Map(node.right,binary+"1",encodingmap)


def Encode(filename,Encoding_Map):
    binary=""
    file=open(filename,"r")
    for line in file:
        for char in line:
            binary+=Encoding_Map[char]

    binary+=Encoding_Map[chr(0)]
    file.close()
    return binary



def MakeBinaryFile(binary,filename):
    while len(binary)%8!=0:
        binary+="0"
    binaryfile=open(filename[0:len(filename)-4]+".bin","wb")
    for i in range(0,len(binary),8):
        integer=int(binary[i:i+8],2)
        binaryfile.write(bytes([integer]))
    binaryfile.close()

def saveFrequencyTable(frequencies,filename):
    file=open(filename[0:len(filename)-4]+".json","w")
    json.dump(frequencies,file)
    file.close()




def Compress_Whole(file_name):
    Frequencies=text_frequency_count(file_name)
    lst=lstinitialisation()
    Insertsingletons(Frequencies,lst)
    Huffman_Tree=Build_Huffman_Tree(lst)
    Encoding_Map={}
    Build_Encoding_Map(Huffman_Tree,"",Encoding_Map)
    binary=Encode(file_name,Encoding_Map)
    MakeBinaryFile(binary,file_name)
    saveFrequencyTable(Frequencies,file_name)



