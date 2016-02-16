#infix expression evaluation

#take two stacks
#1. operatorStack { for operators and parenthesis }
#2. operandStack

#algorithm:

#If character exists to be read:
    
    #1. if character is operand or (. push on the operandStack
    #2. else if character is operator
         #2.1. while the top of the operatorStack is not of smaller precedence than this character
         #2.2. pop from operatorStack
         #2.3. pop two operands from operandStack
         #2.4. store op1 op op2 on the operandStack back to 2.1
    #3. else if character is ) [do the same as 2.2 - 2.4 till you encounter (]

#else // no more character left to read
    #pop operators till operator stack is not empty
    #pop top 2 operands and perform operation op1 op op2 and push result on the operand stack
    #return the top value from operandStack
   
   
def isOp(c):
    if c != "": return (c in "+-*/")
    else: return False

def pri(c): # operator priority
    if c in "+-": return 0
    if c in "*/": return 1
    
def isNum(c):
    if c != "": return (c in "0123456789.")
    else: return False

def calc(op, num1, num2):
    if op == "+": return str(float(num1) + float(num2))
    if op == "-": return str(float(num1) - float(num2))
    if op == "*": return str(float(num1) * float(num2))
    if op == "/": return str(float(num1) / float(num2))

def Infix(expr):
    expr = list(expr)
    stackChr = list() # character stack
    stackNum = list() # number stack
    num = ""
    while len(expr) > 0:
        c = expr.pop(0)
        if len(expr) > 0: d = expr[0]
        else: d = ""
        if isNum(c):
            num += c
            if not isNum(d):
                stackNum.append(num)
                num = ""
        elif isOp(c):
            while True:
                if len(stackChr) > 0: top = stackChr[-1]
                else: top = ""
                if isOp(top):
                    if not pri(c) > pri(top):
                        num2 = stackNum.pop()
                        op = stackChr.pop()
                        num1 = stackNum.pop()
                        stackNum.append(calc(op, num1, num2))
                    else:
                        stackChr.append(c)
                        break
                else:
                    stackChr.append(c)
                    break
        elif c == "(":
            stackChr.append(c)
        elif c == ")":
            while len(stackChr) > 0:
                c = stackChr.pop()
                if c == "(":
                    break
                elif isOp(c):
                    num2 = stackNum.pop()
                    num1 = stackNum.pop()
                    stackNum.append(calc(c, num1, num2))

    while len(stackChr) > 0:
        c = stackChr.pop()
        if c == "(":
            break
        elif isOp(c):
            num2 = stackNum.pop()
            num1 = stackNum.pop()
            stackNum.append(calc(c, num1, num2))

    return stackNum.pop()

if __name__ == "__main__":
    # TEST
    expr = "2+4*5"
    print "EXPR: " + expr
    print "EVAL: " + str(eval(expr))
    print "INFX: " + Infix(expr)

