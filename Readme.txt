Used Python Version - 3.10.1

# /* explain what the program is doing . . . 
# : It reads input from the user and performs algorithm to interpret the command and output the result accordingly.
# 
# Decisions that I have made
# 1. To print double-quotes inside a string, type '\@'. For example - ("Hello \@Wrold\@") will print out as (Hello "World")
# 2. Until ';' is reached, interpreter will not perform any task. It will keep read user input until ';' is typed.
#    If it reaches semi-colon, interperter will perform the task accordingly and if the command is invalid it will print out
#   error message to infrom the user.
# 3. In this program words are sperated by a space*/

Requirements:
The interpreter must read input from the standard input (stdin) and write output to the standard output (stdout)
and should read statements from the user one at a time and perform the associated action immediately. If invalid input
is provided, the interpreter should attempt to recover and try to provide as useful an error message as possible.
The grammar for the strings processing language is given below:
program := { statement }
statement := 'append' identifier expression ';'
| 'list' ';'
| 'exit' ';'
| 'print' expression ';'
| 'printlength' expression ';'
| 'printwords' expression ';'
| 'printwordcount' expression ';'
| 'set' identifier expression ';'
| 'reverse' identifier ';'
expression := value { '+' value }
value := identifier | constant | literal
constant := 'SPACE' | 'TAB' | 'NEWLINE'
literal := '"' { letter | digit | punctuation } '"'
identifier := letter { letter | digit }
letter := 'A' | 'B' | ... | 'Z' | 'a' | 'b' | ... | 'z'
digit := '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
punctuation := '.' | ',' | ':' | ';' | '?' | '!' | '"' | ...
The intended behavior of each instruction is given in the following table:
Command Parameters Behaviour
append identifier expression Evaluate the expression and append it to the contents of the variable.
list List all variables and their contents.
exit Exit the interpreter
print expression Evaluate and print the expression
printlength expression Evaluate the expression and print its length
printwords expression Evaluate the expression and print the individual words
printwordcount expression Evaluate the expression and print the number of words
set identifier expression Set (create if necessary) the contents of the variable to the expression
reverse identifier Reverse the order of the words in the contents of the variable.