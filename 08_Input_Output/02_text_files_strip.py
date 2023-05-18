filename = "Jabberwocky.txt"
with open(filename) as f:
    content = f.readline().rstrip()
    
print(content)

chars = "'"
no_apostrophe = content.strip(chars)
print(no_apostrophe)

twas_removed = content.removeprefix("'Twas")
print(twas_removed)
toves_removed = content.removesuffix("toves")
print(toves_removed)
