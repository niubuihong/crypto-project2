import urllib.request
from Crypto.Cipher import AES
import binascii
import base64
import random
import os
import zlib

################################################################################
# CS 284 Padding Utility Functions
################################################################################

# s is a bytearray to pad, k is blocklength
# you won't need to change the block length
def cmsc284pad(s,k=16):
    if k > 255:
        print("pkcs7pad: padding block length must be less than 256")
        return bytearray()
    n = k - (len(s) % k)
    if n == 0:
        n = k
    for i in range(1,n+1):
        s.extend([i])
    return s

# s is bytes to pad, k is blocklength
# you won't need to change the block length
def cmsc284padbytes(s,k=16):
    if k > 255:
        raise Exception("pkcs7pad: padding block length must be less than 256")
    n = k - (len(s) % k)
    if n == 0:
        n = k
    for i in range(1,n+1):
        s += chr(i).encode("utf-8")
    return s

# s is bytes to unpad, k is blocklength
# you won't need to change the block length
def cmsc284unpad(s,k=16):
    if not cmsc284checkpadding(s,k):
        print("cmsc284unpad: invalid padding")
        return b''
    n = s[len(s)-1]
    return s[:len(s)-n]

# checks padding on s and returns a boolean
# you won't need to change the block length
def cmsc284checkpadding(s,k=16):
    if(len(s) == 0):
       #print("Invalid padding: String zero length"%k) 
       return False
    if(len(s)%k != 0): 
       #print("Invalid padding: String is not multiple of %d bytes"%k) 
       return False
    n = s[len(s)-1]
    if n > k or n == 0:
       return False
    else: 
        for i in range(n):
            if s[len(s)-1-i] != (n-i):
                return False
    return True

################################################################################
# Function for querying the server
################################################################################

SERVER = "http://cryptoclass.cs.uchicago.edu/"
def make_query(task, cnetid, query):
    DEBUG = False
    if DEBUG:
        print("making a query")
        print("Task:", task)
        print("CNET ID:", cnetid)
        print("Query:", query)
    if (type(query) is bytearray) or (type(query) is bytes):
        url = SERVER + urllib.parse.quote_plus(task) + "/" + urllib.parse.quote_plus(cnetid) + "/" + urllib.parse.quote_plus(base64.urlsafe_b64encode(query)) + "/"
    else:
        url = SERVER + urllib.parse.quote_plus(task) + "/" + urllib.parse.quote_plus(cnetid) + "/" + urllib.parse.quote_plus(base64.urlsafe_b64encode(query.encode('utf-8'))) + "/"
    if DEBUG:
        print("Querying:", url)

    with urllib.request.urlopen(url) as response:
        raw_answer = response.read()
        answer = base64.urlsafe_b64decode(raw_answer)
        if DEBUG:
            print("Answer:", answer)
        return answer
    return None


################################################################################
# Problem 1 SOLUTION
################################################################################

def problem1(cnetid):
    return b''


################################################################################
# Problem 2 SOLUTION
################################################################################

def problem2(cnetid):
    return b''


################################################################################
# Problem 3 SOLUTION
################################################################################

def problem3(cnetid):
    return b''


################################################################################
# Problem 4 SOLUTION
################################################################################

def problem4(cnetid):
    return b''


################################################################################
# Problem 5 SOLUTION
################################################################################

def problem5(cnetid):
    return b''

################################################################################
# Problem 6 SOLUTION
################################################################################

def problem6(cnetid):
    return b''

################################################################################
# Problem 7 SOLUTION
################################################################################

def problem7(cnetid):
    return b''

if __name__ == "__main__":
    # your driver code for testing here

    # example running AES; delete the code below here
    key = b'ABCDEFGHABCDEFGH'
    block1 = b'abcdefghabcdefgh'
    block2 = bytearray(b'abcdefghabcdefgh')

    # we declare the mode to be ECB, but just use it for single-block calls
    # cipher = AES.new(key, AES.MODE_ECB)
    # print("\n*****ECB block 1*****")
    # print(cipher.encrypt(block1))

    # the following call with fail without the converting block2 to bytes
    # before the call to AES. The AES implementation requires an immutable
    # object, but bytearray is mutable. Same goes for key in the AES.new call.
    # print("\n*****ECB block 2*****")
    # print(cipher.encrypt(bytes(block2)))

    # test query, will hang if off-campus
    id = 'niubuihong'
    zerosArray = [0x00] * 10000
    # print(f"\n*****make_query('one',{id},{zerosArray})*****")
    print(make_query('one',id, ''))

    # examples below: bytearrays are mutable, which is handy
    # print("\n*****BYTEARRAYS*****")
    # print(block2)
    # block2.extend([0])
    # print(block2)
    # block2.extend(block1)
    # block2 = bytearray(b'abcdefghabcdefgh')
    # print(block2)


    # print("\n*****Bytes/Bytearray/ord/chr*****")
    # prime_numbers = [0, 97, 0x61, 5, 255] # if something is printatble, it will be printed
    # # convert list to bytearray
    # byte_array = bytearray(prime_numbers)
    # bytes = bytes(prime_numbers)
    # print(byte_array)
    # print(bytes)
    # print('abc'.encode('utf-8'))
    # print(b'abc'.decode())
    # print(chr(0x61))
    # print(hex(ord('a')))

