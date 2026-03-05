good = """
   ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..jb
 (this is a fire)"""
bad = """
                                   ,/
                                 ,'/
                               ,' /
                             ,'  /_____,
                           .'____     ,'   
                                   /   ,'
                                  /  ,'
                                 / ,'
                                / '
"""
drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: Its strike flames the wooden walkway as you passed"
    print(good)
else:
    outcome = "Doom: The rage of the sky burnt your body"
    print(bad)
print(outcome)