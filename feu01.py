import sys

def order_operation(operation):
    if "(" in operation:
        calcul = []
        first_parenthese = 0
        last_parenthese = 0
        for i in range(len(operation)):
            if operation[i] == "(":
                first_parenthese = i
            elif operation[-i] == ")":
                last_parenthese = i
            elif first_parenthese != 0 and last_parenthese != 0:
                break
        calcul.extend(operation[:first_parenthese])
        calcul.extend(order_operation(operation[first_parenthese + 1:-last_parenthese]))
        calcul.extend(operation[-(last_parenthese-1):])
        operation = calcul.copy()
    if "%" in operation:
        operation = modulo(operation)
    if "*" in operation:
        operation = multiplication(operation)
    if "/" in operation:
        operation = division(operation)
    if "-" in operation:
        operation = soustraction(operation)
    if "+" in operation:
        operation = addition(operation)

    return operation

def modulo(operation):
    result = []
    for i in range(len(operation)):
        if operation[i] == "%":
            result.extend(operation[:i-1])
            result.append(float(operation[i-1]) / 100)
            result.extend(operation[i+1:])
            break
    return result

def division(operation):
    result = []
    for i in range(len(operation)):
        if operation[i] == "/":
            result.extend(operation[:i-1])
            result.append(float(operation[i-1]) / float(operation[i+1]))
            result.extend(operation[i+2:])
            break
    return result

def multiplication(operation):
    result = []
    for i in range(len(operation)):
        if operation[i] == "*":
            result.extend(operation[:i-1])
            result.append(float(operation[i-1]) * float(operation[i+1]))
            result.extend(operation[i+2:])
            break
    return result

def addition(operation):
    result = []
    for i in range(len(operation)):
        if operation[i] == "+":
            result.extend(operation[:i-1])
            result.append(float(operation[i-1]) + float(operation[i+1]))
            result.extend(operation[i+2:])
            break
    return result

def soustraction(operation):
    result = []
    for i in range(len(operation)):
        if operation[i] == "-":
            result.extend(operation[:i-1])
            result.append(float(operation[i-1]) - float(operation[i+1]))
            result.extend(operation[i+2:])
            break
    return result

if __name__ == "__main__":
    operation = sys.argv[1].split()
    while len(operation) != 1:
        operation = order_operation(operation)
    print(float(operation[0]))
