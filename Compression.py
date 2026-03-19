""" To compress we use disparity between frequencies and use variable length encoding Less bits for frequent characters and vice versa
1: Count frequencies and create a dictionary
2:Make a priority queue of binary trees
3:Convert all the binary trees into a single huffman tree
4:Build an encoding map
5:Encode the data(Use the encoding map to convert the strings to new binary representations)
6: Write the binary string to a binary file
"""


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
    frequencies[256]=1 #An integer is never a character in the text file
    file.close()

    return frequencies



def pqinitialisation():
    pq=[]
    return pq

def pqenqueue(pq,node):
    pq.append(node)

    
    


def pqdequeue(pq):
    lowestfreq=pq[0].frequency
    lowestfreqindex=0
    for i in range(1,len(pq)):
        if pq[i].frequency<lowestfreq:
            lowestfreq=pq[i].frequency
            lowestfreqindex=i
    lowestfreqnode=pq[lowestfreqindex]
    pq.pop(lowestfreqindex)
    return lowestfreqnode




def Insertsingletons(frequencies,pq):
    for character,frequency in frequencies.items():
        obj=Node(character,frequency)
        pqenqueue(pq,obj)


def Build_Huffman_Tree(pq):
    while len(pq)!=1:
        low=pqdequeue(pq)
        newlow=pqdequeue(pq)
        internalnode=Node(None,low.frequency+newlow.frequency)
        internalnode.left=low
        internalnode.right=newlow
        pqenqueue(pq,internalnode)
    return pqdequeue(pq) #This is the huffman or mapping tree

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

    binary+=Encoding_Map[256]
    file.close()
    return binary



def MakeBinaryFile(binary):
    while len(binary)%8!=0:
        binary+="0"
    binaryfile=open("compressed.bin","wb")
    for i in range(0,len(binary),8):
        integer=int(binary[i:i+8],2)
        binaryfile.write(bytes([integer]))
    binaryfile.close()
    