'''
Implements base class for memory elements.

Note that since both DataMemory and InstructionMemory are subclasses of the Memory
class, they will read the same memory file containing both instructions and data
memory initially, but the two memory elements are treated separately, each with its
own, isolated copy of the data from the memory file.

Code written for inf-2200, University of Tromso
'''

from cpuElement import CPUElement
import common

memoryDict = {}

class Memory(CPUElement):
    def __init__(self, filename):
    
        # Dictionary mapping memory addresses to data
        # Both key and value must be of type 'long'
        self.memory = {}
        
        self.initializeMemory(filename)
    
    def initializeMemory(self, filename):
        '''
        Helper function that reads initializes the data memory by reading input
        data from a file.
        '''
        # Remove this and replace with your implementation!
        # Implementation MUST populate the dictionary in self.memory!
        
        with open(filename, "r") as f:
            for line in f:
                # line = line.strip()
                # skip empty lines or pure comments
                if not line.strip() or line.strip().startswith("#"):
                    
                    continue

                parts = line.strip().split("\t")
                if len(parts) < 2:
                    continue

                try:
                    address = int(parts[0], 16)  # hex string -> int
                    value = int(parts[1], 16)    # hex string -> int

                    self.memory[address] =value
                    # print(self.memory)
                    # print(f"adress {hex(address)} value {hex(value)} ")

                    # self.memory[address] = value
                except ValueError:
                    # ignore malformed lines
                    continue
        
    def printAll(self):
        for key in sorted(self.memory.keys()):
            print("%s\t=> %s\t(%s)" % (hex(int(key)), common.fromUnsignedWordToSignedWord(self.memory[key]), hex(int(self.memory[key]))))

