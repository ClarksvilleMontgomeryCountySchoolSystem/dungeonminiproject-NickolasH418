good = r"""
 ______________
|\ ___________ /|
|  |  /|,| |            | |
|  | |,x,| |            | |
|  | |,x,' |            | |
|  | |,x   ,           |  |
|  | |/    |%==   |  |
|  |    /] ,           |  |
|  |   [/ ()           |  |
|  |       |            |  |
|  |       |            |  |
|  |       |            |  |
|  |      ,'            |  |
|  |   ,'               |  |
|_|,'_________|_| """
bad = r"""
   . - ' ' ' ' '  -  .
  | ' - - - - -  ' |
/ ` - . . . . . - ` \ 
|   < _ }           |
|       . - \ - .     | 
|     / #   `  \    |
|    \            /   |
\       ' - ' - '      /
  ` '  - - - - -  ' ` 
"""
has_key = True
if has_key:
    outcome = "Click: The door's sound fills you with relief"
    print(good)
else:
    outcome = "Doom: You're locked in forever, your stomach becoming nothing"
    print(bad)
print(outcome)