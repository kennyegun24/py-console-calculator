class Calculator:
    def __init__(self):
        self.answers = []

    def run(self):
        print(self.library_menu())
        user_input = input().strip()

        if user_input <= '3':
            self.options(user_input)
        elif user_input == '4':
            print('Thanks for using the app!')
        else:
            print('Please select an option from 1 - 4')

    def library_menu(self):
        menu = '''
Welcome👋 to Calc App!

Please choose an option by entering a number
1 - List all 10 previous answers
2 - Do some basic arithmethics
3 - Undo
4 - Exit
'''
        return menu

    def back_to_menu(self):
        print('\nPress Enter to go back to menu: ')
        input()
        self.run()

    def list_solutions(self):
        if not self.answers:
            print('No answers available 😔')
            self.back_to_menu()

        print('List of all answers: ')
        for i, answer in enumerate(self.answers):
            print(f"{i}) Answer: {answer['num1']} {answer['operator']} {answer['num2']} = {answer['result']}")
        self.back_to_menu()

    def operate(self):
        title = float(input('First Number: '))
        operator = input('Operator: ').strip()
        second = float(input('Second Number: '))

        if operator == '-':
            solution = title - second
        elif operator == '+':
            solution = title + second
        elif operator == '*':
            solution = title * second
        elif operator == '/':
            solution = title / second

        print(solution)
        self.answers.append({
            'num1': title,
            'num2': second,
            'operator': operator,
            'result': solution
        })
        if len(self.answers) > 10:
            self.answers.pop(0)

        print('Pushed to memory')
        self.back_to_menu()

    def undo(self):
        if not self.answers:
            self.back_to_menu()
        operation = self.answers.pop()
        print(f"Reverted : {operation['num1']} {operation['operator']} {operation['num2']} = {operation['result']}")
        self.back_to_menu()

    def options(self, user_input):
        if user_input == '1':
            self.list_solutions()
        elif user_input == '2':
            self.operate()
        elif user_input == '3':
            self.undo()
        else:
            print('Enter a number between 1 - 4')

app = Calculator()
app.run()
