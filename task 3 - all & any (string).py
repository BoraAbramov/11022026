
words = ["HELLO", "WORLD", "PYTHON", "CODE", "DEVELOPER", "AI"]

#section 1

print(f"all words in the string are use upper letters? {all(bigword.isupper for bigword in words)}")

#section 2

print(f"is there any word with length 5 or more characters? {any(len(oreh) > 5 for oreh in words)}")