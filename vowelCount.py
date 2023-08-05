def vowel():
    print("Enter a string: ")
    s = input(" ")
    v = 0

    print("Old String: ", s.upper())
    for i in s:
        if i == "a":
            v = v + 1
            s = s.replace("a", "*")
        elif i == "e":
            v = v+1
            s = s.replace("e", "*")
        elif i == "i":
            v = v + 1
            s = s.replace("i", "*")
        elif i == "o":
            v = v + 1
            s = s.replace("o", "*")
        elif i == "u":
            v = v + 1
            s = s.replace("u", "*")
    print("New String", s.upper())
    print("Number of vowel characters: ", v)
vowel()
