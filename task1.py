good = """
            (_)
            .-'-.
            |   |
            |   |
            |   |
            |   |
        __|   |__   .-.
       .-'  |   |  `-:   :
      :     `---'     :-'
       `-._       _.-
"""
bad = r"""          
                            ,___
                            |---.\
              ___        |     `
             /   .- \    ./=)
            |   | " |_/\/|
            ;   | - ;| /_ |
           /  \_|   |/ \  |
          /           \/\(  |
          |    /      |` ) |
          /      \  _/     |
        /--._/   \         |
       `/|)       |        /
           /        |       |
         .'          |       |
        /             \     |
      (_.-.__.__./    /
"""
torch_lit = True
if torch_lit:
    outcome = "Flicker: You can see within the dark from the warmth of the torch"
    print(good)
else:
    outcome = "Doom: The shadows are closing around you"
    print(bad)
print(outcome)
