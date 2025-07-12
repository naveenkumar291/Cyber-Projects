import hashlib
from pyfiglet import Figlet
import sys

def main():
    menu()

def menu():
    print()
    custom_fig = Figlet(font="smblock")
    print()
    print(custom_fig.renderText(" Hash your String "))
    print()
    print("*** convert your string to hash ***")

    #select your choice
    choose = input("""
             A : MD5
             B : SHA_1
             C : SHA_256
             Q : Quit

	     Please enter your choice """)

    if choose == 'A' or choose == 'a':
       md5()
    elif choose == 'B' or choose == 'b':
         sha_1()
    elif choose == 'C' or choose == 'c':  
         sha_256()
    elif choose == 'Q' or choose == 'q':
          sys.exit
    else:
         print ("Select either A,B or C")
         print ("Please try again")
         menu()

def md5():
      hash = input("Enter your string :")
      hash_md = hashlib.md5()
      hash_md.update(hash.encode())
      print (f"MD5 for {hash} is :" + hash_md.hexdigest())


def sha_1():
      hash = input("Enter your string :")
      hash_md = hashlib.sha1()
      hash_md.update(hash.encode())
      print (f"SHA_1 for {hash} is :" + hash_md.hexdigest())

def sha_256():
      hash = input("Enter your string :")
      hash_md = hashlib.sha256()
      hash_md.update(hash.encode())
      print (f"SHA_256 for {hash} is :" + hash_md.hexdigest())

main()
