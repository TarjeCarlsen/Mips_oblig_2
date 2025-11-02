from cpuElement import CPUElement

class ALU(CPUElement):
    #Performs arithmetic operations. Not finished, currently only performing add, addu, addi, addiu operations used for testing.
    def connect(self, inputSources, outputValueNames, control, outputSignalNames):
        CPUElement.connect(self, inputSources, outputValueNames, control, outputSignalNames)
        assert len(inputSources) == 2, 'ALU needs two inputs'
        assert len(outputValueNames) == 1, 'ALU produces one output'
        assert len(control) == 1, 'ALU needs one control input'

        self.a = inputSources[0][1]
        self.b = inputSources[1][1]
        self.output = outputValueNames[0]
        self.control_signal = control[0][1]

    def writeOutput(self):
        control = self.controlSignals.get(self.control_signal, {})
        op = control.get("ALUOp", "")
        alu_src = control.get("ALUSrc", 0)

        a = self.inputValues.get(self.a, 0)
        b = self.inputValues.get(self.b, 0)

        if alu_src == 1: #used in testing with immediate instruction, something that was removed, but would still be implemented if a working solution were found.
            instr = control.get("instr", {})
            if "imm" in instr:
                b = instr["imm"]


        if op in ("add", "addu", "addi", "addiu"):
            result = a + b
        elif():
            print("testing outside add")
        else:
            result = 0

        self.outputValues[self.output] = result & 0xffffffff
