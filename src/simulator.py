'''
Code written for inf-2200, University of Tromso
'''

import sys
from mipsSimulator import MIPSSimulator

def runSimulator(sim, max_cycles=4):
    # Skriv startadresse
    print("Startadresse for PC:", hex(sim.pc.currentAddress()))

    # Kjør til max_cycles nås
    while sim.nCycles < max_cycles:
        sim.tick()
    print(f"Finished after {sim.nCycles} cycles")
















if __name__ == '__main__':
    assert(len(sys.argv) == 2), 'Usage: python %s memoryFile' % (sys.argv[0],)
    memoryFile = sys.argv[1]
    
    simulator = MIPSSimulator(memoryFile)
    print("=== Instruction memory loaded ===")
    print(simulator.instructionMemory.memory)
    runSimulator(simulator)
