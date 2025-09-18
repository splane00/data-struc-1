"""
Samantha Lane
Data Structures Lab 1

"""

# Custom stack class 
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
# Function to check if character is an operator
def is_operator(ch):
    return ch in "+-*/$^"


# Function to convert prefix to postfix using custom stack
def prefix_to_postfix(expression):
    stack = Stack()
    # Process each character from right to left
    for ch in reversed(expression.strip()):
        if ch.isspace():
            continue
        elif is_operator(ch):
            if stack.size() < 2:
                raise ValueError("Invalid expression: insufficient operands.")
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(op1 + op2 + ch)
        else:
            stack.push(ch)
    if stack.size() != 1:
        raise ValueError("Invalid expression: leftover items on stack.")
    return stack.pop()


# Driver code
if __name__ == "__main__":
    input_file = input("Enter input filename: ")
    output_file = input("Enter output filename: ")

    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                if not line.strip():
                    continue
                try:
                    postfix = prefix_to_postfix(line)
                    print(f"Postfix: {postfix}")
                    outfile.write(postfix + "\n")
                except ValueError as e:
                    print(f"Error: {e}")
                    outfile.write("ERROR: Invalid expression\n")
    except FileNotFoundError:
        print("ERROR: File not found.")