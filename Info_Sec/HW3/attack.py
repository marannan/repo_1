# CS 642 University of Wisconsin
#
# usage: attack.py ciphertext
# Outputs a modified ciphertext and tag

import sys
import hashlib
# Grab ciphertext from first argument
ciphertextWithTag = (sys.argv[1]).decode("hex")

if len(ciphertextWithTag) < 16+16+32:
  print "Ciphertext is too short!"
  sys.exit(0)

iv = ciphertextWithTag[:16]
ciphertext = ciphertextWithTag[16:len(ciphertextWithTag)-32]
tag = ciphertextWithTag[len(ciphertextWithTag)-32:]

#New message with a more lucrative amount
newmessage = \
"""AMOUNT: $  901.00
Originating Acct Holder: ACE
Orgininating Acct #82675-582370954

I authorized the above amount to be transferred to the account #78561-1848 
held by a UW-Student at the National Bank of the Cayman Islands.
"""

#Tag calculated for the new modified message
tag = hashlib.sha256(newmessage).hexdigest()

#Converting the iv string to a list
oldiv = iv
listiv = list(iv);

#Modifying the iv to get a higher amount
iv = ''.join(listiv[:11])
iv += chr(ord(oldiv[11]) ^ 0x08)
iv += ''.join(listiv[12:])

#Generating the new hacked ciphertext
print iv.encode("hex") + ciphertext.encode("hex")+tag
