'''
Code written for inf-2200, University of Tromso
'''

import unittest
from cpuElement import CPUElement
import common


class RegisterFile(CPUElement):
    def __init__(self):
        # Dictionary mapping register number to register value
        self.register = {}
        # Note that we won't actually use all the registers listed here...
        self.registerNames = ['$zero', '$at', '$v0', '$v1', '$a0', '$a1', '$a2', '$a3',
                              '$t0', '$t1', '$t2', '$t3', '$t4', '$t5', '$t6', '$t7',
                              '$s0', '$s1', '$s2', '$s3', '$s4', '$s5', '$s6', '$s7',
                              '$t8', '$t9', '$k0', '$k1', '$gp', '$sp', '$fp', '$ra']
        # All registers default to 0
        for i in range(0, 32):
            self.register[i] = 0

    def connect(self, inputSources, outputValueNames, control, outputSignalNames):
        CPUElement.connect(self, inputSources, outputValueNames, control, outputSignalNames)
        assert(len(inputSources) == 2), 'registerFile should have two inputs'
        assert(len(outputValueNames) == 2), 'registerFile should given two outputs'
        assert(len(control) == 1), 'registerFile should have one control source'
        # assert(len(outputSignalNames) == 1), 'registerFile should have one control input' 

        self.instr = inputSources[0][1]
        if len(inputSources) > 1:
            self.writeData = inputSources[1][1]

        self.control_output = control[0][1]

        self.rs = outputValueNames[0]
        self.rt = outputValueNames[1]

    def writeOutput(self):
        instr = self.inputValues.get(self.instr, {})
        rs = instr.get('rs', 0)
        rt = instr.get('rt', 0)
        self.outputValues[self.rs] = self.register.get(rs, 0)
        self.outputValues[self.rt] = self.register.get(rt, 0)
    
    def setControlSignals(self):
        control_signals = self.controlSignals.get(self.control_output, {})

        if control_signals.get('regWrite', 0):
            instr = self.inputValues.get(self.instr, {})

            if instr.get('rd') == 0:
                writeReg = instr.get('rd', 0)
            if instr.get('rd') == 1:
                writeReg = instr.get('rt', 0)

            writeData = self.inputValues.get(self.writeData, None)
            
            if writeData == None:
                return
            



    def printAll(self):
        '''
        Print the name and value in e ach register.
        '''

        print()
        print("Register file")
        print("================")
        for i in range(0, 32):
            print("%s \t=> %s (%s)" % (self.registerNames[i], common.fromUnsignedWordToSignedWord(
                self.register[i]), hex(int(self.register[i]))[:-1]))
        print("================")
        print()
        print()


class TestRegisterFile(unittest.TestCase):
    def setUp(self):
        # Implement me!
        pass

    def test_correct_behavior(self):
        # Implement me!
        pass


if __name__ == '__main__':
    unittest.main()
