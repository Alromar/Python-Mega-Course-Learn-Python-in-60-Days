# variable string
user_message = 'Enter a todo:'
# variable output
# niet gebruiksvriendelijk: bij iedere todo moet er een inputfunction worden geschreven
# de gebruiker moet de hoeveelheid input functions kunnen bepalen

# batchbewerking

todos = []

while True:
    # 4 keer spatie onder de condition

    todo = input(user_message)
    # koppel de variabelen met de method 'append'
    # ieder object/data-type heeft eigen method
    # bijv
    # todo.append()
    # todo data-type=string heeft geen append-methode
    # todo.capitalize kan wel
    print(todo.title())
    todos.append(todo)
    # print(todos)
    # todos = [todo]
    # # todos overschrijft todo
    # print(todos)

# todo2 = input(user_message)
# todo3 = input(user_message)

# list is een variabele om meerdere objecten in op te slaan
# variable list
# todos = [todo1, todo2, todo3, "Hello"]
# output
# print(todos)

# type var string
# print(type(user_message))
# print(type(todos))
# print(type(todo1))
