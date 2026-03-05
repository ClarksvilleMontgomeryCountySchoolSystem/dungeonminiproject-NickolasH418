good = r"""
        . - ' " ' - . 
      /   #           \ 
     :   #              :     . - ' " ' - . 
       \               /     /   #           \ 
         \           /     :   #               : 
 j g s  ` ' q ' `         \               / 
               (               \           / 
                 )               ` ' p ' ` 
               (                     ) 
                 )                 ( 
                                     )
"""
bad = r"""
                               . 
                 *       .           .       .   
                           .   ( * . )   .         *   . 
                   .     (   . ( . .   )   )     
                 .   . (   ( . . *     ) . * )   .   
                       (   *     .   ) .   . )     . 
                     .     (   ( .   * . )   .   
                              .     .         * 
                       . *               .                       
"""
escaped = True
if escaped:
    outcome = "Legend: You're known but that doesn't mean you live forever"
    print(good)
else:
    outcome = "Doom: You've failed yourself and the spirits, shame"
    print(bad)
print(outcome)