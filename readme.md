# FSym
FSym, short for Face Symbols (because I don't like the word 'emoticon' xD), is a work in progress stack-based esolang. Created solely for the purpose of seeing if I can create my own language... :p

## Commands
Command | Description
------------ | -------------
:) | Pop the top item from the stack and returns the value
;) | Swaps top two items in the stack
:& | Pop top two items in stack, adds them, then pushes result to stack
:S | Pop top two items in stack,  subtracts the first by the second, then pushes result to stack
:3 | Pop top two items in stack, multiplies them, then pushes result to stack
:/ | Pop top two items in stack, divides the first by the second, then pushes result to stack
xD | Pop top item in stack, not's it, then pushes result to stack
x3 | Pop top two items in stack, and's them, then pushes result to stack
xP | Pop top two items in stack, or's them, then pushes result to stack
:p | Loops while top item in stack is true (not 0)
:d | Ends while loop
:D | Push 1 to stack
:o | Pop top item in stack and print as int
:@ | Pop top item in stack and print as ASCII character
:# | Print every item in the stack


You can push a number/character/ASCII code to the stack without using any of the commands. The stack only stores single character codes so strings (e.g. "hello") can't be pushed in one command.


## Examples
### Hello World!
```! d l r o W 32 o l l e H 12 :p ;) :@ :D ;) :S :d```