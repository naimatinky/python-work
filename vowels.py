from collections import OrderedDict
def vowels(word):
    vowel = ['a','e','i','o','u']
    list_word = list(word)
    new_list = [char for char in list_word if char in vowel]
    tuple1 =tuple(new_list)
    remove_duplicates="".join(OrderedDict.fromkeys(tuple1))
    get_unique_vowels_tuple =(remove_duplicates,)
    get_dup1_char=[ letter for letter in word.count(letter)>1]
    get_unique_char="".join(OrderedDict.fromkeys(get_dup1_char))
    tuple_dup=tuple(get_unique_char)
    count_tuple_dup=len(tuple_dup)
    count_tuple_dup_final=(count_tuple_dup,)
    combine_tuple=get_unique_vowels_tuple + count_tuple_dup_final
    print(combine_tuple)
    
word="viviandoreen"
    
vowels(word)
                              

    
