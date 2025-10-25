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
        # Hente adresse til aktuelle instruksjon
        pc_val = sim.pc.currentAddress()
        converted_adress = (pc_val - (pc_val % 4))
        instr = sim.instructionMemory.memory.get(pc_val,0)
        decoded_instr = sim.instructionMemory.decode(instr)
        print(decoded_instr)
        print("fuck")



