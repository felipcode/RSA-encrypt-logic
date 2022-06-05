import numpy as np
import math
import random
import string



'''@@------------------------------------------------------------------@@'''
## PREREQUISITES
# to generate a large prime number I used this logic:

### Pre generated primes

first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

# if a prime candidate is already not divisible by the first_primes_list
# there is a high probability that de candidate is also a prime
# yet, it is used the  Rabin Miller Primality test for assurance
# generates large prime numbers of size = bitsize

def generate_large_prime(bitsize = 1024):
  while True:
    n = bitsize
    prime_candidate = get_lowLevelPrime(n)
    if not rabin_passed(prime_candidate):
      continue
    else:
      print(n, "bit prime is: \n", prime_candidate)
      return prime_candidate
      break
  pass

def nBitRandom(n):
  return (random.randrange(2**(n-1)+1, 2**n-1))

def get_lowLevelPrime(n):
  '''Generate a prime candidate divisible
    by first primes'''
  
  # Repeat until a number satisfying
  # the test isn't found
  while True: 
  
      # Obtain a random number
      prime_candidate = nBitRandom(n) 
  
      for divisor in first_primes_list: 
          if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate:
            break
          # If no divisor found, return value
          else: 
            return prime_candidate
  

def rabin_passed(mrc):
  '''Run 20 iterations of Rabin Miller Primality test'''
  maxDivisionsByTwo = 0
  ec = mrc-1
  while ec % 2 == 0:
      ec >>= 1
      maxDivisionsByTwo += 1
  assert(2**maxDivisionsByTwo * ec == mrc-1)

  def trialComposite(round_tester):
      if pow(round_tester, ec, mrc) == 1:
          return False
      for i in range(maxDivisionsByTwo):
          if pow(round_tester, 2**i * ec, mrc) == mrc-1:
              return False
      return True

  # Set number of trials here
  numberOfRabinTrials = 20
  for i in range(numberOfRabinTrials):
      round_tester = random.randrange(2, mrc)
      if trialComposite(round_tester):
          return False
  return True
  
'''@@------------------------------------------------------------------@@'''




class rsa:              # my rsa class
  def __init__(self):
    self.p =0         # suposed to be private 
    self.q =0         # suposed to be private 
    self.n =0         # suposed to be private 
    self.totient =0   # suposed to be private
    self.d =0         # suposed to be private
    self.e =0         # suposed to be private
    self.pub_k = []   # suposed to be pUBLIC
    self.pv_k = []    # suposed to be private
    pass
  
  def generate_keys(self):
    flag = 1
    while(flag):
      self.p = generate_large_prime(8)              # i choose size of 8 bits for this example
      self.q = generate_large_prime(8)              # i choose size of 8 bits for this example
      if (self.q != self.p):
        self.n = self.q * self.p
        flag = 0
    self.totient = (self.p-1)*(self.q-1)
    
    # lets define  "e"
    #  1 < e < totient    and must be coprimes
    for i in range (2, self.totient+1):
      aux1 = 1
      aux1 = self.gcd(i, self.n)
      aux2 = self.gcd(i, self.totient)         # maybe not coprime with "n"
      if (aux1 == 1 and aux2 == 1):
        self.e = i

    # lets define "d"
    # d = (2 * totient + 1) / e
    # self.d = int((2*self.totient+1)/self.e)
    for i in range(self.e * 5):
        if (self.e * i) % self.totient == 1:
            self.d = i

    self.pub_k = [self.n, self.e]   #  [n, e]
    self.pv_k = [self.d, self.n]    #  [d, n ]
    # print(self.e)
    pass
  def gcd(self,x, y):        # greatest commom divisor   -  should be 1 if the numbers compared are coprimes
    while(y):
        x, y = y, x % y
    return x



  def cipher(self, msg, key_):
    M = self.text_to_digits(msg)
    return [(i ** key_[1]) % key_[0] for i in M]            # operation 
    pass

  def de_cipher(self, e_msg, key_):
    return [((i ** key_[0]) % key_[1]) for i in e_msg]      # operation
    pass

  def text_to_digits(self, PT):
    M = []
    for i in PT:
      M.append(ord(i))
    return M

  def digits_to_text(self, DT):
    msg = []
    for i in DT:
      i = int(i)
      msg.append(chr(i))
      #print(i)
    return msg

  def show_msg(self, msg_dgt):
    i = self.digits_to_text(msg_dgt)
    # print(i)
    for j in i:
      print(j, end='', sep='')
    print("")
    


def text_to_digits(PT):
  M = []
  for i in PT:
    M.append(ord(i))
  return M

''' @@--------------------------FUNCTIONING-TEST--------------------------@@ '''

## CREATE INSTANCE
ablu = rsa()
ablu.generate_keys()
## DEFINE MESSAGE
msg = 'ninguem eh 100porcento toda hr'          # string
dgt_m = text_to_digits(msg)                     # digits - ascii

## AUTHENTICATION TEST
enc_msg = ablu.cipher(msg, ablu.pub_k)              # The encoded message --> encode with recievers public key
d_msg = ablu.de_cipher(enc_msg, ablu.pv_k)          # The decoded message --> decrypt with recievers private key

print("The original message string : ", end='')
ablu.show_msg(d_msg)

print("\nThe original message in ascii :\n", dgt_m)
print("The encoded message in ascii:\n", enc_msg)
print("The decoded message in ascii:\n", d_msg)

print("\n\n\nThe original message string : ", end='')
ablu.show_msg(dgt_m)
print("The decoded message string : ", end='')
ablu.show_msg(d_msg)

print("\n\nThe pv_key vector for the instance:", ablu.pv_k)
print("The pub_key vector for the instance:", ablu.pub_k)


