'''
Code written for inf-2200, University of Tromso
'''

import sys
from mipsSimulator import MIPSSimulator

def runSimulator(sim, max_cycles=4): #Running 4 cycles, used for testing one test.mem file

    print("Startadresse for PC:", hex(sim.pc.currentAddress()))


    while sim.nCycles < max_cycles:
        sim.tick()
    print(f"Finished after {sim.nCycles} cycles")


if __name__ == '__main__': #Used for debugging 
    assert(len(sys.argv) == 2), 'Usage: python %s memoryFile' % (sys.argv[0],)
    memoryFile = sys.argv[1]
    
    simulator = MIPSSimulator(memoryFile)
    print("=== Instruction memory loaded ===")
    print(simulator.instructionMemory.memory)
    runSimulator(simulator)
