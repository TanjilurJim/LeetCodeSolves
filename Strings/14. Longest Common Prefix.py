def longestCommonPrefix(strs):
    if not strs: #meaning if the list has no strings
        return ""

    #picking the first string as reference

    prefix = strs[0]

    #step 2: loop through the rest of the strings

    for s in strs[1:]:

        #step3: compare prefix with each string, character by character

        i = 0
        while i< len(prefix) and i < len(s) and prefix[i] == s[i]:
            i+=1

            #step4: cut prefix down to the matched portion


        prefix = prefix[:i]

            #step 5: if prefix becomes empty, no need to continue
        if prefix == "":
            return ""

    return prefix


strrr = ['flowers', 'flow', 'flour']

print(longestCommonPrefix(strrr))
