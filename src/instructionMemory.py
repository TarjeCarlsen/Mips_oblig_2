'''
Implements CPU element for Instruction Memory in MEM stage.

Code written for inf-2200, University of Tromso
'''

from cpuElement import CPUElement
from memory import Memory

class InstructionMemory(Memory):
    def __init__(self, filename):
        Memory.__init__(self, filename)
    
    def connect(self, inputSources, outputValueNames, control, outputSignalNames):
        CPUElement.connect(self, inputSources, outputValueNames, control, outputSignalNames)
        
        # Remove this and replace with your implementation!

        self.input = list(self.inputValues.keys())[0]
        self.instruction = outputValueNames[0]

        # raise AssertionError("connect not implemented in class InstructionMemory!")
    
    def writeOutput(self):
        # Remove this and replace with your implementation!

        pc = self.inputValues[self.input]

        instructions = self.memory.get(pc, 0)

        self.outputValues[self.instruction] = instructions

        # raise AssertionError("writeOutput not implemented in class InstructionMemory!")
