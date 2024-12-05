import stack

def cmdRec(s, ctr):
    if ctr == 1:
        print(s.stack)
    else:
        prCtr = 0
        cmdCtr = 0
        cmd = ''
        tmp = ''

        while True:
            tmp += s.pull()
            if tmp[len(tmp) - 1] == '(' or tmp[len(tmp) - 1] == ')':
                cmd += tmp[len(tmp) - 1]
                tmp = ''.join([c for c in tmp if c != ')' and c != '('])
                break

        if cmd[len(cmd) - 1] == ')':
            while prCtr > -1 and s.size() > 0:
                cmd += s.pull()
                if cmd[len(cmd) - 1] == ')':
                        prCtr += 1
                elif cmd[len(cmd) - 1] == '(':
                    if prCtr > 0:
                        cmdCtr += 1
                    prCtr -= 1
            else:
                if s.size() == 0:
                    print("ERROR: one ')' is extra")
                    return
                else:
                    char = s.pull()
                    if char == '(':
                        print("ERROR: one '(' is extra")
                        return
                    else:
                        s.push(char)
        elif cmd[len(cmd) - 1] == '(':
            while prCtr > -1 and s.size() > 0:
                cmd += s.pull()
                if cmd[len(cmd) - 1] == '(':
                        prCtr += 1
                elif cmd[len(cmd) - 1] == ')':
                    if prCtr > 0:
                        cmdCtr += 1
                    prCtr -= 1
            else:
                if s.size() != 0:
                    char = s.pull()
                    if char == '(':
                        print("ERROR: one '(' is extra")
                        return
                    else:
                        s.push(char)
        wCount = 0
        if cmd[0] != '(' and cmd[0] != ')':
             for c in cmd:
                if c != '(' and c != ')':
                    wCount += 1
                else:
                    break
        
        nS = []
        cmdRec(stack.Stack(nS, cmd[wCount+1:len(cmd) - 1]), cmdCtr)
        if len(tmp) > 0:
            s.push(tmp)
        print(s.stack)
             

str = input()
s = []
new = stack.Stack(s, str)
print(s)

cmdRec(new, -1)

# cmdList = []
# tmp = ''
# cmdCtr = 0
# cmd = new.pull()
# while cmd != '(' and cmd != ')':
#     cmdList.append(cmd)
#     cmd = new.pull()
# else:
#     if cmd == ')':
#         cmdCtr += 1
#         while cmdCtr > 0:
#             tmp += new.pull()
#             if tmp[len(tmp) - 1] == ')':
#                 cmdCtr += 1
#             elif tmp[len(tmp) - 1] == '(':
#                 cmdCtr -= 1
#                 if cmdCtr == 0:
#                     cmd += tmp

# while len(s) != 0:
#     cmd += new.pull()
# cmdList
# print(cmd)
    #     else:
    #         cmd += new.pull()
    #         cmdList.append(cmd)
    # else:
    #     cmdList.append(cmd)