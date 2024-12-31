"""
Реализована функция balance - проверка сбалансированности скобок.
Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий,
и пары скобок правильно вложены друг в друга.
"""

def balance(prov):
    new_str = ''

    for i, bracket in enumerate(prov):

        if bracket == '(' or bracket == '[' or bracket == '{':
            new_str = new_str + bracket
        elif bracket == ')':
            if new_str != '' and '(' == new_str[-1]:
                new_str = new_str[:-1]
            else:
                return 'Несбалансированно'
        elif bracket == ']':
            if new_str != '' and '[' == new_str[-1]:
                new_str = new_str[:-1]
            else:
                return 'Несбалансированно'
        elif bracket == '}':
            if new_str != '' and '{' == new_str[-1]:
                new_str = new_str[:-1]
            else:
                return 'Несбалансированно'

    if new_str == '':
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

if __name__ == '__main__':
    print(balance('(((([{}]))))'))
    print(balance('[[{())}]'))