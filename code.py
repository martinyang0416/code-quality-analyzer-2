def reverse_consonants(S):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s_list = list(S)
    consonants = []
    
    # Collect all consonants
    for char in s_list:
        if char not in vowels:
            consonants.append(char)
    
    # Reverse the consonants list
    consonants.reverse()
    
    # Replace consonants in the original string with the reversed ones
    ptr = 0
    for i in range(len(s_list)):
        if s_list[i] not in vowels:
            s_list[i] = consonants[ptr]
       