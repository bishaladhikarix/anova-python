started = False
helpc = False
i = ""
while True:
    i = input('Enter the command or enter help to see the list of command avalilable to you ')

    if   i.upper() == 'HELP':
        if helpc:
            print('you can only use that command once you idiot!!')
        else:
            helpc = True
            print('START , STOP , QUIT')


    elif i.upper() == 'START':
        if started:
            print('car is already started!!')
        else:
            started = True
            print("your car has been started and running at the speed of 45 km/h")


    elif i.upper() == 'STOP':
        if not started:
            print('your car is already stopped')
        else:
            started = False
            print("your car has been stopped.")

    elif i.upper() == 'QUIT':
        break

    else:
        print('invalid command')

