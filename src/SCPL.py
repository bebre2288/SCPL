program = input()
counter = 0.0
iter = 0

def operate(num):
    global iter
    oper = program[iter]
    if oper=='+':
        num+=1
    elif oper=='-':
        num-=1
    elif oper=='*':
        iter+=1
        num *= operate(num)
    elif oper=='/':
        iter+=1
        num /= operate(num)
    elif oper=='(':
        temp = 0
        while program[iter]!=')':
            iter+=1
            temp = operate(temp)
            num = temp
    elif oper==',':
        print(chr(int(round(counter))))
        num=0
    elif oper=='.':
        num=int(input())
    
    return num


while iter < len(program):
    counter = operate(counter)
    iter+=1


print("final:", counter)

