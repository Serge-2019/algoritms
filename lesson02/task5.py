code = 32
while code <= 127:
    print(f'{code:5d}-{chr(code)}', end=' ')
    if (code-31) % 10 == 0:
        print()
    code += 1
