def hex_to_binary(hex):
    result = ''
    HEX = '0123456789ABCDEF'
    BIN = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    HEX_TO_BIN = { char:num for char, num in zip(HEX, BIN) }
    for char in hex:
        result += HEX_TO_BIN[char]
    return result

def read_bits(state, num_bits):
    result = 0
    for i in range(num_bits):
        bit = 1 if state[i] == '1' else 0
        result <<= 1
        result |= bit
    return result, state[num_bits:]

def read_packet(state):
    version, state = read_bits(state, 3)
    type_id, state = read_bits(state, 3)
    if type_id == 4:
        literal = 0
        while True:
            go_on, state = read_bits(state, 1)
            value, state = read_bits(state, 4)
            literal <<= 4
            literal |= value
            if not go_on:
                break
        return version, type_id, literal, state
    else:
        children = []
        length_type_id, state = read_bits(state, 1)
        if length_type_id == 0:
            sub_packet_length_in_bits, state = read_bits(state, 15)
            start_state = state
            while len(start_state) - len(state) < sub_packet_length_in_bits:
                cver, ctyp, cval, state = read_packet(state)
                children.append((cver, ctyp, cval))
        else:
            num_subpackets, state = read_bits(state, 11)
            for i in range(num_subpackets):
                cver, ctyp, cval, state = read_packet(state)
                children.append((cver, ctyp, cval))
        return version, type_id, children, state

def sum_versions(packet):
    version, type_id, children = packet
    if type_id == 4:
        return version
    else:
        sum = version
        for child in children:
            sum += sum_versions(child)
        return sum

def evaluate(packet):
    version, type_id, children = packet
    if type_id == 0:
        return sum(evaluate(child) for child in children)
    elif type_id == 1:
        product = 1
        for child in children:
            product *= evaluate(child)
        return product
    elif type_id == 2:
        return min(evaluate(child) for child in children)
    elif type_id == 3:
        return max(evaluate(child) for child in children)
    elif type_id == 4:
        return children
    else:
        a = evaluate(children[0])
        b = evaluate(children[1])
        if type_id == 5:
            return int(a > b)
        elif type_id == 6:
            return int(a < b)
        else:
            return int(a == b)

with open('day16.txt') as file:
    input = hex_to_binary(file.readline().strip())

root = read_packet(input)
version, type_id, value, _ = root
root = (version, type_id, value)

print('Part 1:', sum_versions(root))
print('Part 2:', evaluate(root))