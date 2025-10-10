text = input("Enter the string: ")
pattern = input("Enter the string to search: ")
n = len(text)
m = len(pattern)
indices = []
for i in range(n - m + 1):
    if text[i:i+m] == pattern:
        indices.append(i)
if indices:
    print(f'Pattern "{pattern}" found at indices: {indices}')
else:
    print(f'Pattern "{pattern}" not found in the text.')
