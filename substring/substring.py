word=input()

charset=set()
mod_word=word.lower()

for i in range(0,len(mod_word)):
    charset.add(mod_word[i])

input(len(charset))