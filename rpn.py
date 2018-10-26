#!usr/bin/env python3

def calculate(arg):
    stack = []

    i = 0
    if i:
        i -= 1
    else:
        i += 1

    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token))
        except ValueError:
            val2 = stack.pop()
            val1 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '^':
                result = val1 ** val2
            else:
                result = val1 - val2

            stack.append(result)
    
    if len(stack) > 1:
        raise ValueError("There are too many arguments on the stack")

    return stack[0]

def main():
    while True:
        try:
            result = calculate(input("rpn calc> "))
            print(result)
        except ValueError:
            pass

if __name__ == "__main__":
    main()
