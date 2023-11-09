#check in python interpreter/console(ALT + SHIFT + E) met 'dir(data-type) voor beschikbare methods vh object
# bijvoorbeeld
# dir(str)
# dir(list)
# dir([object])
# dir(variablename)

# methods per datatype
    #met de help() function zoeken op omschrijving method:
        #help('data'/data-type.method zonder ())

user_prompt = "Enter a todo:"

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo)
    print(todos)

#voor list met functions:
    'import builtins'
# om te zoeken in beschikbare functions(kleine letters in command)
    'dir(builtins)'
# builtins als argument

