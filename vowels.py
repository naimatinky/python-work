def my_Vowels(stringInput):
    vowels = ['a', 'e', 'i', 'o', 'u']
    listFoundVowels = []
    StringChars = set()
    DuplicatedChars = set()

    try:
        stringInput = stringInput.replace(' ', '')

        for each in stringInput:
            if (each in vowels and each not in listFoundVowels):
                listFoundVowels.append(each)
            if(each in StringChars):
                DuplicatedChars.add(each)
            else:
                StringChars.add(each)

            stringvoweltuple = ''.join(tuple(listFoundVowels))
        return (stringvoweltuple, len(DuplicatedChars))
    except TypeError:
        return("Invalid input")

print(my_Vowels('dahdah'))
print(my_Vowels('drink water')) 
                              

    
