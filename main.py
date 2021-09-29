'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n < 2:
    return False
  for i in range(2,n):
    if n % i==0:
      return False
  return True
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  produs = 1
  for numar in lst:
    produs *=numar
  return produs

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x!=y:
    if x > y: x -=y
    else: y -=x
  return x


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  r = x%y
  while x % y:
    x=y
    y=r
    r=x%y
  return y



def main():
  # interfata de tip consola aici
  pass
  print()
  if __name__ == '__main__':
    main()
