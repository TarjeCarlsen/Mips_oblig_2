from cpuElement import CPUElement

class ControllUnit(CPUElement):
    def __init__(self):
        super().__init__()

    def connect(self, input, outputValueNames, control, outputSignalNames):
        return super().connect(input, outputValueNames, control, outputSignalNames)
    
    def setupControllSignals(self):
        opcode = self.inputValues[self.inputSources]