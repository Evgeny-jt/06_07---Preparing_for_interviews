from stack import Stack

if __name__ == '__main__':
    stack_1 = Stack()


    action = input('''
    выбирите действие:
    проверка, добавить, удалить, вернуть, количество
    или нажмите Enter для завершения программы
    ''')
    while action != '':

        if action == 'проверка':
            print(stack_1.is_empty())
        elif action == 'добавить':
            stack_1.push()
        elif action == 'удалить':
            stack_1.pop()
        elif action == 'вернуть':
            print(stack_1.peek())
        elif action == 'количество':
            print(stack_1.size())
        else:
            print('Команда не распознана')

        action = input('''
            выбирите действие:
            проверка, добавить, удалить, вернуть, количество
            или нажмите Enter для завершения программы
            ''')