"""
Hеализован класс Stack со следующими методами:
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке.
"""

class Stack:
    def __init__(self):
        self.stack = ''

    def is_empty(self):
        if self.stack == '':
            return False
        else:
            return True

    def push(self):
        symbol = input('введите символ ( { [ ] } ) и нажмите ENTER или нажмите ENTER для возврата')
        if symbol in '(){}[]' and len(symbol) == 1:
            self.stack = symbol + self.stack

    def pop(self):
        if self.stack != '':
            self.stack = self.stack[1:]

    def peek(self):
        if self.stack != '':
            return self.stack[0]

    def size(self):
        # print(self.stack)
        return len(self.stack)


