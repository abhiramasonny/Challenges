def group_anagrams(strs):
    anagrams = {}
    
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams:
            anagrams[sorted_word] = [word]
        else:
            anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))  
