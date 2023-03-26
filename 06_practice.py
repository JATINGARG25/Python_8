# This is a strip function

#this = "    Jatin is a good boy    "
# print(this)
# print(this.strip())

def remove(string, word):
    new = string.replace(word, "")
    return new.strip()

a = "    jatin is a good boy    "
n = remove(a, "jatin")
print(n)
