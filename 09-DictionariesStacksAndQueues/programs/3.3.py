import queue
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

brackets=queue.LifoQueue()
def cdin(n):
    brackets.put(n)

def brackets_ok(expression):
    count=[0,0,0]
    for char in expression:
        if char=='[' or char==']' or char=='(' or char==')' or char=='{' or char=='}':
            if char==']'or char==')'or char=='}':
                bracket = brackets.get()
                if bracket=='[' and char!=']':
                    return False
                elif bracket=='(' and char!=')':
                    return False
                elif bracket=='{' and char!='}':
                    return False
            else:
                cdin(char)
    if brackets.qsize()>0:
        return False
    return True#True if brackets in expression are ok of False otherwise

def test(exp):
    if brackets_ok(exp):
        print("great")
    else:
        print("not great")

test(expression1)
test(expression2)
test(expression3)
