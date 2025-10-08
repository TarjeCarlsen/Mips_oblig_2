'''
Code written for inf-2200, University of Tromso
'''

import sys
from mipsSimulator import MIPSSimulator

def runSimulator(sim):
    # Replace this with your own main loop!
    counter = 0
    while (counter < 25):
        sim.tick()
        # print(sim.dataMemory.memory)
        pc_val = sim.pc.currentAddress()
        memory = sim.instructionMemory.memory
        instr = sim.instructionMemory.memory.get(pc_val,0)

        converted_adress = (pc_val - (pc_val % 4))
        # print(f"PC={converted_adress}  Instr={hex(instr)}")
        # print(sim.pc.currentAddress())
        count = 0
        for key,value in memory.items():
            if(key == converted_adress):
                print(f"count {count} key - {key} adress - {converted_adress}")

                print(f"{hex(key)} - {hex(value)}")
            count = count +1

        # if(converted_adress in memory):
        #     print(f"pc value = {hex(pc_val)} found in memory")
        # else:
        #     print(f"pc value = {hex(pc_val)} not found in memory")




        counter = counter+1

if __name__ == '__main__':
    assert(len(sys.argv) == 2), 'Usage: python %s memoryFile' % (sys.argv[0],)
    memoryFile = sys.argv[1]
    
    simulator = MIPSSimulator(memoryFile)
    print("=== Instruction memory loaded ===")
    print(simulator.instructionMemory.memory)
    runSimulator(simulator)
