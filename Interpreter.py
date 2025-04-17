def Exc(code):
    cells = [0] * 30000
    ptr = 0
    i = 0
    loop_stack = []

    while i < len(code):
        cmd = code[i]

        if cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
        elif cmd == '+':
            cells[ptr] = (cells[ptr] + 1) % 256
        elif cmd == '-':
            cells[ptr] = (cells[ptr] - 1) % 256
        elif cmd == '.':
            print(chr(cells[ptr]), end='')
        elif cmd == ',':
            cells[ptr] = ord(input("Input a character: ")[0])
        elif cmd == '[':
            if cells[ptr] == 0:
                open_brackets = 1
                while open_brackets:
                    i += 1
                    if code[i] == '[':
                        open_brackets += 1
                    elif code[i] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(i)
        elif cmd == ']':
            if cells[ptr] != 0:
                i = loop_stack[-1]
                continue
            else:
                loop_stack.pop()

        i += 1

with open("main.b", "r", encoding='utf-8') as f: # set main.b as your code's name
    Exc(f.read())
# Bugs may be found, if so please issue a report in https://github.com/Zelpak/BFInterpreter/issues
