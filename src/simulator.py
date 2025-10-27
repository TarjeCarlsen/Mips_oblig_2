'''
Code written for inf-2200, University of Tromso
'''

import sys
from mipsSimulator import MIPSSimulator

def runSimulator(sim, max_cycles=None, verbose=False):
    """
    Minimal simulation loop: call sim.tick() repeatedly until a break
    is observed (via controller controlSignals) or until max_cycles is
    reached. Returns number of cycles executed.
    """
    cycles = 0
    try:
        while True:
            # Read PC before the tick so we know which instruction is being executed
            try:
                pc_val = sim.pc.currentAddress()
            except Exception:
                pc_val = None

            # Align PC to word (multiple of 4)
            if pc_val is not None:
                pc_aligned = pc_val - (pc_val % 4)
            else:
                pc_aligned = None

            # Snapshot instruction word from instruction memory (may be 0)
            instr_word = None
            try:
                if pc_aligned is not None:
                    instr_word = sim.instructionMemory.memory.get(pc_aligned, 0)
            except Exception:
                instr_word = None

            # Execute one cycle
            sim.tick()
            cycles += 1

            # After tick, read decoded instruction and control signals (if produced)
            decoded = None
            ctrl = None
            try:
                decoded = sim.instructionMemory.outputValues.get('instruction')
            except Exception:
                decoded = None

            try:
                ctrl = sim.controller.outputControlSignals.get('controlSignals')
            except Exception:
                ctrl = None

            # Print one line per cycle: PC, raw instr, decoded instr, control signals
            if pc_aligned is not None:
                print(f"PC=0x{pc_aligned:08X}\tInstr=0x{(instr_word or 0):08X}\tDecoded={decoded}\tControl={ctrl}")
            else:
                print(f"PC=None\tDecoded={decoded}\tControl={ctrl}")

            # Stop if controller signalled break
            if isinstance(ctrl, dict) and (ctrl.get('Break') == 1 or ctrl.get('ALUOp') == 'break'):
                if verbose:
                    print(f"Break encountered at cycle {cycles}")
                break

            if max_cycles is not None and cycles >= max_cycles:
                if verbose:
                    print(f"Reached max_cycles={max_cycles}, stopping.")
                break

            if verbose and cycles % 100 == 0:
                print(f"Cycle {cycles}")
    except KeyboardInterrupt:
        print(f"Interrupted by user after {cycles} cycles.")

    return cycles
















if __name__ == '__main__':
    assert(len(sys.argv) == 2), 'Usage: python %s memoryFile' % (sys.argv[0],)
    memoryFile = sys.argv[1]
    
    simulator = MIPSSimulator(memoryFile)
    print("=== Instruction memory loaded ===")
    print(simulator.instructionMemory.memory)
    runSimulator(simulator)
