def palindrome(word, idx, left_idx=-1):
    if idx == len(word)//2:
        return f"{word} is a palindrome"

    if word[idx] == word[left_idx]:
        return palindrome(word, idx+1, left_idx-1)

    else:
        return f"{word} is not a palindrome"
