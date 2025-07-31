import re

with open('data/input.txt', 'r') as f:
    instructions = f.read().splitlines()
    
def parse_instructions(instructions):
    wires = {}
    for line in instructions:
        lhs, rhs = line.split('->')
        wires[rhs.strip()] = lhs.strip()
    return wires
    
def get_signal(wire, wires, cache):
    if wire.isdigit():
        return int(wire)
    if wire in cache:
        return cache[wire]
    expr = wires[wire]
    tokens = expr.split()
    if len(tokens) == 1:
        val = get_signal(tokens[0], wires, cache)
    elif "AND" in tokens:
        val = get_signal(tokens[0], wires, cache) & get_signal(tokens[2], wires, cache)
    elif "OR" in tokens:
        val = get_signal(tokens[0], wires, cache) | get_signal(tokens[2], wires, cache)
    elif "LSHIFT" in tokens:
        val = (get_signal(tokens[0], wires, cache) << int(tokens[2])) & 0xFFFF
    elif "RSHIFT" in tokens:
        val = (get_signal(tokens[0], wires, cache) >> int(tokens[2])) & 0xFFFF
    elif "NOT" in tokens:
        val = (~get_signal(tokens[1], wires, cache)) & 0xFFFF
    else:
        raise ValueError(f"Unknown instruction: {expr}")
    cache[wire] = val
    return val

instructions = ['956 -> b'] + instructions

wires = parse_instructions(instructions)
cache = {}
output = get_signal('a', wires, cache)