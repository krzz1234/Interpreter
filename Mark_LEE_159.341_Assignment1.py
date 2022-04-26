# /* Lee, Mark, 08493227, Assignment number 1, 159.341 */

# /* explain what the program is doing . . . 
# : It reads input from the user and performs algorithm to interpret the command and output the result accordingly.
# 
# Decisions that I have made
# 1. To print double-quotes inside a string, type '\@'. For example - ("Hello \@Wrold\@") will print out as (Hello "World")
# 2. Until ';' is reached, interpreter will not perform any task. It will keep read user input until ';' is typed.
#    If it reaches semi-colon, interperter will perform the task accordingly and if the command is invalid it will print out
#   error message to infrom the user.
# 3. In this program words are sperated by a space*/


from logging import exception


print("----------------------------------------")
print(" 159.341 Assignment 1 Semester 1 2022 ")
print(" Submitted by: Mark Lee, 08493227 ")
print("----------------------------------------")


i = 0
identifier = []
expression = []
temp_expression = []

# Checks whether the identifier is already set as a variable.
# Returns 'True' if it already been assigned a value, otherwise return 'False'
def identifier_Checker(command):
    varaible_exist = False
    for x in identifier:
        if x == command:
            varaible_exist = True
            break

    return varaible_exist

# Removes semi-colon from end of the user-input
def remove_Colon():
    remove_colon = line[:-1]
    command = remove_colon.split()
    global txt
    txt = remove_colon.split("\"")
    return command

# First check if the identifer is already assigned a value, if it's already been assigned new value will be overwritten
# otherwise make a new variable
def set_Variable():
    varaible_exist = identifier_Checker(command[1])
    temp = "".join(txt[1:-1])
    result = temp.replace("\@", "\"")
    if(varaible_exist):
        indx = identifier.index(command[1])
        expression[indx] = result
    else:
        identifier.append(command[1])
        expression.append(result)

# Reads user-input and convert into list of strings
def read_Command():
    global str
    global line
    str = ""
    line = ""
    endOfStr = str.endswith(";")
    while(endOfStr != True):
        str = input()
        line += str
        line += "\n"
        endOfStr = str.endswith(";")
    line = line[:-1]
    global command
    command = line.split()
    global semi_colon
    semi_colon = str.endswith(";")

# checks for semi_colon, if 'exit' is typed it will terminate the program.
def check_Semicolon():
    if(semi_colon == True):
        if(command[0] == "exit" or command[0] == "exit;"):
            print("Exiting Interpreter. Goodbye.")
            exit(0)

    if(semi_colon == False):
        print("ERROR: Missing a semi-colon, please type it again")

