
from cpuElement import CPUElement

class Controller(CPUElement):

    def connect(self, inputSources, outputValueNames, control, outputSignalNames):
        CPUElement.connect(self, inputSources, outputValueNames, control, outputSignalNames)
        assert(len(inputSources) == 1), 'Controller should have one inputs'
        assert(len(outputValueNames) == 1), 'Controller has only one output'
        assert(len(control) == 0), 'Controller has no control signals'
        assert(len(outputSignalNames) == 1), 'Controller should have one control output'

        self.decoded_instr = inputSources[0][1]
        print("Controller sin self.decoded_instr: "+ self.decoded_instr)
        self.control_name = outputSignalNames[0]
    
    def writeOutput(self):
        decoded_instr = self.inputValues[self.decoded_instr]
        control_signals = self.controller(decoded_instr)
        self.outputControlSignals[self.control_name] = control_signals

        self.outputValues['instr'] = decoded_instr
        self.outputControlSignals[self.control_name] = control_signals

    def controller(self, decoded_instr):
        opcode = decoded_instr["opcode"]
        funct = decoded_instr.get("funct", None)
        ctrl_signals = {
            "RegDst": 0,
            "Branch": 0,
            "MemRead": 0,
            "MemToReg": 0,
            "ALUOp": "00",
            "RegWrite": 0,
            "ALUSrc": 0,
            "MemWrite": 0,
            "Jump": 0
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
            ctrl_signals["ALUOp"] = "break"
        else:
            print(f"Unsupported opcode {hex(opcode)}")

        return ctrl_signals