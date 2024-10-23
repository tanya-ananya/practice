'''Use a stack to check if the parentheses in a string are valid'''

def check_parenthesis(string):
    open_paren = ['(', '[', '{']
    close_paren = [')', ']', '}']
    s = Stack()
    for x in string:
        if x in open_paren:
            s.push(x)
        elif x in close_paren:
            if s.is_empty() == True:
                return None

        top = s.pop()
        if open_paren.index(top) != close_paren.index(x):
            return False
        
    return s.is_empty()