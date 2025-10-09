'''
Code written for inf-2200, University of Tromso
'''

import sys
from mipsSimulator import MIPSSimulator

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


def controller(decoded_instr):
    opcode = decoded_instr["opcode"]
    funct = decoded_instr.get("funct", None)
    ctrl_signals = {
        "RegDst": 0,
        "Branch": 0,
        "MemRead": 0,
        "MemToReg": 0,
        "ALUOp": "00",
        "RegWrite": 0,
        "ALUSrc": 0,
        "MemWrite": 0,
    }
    # addi
    if opcode == 0x08:  
        ctrl_signals["ALUSrc"] = 1
        ctrl_signals
    # legg til flere etterhvert...
    else:
        print(f"Unsupported opcode {hex(opcode)}")

    return ctrl_signals


def runSimulator(sim):
    # Replace this with your own main loop!
    counter = 0
    while (counter < 4):
        sim.tick()
        # print(sim.dataMemory.memory)
        pc_val = sim.pc.currentAddress()
        converted_adress = (pc_val - (pc_val % 4))
        memory = sim.instructionMemory.memory
        instr = sim.instructionMemory.memory.get(converted_adress,0)

        # print(f"PC={converted_adress}  Instr={hex(instr)}")
        # print(sim.pc.currentAddress())
        count = 0
        
        #for key,value in memory.items():
        #    if(key == converted_adress):
        #        print(f"count {count} key - {key} adress - {converted_adress}")
        #
        #        print(f"{hex(key)} - {hex(value)}")
        #    count = count +1
#
        #if(converted_adress in memory):
        #     print(f"pc value = {hex(pc_val)} found in memory")
        #else:
        #     print(f"pc value = {hex(pc_val)} not found in memory")

        pc_value = sim.pc.getOutputValue("pcAddress")

        pc_instructions = sim.instructionMemory.getOutputValue("instruction")

        decoded_instructions = decoder(instr)


        controller(decoded_instructions)
        signals = controller(decoded_instructions)
        print(f"Instruksjon: {decoded_instructions}")
        print(f"Kontrollsignaler: {signals}")
        # print("Dekodet instruksjon:", decoded_instructions)













        counter = counter+1



if __name__ == '__main__':
    assert(len(sys.argv) == 2), 'Usage: python %s memoryFile' % (sys.argv[0],)
    memoryFile = sys.argv[1]
    
    simulator = MIPSSimulator(memoryFile)
    print("=== Instruction memory loaded ===")
    print(simulator.instructionMemory.memory)
    runSimulator(simulator)
