

def parens_check(text):
    opens = text.count('(')
    closed = text.count(')')
    parens = opens - closed
    if text.find(')') < text.find('('):
        return -1
    elif parens == 0: return 0
    elif parens > 0: return 1
    else: return -1