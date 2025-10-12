'''
Code written for inf-2200, University of Tromso
'''

import sys
from mipsSimulator import MIPSSimulator

def decoder(pc_instructions):
    opcode = (pc_instructions >> 26) & 0x3f

    if opcode == 0x00:
        # R type
        rs = (pc_instructions >> 21) & 0x1F
        rt = (pc_instructions >> 16) & 0x1F
        rd = (pc_instructions >> 11) & 0x1F
        shamt = (pc_instructions >> 6) & 0x1F
        funct = pc_instructions & 0x3F

        return {"instruction_type": "R", "opcode": opcode, "rs": rs, "rt": rt, 
                "rd": rd, "shamt": shamt, "funct": funct}

    elif opcode in [0x02, 0x03]:
        # J type
        adress = pc_instructions & 0x3FFFFFF
        return {"instruction_type": "J",
                "opcode": opcode, "adress": adress}

    elif opcode in [0x08, 0x09, 0x0F, 0x23, 0x2B, 0x04, 0x05, 0x0D]: 
        # I type
        rs = (pc_instructions >> 21) & 0x1F
        rt = (pc_instructions >> 16) & 0x1F
        imm = pc_instructions & 0xFFFF

        return {"instruction_type": "I", "opcode": opcode, 
                "rs": rs, "rt": rt, "imm": imm}
    
    else:
        print("Decoder could not decode instructions!")





def runSimulator(sim):
    # Replace this with your own main loop!
    counter = 0
    while (counter < 10):
        # print(sim.dataMemory.memory)
        pc_val = sim.pc.currentAddress()
        converted_adress = (pc_val - (pc_val % 4))
        memory = sim.instructionMemory.memory
        instr = sim.instructionMemory.memory.get(converted_adress,0)

        count = 0
        
        pc_value = sim.pc.getOutputValue("pcAddress")

        pc_instructions = sim.instructionMemory.getOutputValue("instruction")
        print(f"PC: {converted_adress}  Instr: {hex(instr)}")
        decoded_instructions = decoder(instr)

        sim.tick()

        counter = counter+1



if __name__ == '__main__':
    assert(len(sys.argv) == 2), 'Usage: python %s memoryFile' % (sys.argv[0],)
    memoryFile = sys.argv[1]
    
    simulator = MIPSSimulator(memoryFile)

    print(simulator.instructionMemory.memory)
    runSimulator(simulator)
