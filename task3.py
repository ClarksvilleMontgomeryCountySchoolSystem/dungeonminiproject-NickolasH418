good = r"""
                                !
!                z   ---=^.|
| . . ________z/  _>|
| : : : : : : : : : : : ||  |
"""
bad = r"""
     . - " " " - . 
    /  _       _ \ 
   ]  (_ '   `_) [
    '-.     N    ,-'  
      |           | 
      ` -  -  -  ' 
"""
guard_awake = False
if not guard_awake:
    outcome = "Shadow: Their presence fills you with fear and determination"
    print(good)
else:
    outcome = "Doom: They've found you and now you no longer think"
    print(bad)
print(outcome)
