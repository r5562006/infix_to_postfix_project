class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "堆疊是空的"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "堆疊是空的"

    def is_empty(self):
        return len(self.stack) == 0

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    postfix = []

    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedence[char] <= precedence[stack.peek()]):
                postfix.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)

# 使用示例
if __name__ == "__main__":
    infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
    print(f"中序表達式 {infix_expression} 的後序表達式：", infix_to_postfix(infix_expression))