# Stacks

## Class

```python
class Register:
    def __init__(self, name):
        self.name = name
        self.value = 0

    def __str__(self):
        return f"{self.name}: {self.value}"

class Flags:
    def __init__(self):
        self.zero = False
        self.carry = False
        self.overflow = False

    def __str__(self):
        return f"FLAGS: Z={int(self.zero)} C={int(self.carry)} O={int(self.overflow)}"

class StackVM:
    def __init__(self, memory_size=256):
        self.registers = {f'R{i}': Register(f'R{i}') for i in range(4)}
        self.acc = Register('ACC')
        self.pc = Register('PC')
        self.sp = Register('SP')
        self.flags = Flags()
        
        self.stack = []
        self.data_memory = [0] * memory_size
        self.program_memory = []
        self.labels = {}
        
    def print_state(self):
        print("\n=== VM State ===")
        for reg in self.registers.values():
            print(reg)
        print(self.acc)
        print(f"PC: {self.pc.value}")
        print(f"SP: {self.sp.value}")
        print(self.flags)
        print(f"Stack: {self.stack}")
        print("==============\n")

    def execute(self, instruction):
        if not instruction:
            return
                
        opcode = instruction[0].upper()
        operands = [op.strip(',') for op in instruction[1:]] if len(instruction) > 1 else []
        
        self.pc.value += 1
        
        if opcode == 'PUSH':
            reg = operands[0]
            value = self.registers[reg].value
            self.stack.append(value)
            self.sp.value += 1
            
        elif opcode == 'POP':
            if self.stack:
                reg = operands[0]
                value = self.stack.pop()
                self.registers[reg].value = value
                self.sp.value -= 1
                
        elif opcode == 'PEEK':
            if self.stack:
                print(f"Top of stack: {self.stack[-1]}")
  
        self.pc.value += 1
        
        if opcode == 'MOV':
            dest, source = operands
            if source.startswith('[') and source.endswith(']'):
                addr = int(source[1:-1])
                self.registers[dest].value = self.data_memory[addr]
            elif dest.startswith('[') and dest.endswith(']'):
                addr = int(dest[1:-1])
                self.data_memory[addr] = self.registers[source].value
            elif source.startswith('R'):
                self.registers[dest].value = self.registers[source].value
            else:
                self.registers[dest].value = int(source)
                
        elif opcode in ['ADD', 'SUB', 'MUL', 'DIV', 'AND', 'OR', 'XOR']:
            r1, r2 = operands
            val1 = self.registers[r1].value
            val2 = self.registers[r2].value
            
            if opcode == 'ADD':
                result = val1 + val2
            elif opcode == 'SUB':
                result = val1 - val2
            elif opcode == 'MUL':
                result = val1 * val2
            elif opcode == 'DIV':
                result = val1 // val2 if val2 != 0 else 0
            elif opcode == 'AND':
                result = val1 & val2
            elif opcode == 'OR':
                result = val1 | val2
            elif opcode == 'XOR':
                result = val1 ^ val2
                
            self.acc.value = result
            self.flags.zero = (result == 0)
            self.flags.overflow = (result > 255)
            self.flags.carry = (result > 255)
            
        elif opcode == 'CMP':
            r1, r2 = operands
            result = self.registers[r1].value - self.registers[r2].value
            self.flags.zero = (result == 0)
            self.flags.carry = (result < 0)
            
        elif opcode == 'JMP':
            label = operands[0]
            if label in self.labels:
                self.pc.value = self.labels[label]
                
        elif opcode in ['JZ', 'JNZ']:
            label = operands[0]
            if ((opcode == 'JZ' and self.flags.zero) or 
                (opcode == 'JNZ' and not self.flags.zero)):
                if label in self.labels:
                    self.pc.value = self.labels[label]
                    
        elif opcode == 'CALL':
            addr = int(operands[0])
            self.stack.append(self.pc.value)
            self.pc.value = addr
            
        elif opcode == 'RET':
            if self.stack:
                self.pc.value = self.stack.pop()
                
        self.print_state()



class Instruction:
    def __init__(self, opcode, operands=None):
        self.opcode = opcode
        self.operands = operands or []
        
    def __str__(self):
        return f"{self.opcode} {' '.join(map(str, self.operands))}"

class Program:
    def __init__(self):
        self.instructions = []
        self.labels = {}
        
    def add_instruction(self, instruction):
        self.instructions.append(instruction)
        
    def add_label(self, label, position):
        self.labels[label] = position

class Assembler:
    def __init__(self):
        self.program = Program()
        
    def parse_line(self, line):
        parts = line.strip().split()
        if not parts or line.startswith(';'):
            return None
            
        if parts[0].endswith(':'):
            label = parts[0][:-1]
            self.program.add_label(label, len(self.program.instructions))
            parts = parts[1:]
            
        if parts:
            return Instruction(parts[0], parts[1:])
        return None
        
    def assemble(self, source):
        lines = source.split('\n')
        for line in lines:
            instruction = self.parse_line(line)
            if instruction:
                self.program.add_instruction(instruction)
        return self.program

vm = StackVM()

program = """
    MOV R0, 10
    MOV R1, 20
    PUSH R0
    PUSH R1
    ADD R0, R1
    CMP R0, R1
    JZ equal 
    MOV R2, 30 
equal:
    POP R3 
    POP R2
    MOV R3, 40
"""


instructions = [line.strip().split() for line in program.splitlines() if line.strip()]
for i, inst in enumerate(instructions):
    if inst[0].endswith(':'):
        vm.labels[inst[0][:-1]] = i
        instructions[i] = inst[1:]

for instruction in instructions:
    if instruction:
        vm.execute(instruction)
```