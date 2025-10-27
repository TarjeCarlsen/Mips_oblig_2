
from cpuElement import CPUElement

class Controller(CPUElement):

    def connect(self, input, outputValueNames, control, outputSignalNames):
        return super().connect(input, outputValueNames, control, outputSignalNames)
    

    def controller(decoded_instr):
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
            "Jumo": 0
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
            ctrl_signals["AluSrc"] = 1
            ctrl_signals["MemRead"] = 1
            ctrl_signals["MemToReg"] = 1
            ctrl_signals["ALUOp"] = "lw"
        elif opcode == 0x2B:
            ctrl_signals["AluSrc"] = 1
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