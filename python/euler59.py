"""Problem 59
19 December 2003

Each character on a computer is assigned a unique code and the
preferred standard is ASCII (American Standard Code for Information
Interchange). For example, uppercase A = 65, asterisk (*) = 42, and
lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes
to ASCII, then XOR each byte with a given value, taken from a secret
key. The advantage with the XOR function is that using the same
encryption key on the cipher text, restores the plain text; for
example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain
text message, and the key is made up of random bytes. The user would
keep the encrypted message and the encryption key in different
locations, and without both "halves", it is impossible to decrypt the
message.

Unfortunately, this method is impractical for most users, so the
modified method is to use a password as a key. If the password is
shorter than the message, which is likely, the key is repeated
cyclically throughout the message. The balance for this method is
using a sufficiently long password key for security, but short enough
to be memorable.

Your task has been made easy, as the encryption key consists of three
lower case characters. Using cipher1.txt (right click and 'Save
Link/Target As...'), a file containing the encrypted ASCII codes, and
the knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the
original text.
"""

from eulerlib import timedRun

def euler59():
    """Used to help solve problem 59 from Project Euler.

    Try every possible key combination and print the most likely results.
    """
    file = open("cipher1.txt", mode="r")
    data = list(map(int, file.read().strip().split(",")))
    file.close()
    key = [0, 0, 0]
    for key[0] in range(ord('a'), ord('z') + 1):
        for key[1] in range(ord('a'), ord('z') + 1):
            for key[2] in range(ord('a'), ord('z') + 1):
                text = crypt(data, key)
                if text.find('the') > 1 and text.find('of') > 1:
                    print("".join(map(chr, key)), text[0:50],
                        sum(map(ord, text)))


def crypt(data, keys):
    text = ""
    for i in range(0, len(data), len(keys)):
        for j in range(len(keys)):
            if i+j < len(data):
                text += chr(data[i+j] ^ keys[j])
    return text

if __name__ == "__main__":
    timedRun(euler59)

            
