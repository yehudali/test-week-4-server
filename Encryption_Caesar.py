ab=["a","b","c","d","d","e","f","g","h",'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(text:str,offset:int):
    enc=""
    for i in text:
        if offset<27:
            if i.isalpha():
                if text.index(i)  <  len(ab)-offset:
                    enc+=ab[ab.index(i)+offset]
                else:
                    enc+=ab[(offset)-(len(ab)-ab.index(i))]
            else:
               enc+=i
        else:
            raise TypeError( "offset is very hi")

    return enc
    
print(encrypt("abcd",3))

def decrypt(text:str,offset:int):
    enc=""
    for i in text:
        if offset<27:
            if text.isalpha():
                if ab.index(i)  <  len(ab)-offset:
                    enc+=ab[ab.index(i)+offset]
                else:
                    enc+=ab[(offset)-(len(ab)-ab.index(i))]
            else:
               enc+=i
        else:
            raise TypeError( "offset is very hi")

    return enc
    