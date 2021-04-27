alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def wordToID(word):
  ID = []

  for letter in word:
    n = alphabet.index(letter)
    ID.append(primes[n])
  return ID


def compareWords(a, b):
  x = wordToID(a)
  y = wordToID(b)

  if set(x) == set(y):
    print("This is an Anagram")
    return True
  else:
    print("This is NOT an Anagram")
    return False


compareWords("brainy", "binary")
compareWords("restful", "fluster")

