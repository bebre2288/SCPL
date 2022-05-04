#from sys import argv
#eee,name=argv
source = list(input())
counter = 0.0
#source=open(name,'r').read()

def count(param):
    global source
    if source[0] == "+":
        try:
            if source[1] == "(":
                source.pop(0)
                param += skobki()
            elif source[1] == "<":
                source.pop(0)
                param += loop()
            elif source[1] == "r":
                source.pop(0)
                param += float(input())
            else:
                param += 1
        except:
            param += 1

    elif source[0] == "-":
        try:
            if source[1] == "(":
                source.pop(0)
                param -= skobki()
            elif source[1] == "<":
                source.pop(0)
                param -= loop()
            elif source[1] == "r":
                source.pop(0)
                param -= float(input())
            
            else:
                param -= 1
        except:
            param -= 1

    elif source[0] == "*":
        if source[1] == "=":
            param *= param
            source.pop(0)
        elif source[1] == "+":
            param *= param + 1
            source.pop(0)
        elif source[1] == "-":
            param *= param - 1
            source.pop(0)
        elif source[1] == "(":
            source.pop(0)
            param *= skobki()
        elif source[1] == "<":
            source.pop(0)
            param *= loop()
        elif source[1] == "r":
                source.pop(0)
                param *= float(input())
            
    elif source[0] == "/":
        if source[1] == "=":
            param /= param
            source.pop(0)
        elif source[1] == "+":
            param /= param + 1
            source.pop(0)
        elif source[1] == "-":
            param /= param - 1
            source.pop(0)
        elif source[1] == "(":
            source.pop(0)
            param /= skobki()
        elif source[1] == "<":
            source.pop(0)
            param /= loop()
        elif source[1] == "r":
            source.pop(0)
            param /= float(input())
    return param


def loop():
    global counter
    condition = 0
    tcounter = 0
    answer = 0
    global source
    source.pop(0)
    while 1:
        if source[0] == "}" or len(source) == 0:
            source.pop(0)
            max_condition = tcounter
            break
        tcounter = count(tcounter)
        if source[0] == ";":
            source.pop(0)
            operator = source[0]
            if operator == "*":
                answer=1
        if len(source) != 0:
            source.pop(0)
    tcounter = 0

    while condition < max_condition:
        i = 0
        tcounter = 0
        while 1:
            if source[i] == ">" or len(source) == 0:
                # source.pop(0)
                break

            if source[i] == "+":
                try:
                    if source[i + 1] == "(":
                        tcounter += skobki()
                    else:
                        tcounter += 1

                except:
                    tcounter += 1

            elif source[i] == "-":
                try:
                    if source[i + 1] == "(":
                        tcounter -= skobki()
                    else:
                        tcounter -= 1
                except:
                    tcounter -= 1

            elif source[i] == "*":
                if source[i + 1] == "=":
                    tcounter *= tcounter
                    source.pop(0)
                elif source[i + 1] == "+":
                    tcounter *= tcounter + 1
                    source.pop(0)
                elif source[i + 1] == "-":
                    tcounter *= tcounter - 1
                    source.pop(0)

            elif source[i] == "/":
                if source[i + 1] == "=":
                    tcounter /= tcounter
                    source.pop(0)
                elif source[i + 1] == "+":
                    tcounter /= tcounter + 1
                    source.pop(0)
                elif source[i + 1] == "-":
                    tcounter /= tcounter - 1
                    source.pop(0)

            if len(source) != 0:
                i += 1
        condition += 1
        if operator == "+":
            answer += tcounter
        elif operator == "-":
            answer -= tcounter
        elif operator == "*":
            
            answer *= tcounter
        elif operator == "/":
            answer /= tcounter
    while i != 0:
        source.pop(i)
        i -= 1
    return answer


def skobki():
    global source
    scounter = 0
    while 1:
        if source[0] == ")" or len(source) == 0:
            return scounter
            break
        scounter = count(scounter)
        if len(source) != 0:
            source.pop(0)


def oper():
    global counter
    if source[0] == ",":
        try:
            if source[1] == "d":
                print(conter)
                source.pop(0)
            else:
                print(chr(int(round(counter))))
        except:
            print(chr(int(round(counter))))
        source.pop(0)
        counter=0
    counter = count(counter)


while 1:
    try:
        oper()
        source.pop(0)
    except:
        break

print("final:", counter)
