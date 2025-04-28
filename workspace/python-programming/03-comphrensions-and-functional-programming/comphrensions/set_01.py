word = input("Enter a word")
# Without
unique_chars = set()
for e in word:
    unique_chars.add(e)
print(unique_chars)

# With
unique_chars = {e for e in word}
print(unique_chars)