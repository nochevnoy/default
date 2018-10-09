def valid_parentheses(string):
    brackets = []
    for num in string:
        if( num == '(' ):
            brackets.append(num)
        elif( num == ')' ):
            try:
                brackets.pop()
            except:
                return False

    if(len(brackets) == 0):
        return True
    else:
        return False