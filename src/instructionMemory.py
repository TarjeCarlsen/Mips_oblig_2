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
        raise AssertionError("connect not implemented in class InstructionMemory!")
    
    def writeOutput(self):
        # Remove this and replace with your implementation!
        raise AssertionError("writeOutput not implemented in class InstructionMemory!")
    
    def decoder(pc_instructions):
        # Segment the bit string and figure out what kind of instruction this is
        opcode = (pc_instructions >> 26) & 0x3f

        if opcode == 0x00:
            # The instruction is of type R
            rs = (pc_instructions >> 21) & 0x1F
            rt = (pc_instructions >> 16) & 0x1F
            rd = (pc_instructions >> 11) & 0x1F
            shamt = (pc_instructions >> 6) & 0x1F
            funct = pc_instructions & 0x3F

            return {"instruction_type": "R", "opcode": opcode, "rs": rs, "rt": rt, 
                    "rd": rd, "shamt": shamt, "funct": funct}

        elif opcode in [0x02, 0x03]:
            # The instruction is of type J
            adress = pc_instructions & 0x3FFFFFF
            return {"instruction_type": "J",
                    "opcode": opcode, "adress": adress}

        elif opcode in [0x08, 0x09, 0x0F, 0x23, 0x2B, 0x04, 0x05, 0x0D]: 
            # The instruction is of type I
            rs = (pc_instructions >> 21) & 0x1F
            rt = (pc_instructions >> 16) & 0x1F
            imm = pc_instructions & 0xFFFF

            return {"instruction_type": "I", "opcode": opcode, 
                    "rs": rs, "rt": rt, "imm": imm}
        
        else:
            print("Decoder: Could not decode instructions!")
