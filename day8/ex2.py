'''
acc increases or decreases a single global value called the accumulator by the value given in the argument. For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0. After an acc instruction, the instruction immediately below it is executed next.
jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction, jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction 20 lines above to be executed next.
nop stands for No OPeration - it does nothing. The instruction immediately below it is executed next.
'''
import re


def run():
    accumulator = 0
    visited = set()
    i = 0
    while i not in visited and i < len(data):
        visited.add(i)
        instr, val = data[i]
        if instr == 'acc':
            accumulator += val
        if instr == 'jmp':
            i += val - 1
        i += 1
    return accumulator, i >= len(data)


with open('input.txt') as f:
    data = re.findall(r'(.+?) ([+-]\d+)', f.read())
    data = [(instr, int(val)) for instr, val in data]

for i in (idx for idx in range(len(data)) if data[idx][0] in ('nop', 'jmp')):
    instr, val = data[i]
    data[i] = 'nop' if instr == 'jmp' else 'jmp', val

    acc, finished = run()
    if finished:
        print("value of the accumulator after the program terminates -",acc)
        break

    data[i] = instr, val 