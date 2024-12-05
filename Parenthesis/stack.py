class Stack:
    def __init__(self, stack, str):
        ctr = 0
        self.stack = stack
        for i in range(len(str)):
            if str[i] == '(' or str[i] == ')':
                if ctr > 0:
                    self.push(str[i-ctr:i])
                self.push(str[i:i+1])
                ctr = 0
                continue
            elif i == len(str) - 1:
                self.push(str[i-ctr:i+1])
            ctr += 1


    def push(self, str):
        self.stack.append(str)

    def pull(self):
        if len(self.stack) == 0:
            return f"END OF STACK({self})"
        else:
            tmp = self.stack[len(self.stack) - 1]
            self.stack.pop(len(self.stack) - 1)
            return tmp
    
    def size(self):
        return len(self.stack)

a = []
new1 = Stack(a, "hello (there)artrtgrr) ")
    