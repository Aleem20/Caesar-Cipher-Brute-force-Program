class Theme:
    GREEN = "\033[92m"
    DARKCYAN = "\033[36m"
    BOLD = "\033[1m"
    END = "\033[0m"
message1 = "TUZBKXEYKIAXK"
message2 = "TSJLCPYZJCRMZPSRCDMPACYRRYAIQ"
print("**********************************************************************")
print(Theme.GREEN+Theme.BOLD+"Welcome to the Caeser Cipher Brute-Forcing program!"+Theme.END)
print()
print(Theme.DARKCYAN+"This program utilizes all possible Caesar Cipher keys to print out every potential plaintext message!"+Theme.END)
print("**********************************************************************")
print(Theme.GREEN+"Given ciphertext messages: "+Theme.END)
print(message1)
print(message2)
print()
print(Theme.GREEN+"Bruteforcing in progress......"+Theme.END)
print()
#defining decipher function
def decipher(ciphertext, key):
    plaintext = ""
    for alphabets in ciphertext:
        shift = ord('a') if alphabets.islower() else ord('A')
    # Decryption formula for Caiser cipher: D(c) = (ciphertext - key) % (26)
        decrypted_alpabets = chr((ord(alphabets) - shift - key) % 26 + shift)
        plaintext = plaintext + decrypted_alpabets
    return plaintext

#brute force function
def bruteForce(ciphertext):
    for key in range(26):
        plaintext = decipher(ciphertext, key)
        print("Key ",(key), ": ", (plaintext))

print(Theme.GREEN+"All the possible plaintexts for message 1 using Brute Force attack:"+Theme.END)
bruteForce(message1)
print()
print(Theme.GREEN+"All the possible plaintexts for message 2 using Brute Force attack:"+Theme.END)
bruteForce(message2)

print()
print(Theme.GREEN+"Results: "+Theme.END)
print ("The plaintext of message 1 (TUZBKXEYKIAXK) is NOTVERYSECURE which has a key of 6")
print("The plaintext of message 2 (TSJLCPYZJCRMZPSRCDMPACYRRYAIQ) is VULNERABLETOBRUTEFORCEATTACKS which has a key of 24" )
