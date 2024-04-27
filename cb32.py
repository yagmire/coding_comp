abc_english = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
c_base32 = ['!','@',"#","$",'%','?','^','&','*','(',')','-','_','=','+','[',']','{','}','\\','|',',','<','.','>','/']
testing_input = "the quick brown fox jumped over the lazy dog"
input = input("Type the phrase to translate: ")
conv = input
#print(len(abc_english), len(c_base32))
for x in range(len(abc_english)):
    conv = conv.replace(abc_english[x], c_base32[x])
print(f"\"{input}\" --> \"{conv}\"")