# Performs the main algorithm
def parse(command):
    command = remove_Colon()
    # 'set' command
    if(command[0] == "set"):
        try:
            if(command[1].isidentifier()):
                if(command[2].isidentifier()):
                    identifier.append(command[1])
                    expression.append("")
                    temp = ' '.join(command[-1:])
                    temp_var = command[1]
                    while(temp != temp_var):
                        if(temp.isidentifier()):
                            if(temp == "NEWLINE"):
                                command.pop()
                                command.pop()
                                last_var = ''.join(command[-1:])
                                indx = identifier.index(last_var)
                                temp1 = ''.join(expression[indx])
                                temp_expression.append("\n")
                                temp_expression.append(temp1)
                                command.pop()
                                last_var = ''.join(command[-1:])
                                temp = last_var

                            if(temp == "TAB"):
                                command.pop()
                                command.pop()
                                last_var = ''.join(command[-1:])
                                indx = identifier.index(last_var)
                                temp1 = ''.join(expression[indx])
                                temp_expression.append("\t")
                                temp_expression.append(temp1)
                                command.pop()
                                last_var = ''.join(command[-1:])
                                temp = last_var

                            if(temp == "SPACE"):
                                command.pop()
                                command.pop()
                                last_var = ''.join(command[-1:])
                                indx = identifier.index(last_var)
                                temp1 = ''.join(expression[indx])
                                temp_expression.append(" ")
                                temp_expression.append(temp1)
                                command.pop()
                                last_var = ''.join(command[-1:])
                                temp = last_var

                            if(temp.isidentifier() and temp != temp_var):

                                last_var = ''.join(command[-1:])
                                indx = identifier.index(last_var)
                                temp1 = ''.join(expression[indx])
                                temp_expression.append(temp1)
                                command.pop()
                                last_var = ''.join(command[-1:])
                                temp = last_var

                        elif(temp == "+"):
                            command.pop()
                            last_var = ''.join(command[-1:])
                            temp = last_var

                    indx = identifier.index(temp_var)
                    temp_expression.reverse()
                    for x in temp_expression:
                        expression[indx] += x

                else:
                    set_Variable()
        except:
            print("ERROR: Please enter valid input")    

    # 'print' command
    elif(command[0] == "print"):
        try:
            indx = identifier.index(command[1])
            print(expression[indx])
        except:
            print("ERROR: Please enter valid input")

    # 'append' command
    elif(command[0] == "append"):
        try:
            varaible_exist = identifier_Checker(command[1])
            if(varaible_exist):
                if(command[2].isidentifier()):
                    temp = ' '.join(command[-1:])
                    temp_var = command[1]
                    while(temp != temp_var):
                        if(temp.isidentifier()):
                            if(temp == "NEWLINE"):
                                command.pop()
                                command.pop()
                                last_var = ''.join(command[-1:])
                                indx = identifier.index(last_var)
                                temp1 = ''.join(expression[indx])
                                temp_expression.append("\n")
                                temp_expression.append(temp1)
                                command.pop()
                                last_var = ''.join(command[-1:])
                                temp = last_var

                            if(temp == "TAB"):
                                command.pop()
                                command.pop()
                                last_var = ''.join(command[-1:])
                                indx = identifier.index(last_var)
                                temp1 = ''.join(expression[indx])
                                temp_expression.append("\t")
                                temp_expression.append(temp1)
                                command.pop()
                                last_var = ''.join(command[-1:])
                                temp = last_var

                            if(temp == "SPACE"):
                                command.pop()
                                command.pop()
                                last_var = ''.join(command[-1:])
                                indx = identifier.index(last_var)
                                temp1 = ''.join(expression[indx])
                                temp_expression.append(" ")
                                temp_expression.append(temp1)
                                command.pop()
                                last_var = ''.join(command[-1:])
                                temp = last_var

                            if(temp.isidentifier() and temp != temp_var):

                                last_var = ''.join(command[-1:])
                                indx = identifier.index(last_var)
                                temp1 = ''.join(expression[indx])
                                temp_expression.append(temp1)
                                command.pop()
                                last_var = ''.join(command[-1:])
                                temp = last_var

                        elif(temp == "+"):
                            command.pop()
                            last_var = ''.join(command[-1:])
                            temp = last_var
                
                    indx = identifier.index(temp_var)
                    temp_expression.reverse()
                    for x in temp_expression:
                        expression[indx] += x   
                    temp_expression.clear()     
            
                else:
                    list = command[2:]
                    temp = ' '.join(list)
                    temp2 = temp.split("\"")
                    temp = ''.join(temp2)
                    indx = identifier.index(command[1])
                    expression[indx] += temp
            else:
                print("ERROR: Variable not found")
                    
        except:
            print("ERROR: Please enter valid input")

    # 'list' command
    elif(command[0] == "list"):
        try:
            i = 0
            identifier_List = len(identifier)
            print(f"Identifier list ({identifier_List}):")
            while(identifier_List > 0):
                print(f"{identifier[i]}: \"{expression[i]}\"")
                i += 1
                identifier_List -= 1
        except:
            print("ERROR: Please enter valid input")

    # 'printlength' command
    elif(command[0] == "printlength"):
        try:
            varaible_exist = identifier_Checker(command[1])
            if(varaible_exist):
                indx = identifier.index(command[1])
                length = len(expression[indx])
                print(f"Length is: {length}")
            else: 
                print("ERROR: Variable not found")
        except:
            print("ERROR: Please enter valid input")

    # 'printwords' command
    elif(command[0] == "printwords"):
        try:
            word = ""
            print("Words are:")
            varaible_exist = identifier_Checker(command[1])
            if(varaible_exist):
                indx = identifier.index(command[1])
                for x in expression[indx]:
                    if(x != " "):
                        word += x
                    else:
                        print(word)
                        word = ""
                print(word)
            else:
                print("ERROR: Variable not found")
        except:
            print("ERROR: Please enter valid input")

    # 'printwordcount' command
    elif(command[0] == "printwordcount"):
        try:
            word_List = []
            word = ""
            varaible_exist = identifier_Checker(command[1])
            if(varaible_exist):
                indx = identifier.index(command[1])
                for x in expression[indx]:
                    if(x != " "):
                        word += x
                    else:
                        word_List.append(word)
                        word = ""
                print(f"Wordcount is: {len(word_List)+1}")
            else:
                print("ERROR: Variable not found")
        except:
            print("ERROR: Please enter valid input")

    # 'reverse' command
    elif(command[0] == "reverse"):
        try:
            varaible_exist = identifier_Checker(command[1])
            if(varaible_exist):
                indx = identifier.index(command[1])
                temp = expression[indx].split()
                temp.reverse()
                rev = " ".join(temp)
                expression[indx] = rev
            else:
                print("ERROR: Variable not found")
        except:
            print("ERROR: Please enter valid input")

    # 'Error message'
    else:
        print("ERROR: Please enter valid input")


while(1):
    read_Command()
    check_Semicolon()
    parse(command)
    i += 1
