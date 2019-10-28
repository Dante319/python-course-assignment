def is_anagram(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    x = 0
    m = len(str1)
    n = len(str2)
    if m == n:
        for i in str1:
            if i not in str2:
                x = 1
    else:
        x=1
    if x == 1:
        print("Not anagram")
    else:
        print("Anagram")

is_anagram('baba','abbas')