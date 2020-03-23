run=1
while run:
    # Take a binary number from user
    binary = int(input(" : "))
    # Create a list by using map
    binary_list = list(map(int, str(binary)))
    # Find length of list -1 because the count starts from 0
    a = len(binary_list) - 1
    nr = 0
    nr_listes = 0


    # converter function
    def converter():
        global a, binary_list, nr, nr_listes
        while a >= 0:
            if binary_list[nr_listes] == 1:
                nr = nr + (2 ** a)
                a = a - 1
                nr_listes = nr_listes + 1
            else:
                a = a - 1
                nr_listes = nr_listes + 1


    converter()
    print(nr)