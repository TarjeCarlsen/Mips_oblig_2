'''
Implements CPU element for Data Memory in MEM stage.

Code written for inf-2200, University of Tromso
'''

from cpuElement import CPUElement
from memory import Memory
import common
from common import fromSignedWordToUnsignedWord


class DataMemory(Memory): 
    def __init__(self, filename):
        Memory.__init__(self, filename)
        
    def connect(self, inputSources, outputValueNames, control, outputSignalNames):
        CPUElement.connect(self, inputSources, outputValueNames, control, outputSignalNames)

        assert(len(inputSources) == 1 or len(inputSources) == 2), 'DataMemory should have one or two inputs'
        assert(len(outputValueNames) >= 1), 'registerFile should given at least one output'
        assert(len(control) == 1), 'DataMemory should have one control source'
        
        self.address = inputSources[0][1]
        self.writeData = inputSources[1][1]
        self.readData = outputValueNames[0]
        self.control_signals = control[0][1]
    
    def writeOutput(self):
        control_signals = self.controlSignals.get(self.control_signals, {})
        if not control_signals:
           return
       
        address = self.inputValues.get(self.address, 0)
        aligned_adress = address - (address % 4)

        if control_signals.get('MemRead', 0):
            readValue = self.memory.get(aligned_adress, 0)

            self.outputValues[self.readData] = fromSignedWordToUnsignedWord(readValue)

        if control_signals.get('MemWrite', 0):
           writeData = self.inputValues.get(self.writeData, None)
           if writeData is None:
               return

           self.memory[aligned_adress] = fromSignedWordToUnsignedWord(writeData)




       
