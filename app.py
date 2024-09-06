import sys

expression = sys.argv[1]

num1, operation, num2 = expression.split()

num1 = float(num1)
num2 = float(num2)

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
else:
    print("Unknown operation. Use '+' or '-'.")
    sys.exit(1)

print(f'Result: {result}')