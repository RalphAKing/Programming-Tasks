# Stacks

## Task Description
Create a virtual machine that operates using both stack and registers to execute assembly-style instructions.

## Requirements

### Registers
- General Purpose Registers: R0-R3
- Accumulator (ACC): Primary register for arithmetic
- Program Counter (PC): Tracks current instruction
- Stack Pointer (SP): Points to top of stack
- Status Register (FLAGS): Stores condition flags (Zero, Carry, Overflow)

### Core Instructions
1. Register Operations
   - MOV Rx, value    : Move immediate value to register
   - MOV Rx, Ry      : Copy between registers
   - LOAD Rx, [addr] : Load from memory address
   - STORE [addr], Rx: Store to memory address

2. Stack Operations
   - PUSH Rx    : Push register to stack
   - POP Rx     : Pop stack to register
   - PEEK       : View top of stack

3. Arithmetic/Logic
   - ADD Rx, Ry : Add registers
   - SUB Rx, Ry : Subtract registers
   - MUL Rx, Ry : Multiply registers
   - DIV Rx, Ry : Divide registers
   - AND Rx, Ry : Bitwise AND
   - OR Rx, Ry  : Bitwise OR
   - XOR Rx, Ry : Bitwise XOR

4. Control Flow
   - JMP label  : Unconditional jump
   - JZ  label  : Jump if zero
   - JNZ label  : Jump if not zero
   - CMP Rx, Ry : Compare registers
   - CALL addr  : Function call
   - RET        : Return from call

### Memory Model
- Program memory space
- Data memory space
- Stack memory space

### Run reqirements
- Should be able to run the following program

```python
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
```

## Testing Requirements
- Register state verification
- Memory access validation
- Instruction execution accuracy
- Flag operations testing
- Stack boundary checking

## Advanced Features
- Interrupt handling
- Memory protection
- Instruction pipelining
- Micro-instruction support
