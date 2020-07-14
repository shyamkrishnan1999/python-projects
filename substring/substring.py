word=input()

charset=set()
mod_word=word.lower()
length=i=j=0

while j<len(mod_word):
    if mod_word[j] in charset:
        charset.remove(mod_word[i])
        i+=1
    else:
        charset.add(mod_word[j])
        j+=1
        length=max(len(mod_word),length)

input(len(charset))