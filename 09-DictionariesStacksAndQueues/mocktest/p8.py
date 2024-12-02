
def f(expression): 
  # splitting expression at whitespaces 
  expression = expression.split() 
    
  # stack 
  stack = [] 
    
  # iterating expression 
  for ele in expression: 
    
    # ele is a number 
    if ele not in '/*+-': 
      stack.append(int(ele)) 
      
    # ele is an operator 
    else: 
      # getting operands 
      right = stack.pop() 
      left = stack.pop() 
        
      # performing operation according to operator 
      if ele == '+': 
        stack.append(left + right) 
          
      elif ele == '-': 
        stack.append(left - right) 
          
      elif ele == '*': 
        stack.append(left * right) 
          
      elif ele == '/': 
        stack.append(int(left / right))
    
  # return final answer. 
  return stack.pop() 

if __name__=='__main__':
    print(f("2 3 +"))
    print(f("2 6 + 4 5 - +"))
    print(f("11 7 + 15 - 14 +"))