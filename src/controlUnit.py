from cpuElement import CPUElement

class ControlUnit(CPUElement):
    def __init__(self):
        super().__init__()

    def connect(self, input, outputValueNames, control, outputSignalNames):
        self.instruction = list(self.inputValues.keys())[0]
        return super().connect(input, outputValueNames, control, outputSignalNames)

    def writeOutput(self):
        instr = self.inputValues[self.instruction] 
        opcode = (instr >> 26) & 0x3F 
        funct = instr & 0x3F
        ctrl_signals = {
            "RegDst": 0,
            "Branch": 0,
            "MemRead": 0,
            "MemToReg": 0,
            "ALUOp": "00",
            "RegWrite": 0,
            "ALUSrc": 0,
            "MemWrite": 0,
            "Jump": 0,
            "Break": 0,
        }
    # R type instructions
        if opcode == 0x00 and funct == 0x20:
            ctrl_signals["RegDst"] = 1
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUOp"] = "add"
        elif opcode == 0x00 and funct == 0x21:
            ctrl_signals["RegDst"] = 1
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUOp"] = "addu"
        elif opcode == 0x00 and funct == 0x22:
            ctrl_signals["RegDst"] = 1
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUOp"] = "sub"
        elif opcode == 0x00 and funct == 0x23:
            ctrl_signals["RegDst"] = 1
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUOp"] = "subu"
        elif opcode == 0x00 and funct == 0x24:
            ctrl_signals["RegDst"] = 1
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUOp"] = "and"
        elif opcode == 0x00 and funct == 0x25:
            ctrl_signals["RegDst"] = 1
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUOp"] = "or"
        elif opcode == 0x00 and funct == 0x27:
            ctrl_signals["RegDst"] = 1
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUOp"] = "nor"
        elif opcode == 0x00 and funct == 0x2A:
            ctrl_signals["RegDst"] = 1
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUOp"] = "slt"
    # I type instructions
        elif opcode == 0x08:
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUSrc"] = 1
            ctrl_signals["ALUOp"] = "addi"
        elif opcode == 0x09:
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUSrc"] = 1
            ctrl_signals["ALUOp"] = "addiu"
        elif opcode == 0x23:
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUSrc"] = 1
            ctrl_signals["MemRead"] = 1
            ctrl_signals["MemToReg"] = 1
            ctrl_signals["ALUOp"] = "lw"
        elif opcode == 0x2B:
            ctrl_signals["ALUSrc"] = 1
            ctrl_signals["MemWrite"] = 1
            ctrl_signals["ALUOp"] = "sw"
        elif opcode == 0x04:
            ctrl_signals["Branch"] = 1
            ctrl_signals["ALUOp"] = "beq"
        elif opcode == 0x05:
            ctrl_signals["Branch"] = 1
            ctrl_signals["ALUOp"] = "bne"
        elif opcode == 0x0F:
            ctrl_signals["RegWrite"] = 1
            ctrl_signals["ALUSrc"] = 1
            ctrl_signals["ALUOp"] = "lui"
    # Jump type instructions
        elif opcode == 0x02:
            ctrl_signals["Jump"] = 1
            ctrl_signals["ALUOp"] = "jump"
    # Break
        elif opcode == 0x00 and funct == 0x0D:
            ctrl_signals["Break"] = 1
            pass
        else:
            print(f"Unsupported opcode {hex(opcode)}")
        for name, value in ctrl_signals.items():
            self.outputControlSignals[name] = value
            print(value)
        return ctrl_signals
    

if __name__ == '__main__':
    ControlUnit()
