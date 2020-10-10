'''
This module explores the use of a vigenere cipher, a polyalphabetic substitution cipher, built in Python.
The excercise uses functions, modulo arithmetic, loops and list methods and builds on top of a caesar cipher
a |  b |  c |  d |  e |  f |  g |  h |  i |  j |  k |  l |  m |  n |  o |  p |  q |  r |  s |  t |  u |  v |  w |  x |  y |  z
0 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25
Formulae: 
    Cipher Text / Encoded Message: Ci = EK(Mi) => (Mi + Ki) mod 26
    Message / Decoded Message:     Mi = DK(Ci) => (Ci - Ki + 26) mod 26
    Where i: index, C: Ciphertext, E/D: Vigenere Encoding/Decoding, K: key k: Keyword (input), M: Message (input)
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Key creation
def msgkey(msg, keyword):
    key = ''
    keyword_length = len(keyword)
    key_list = []
    i = 0
    for char in msg:
        if char in alphabet:
            key_list.append(i)
            i += 1
        else:
            key_list.append(char)
    for item in key_list:
        if type(item) == int:
            key += keyword[item % keyword_length]
        else:
            key += item
    return key

# Encode
def v_encode(msg, keyword):
    emsg = ''
    key = msgkey(msg, keyword)
    for i in range(len(key)):
        if key[i] not in alphabet:
            emsg += key[i]
        else:
            emsg += alphabet[((alphabet.index(msg[i]) + alphabet.index(key[i])) % len(alphabet))]
    return emsg

# Decode
def v_decode(msg, keyword):
    key = msgkey(msg, keyword)
    dmsg = ''
    for i in range(len(key)):
        if key[i] not in alphabet:
            dmsg += key[i]
        else:
            dmsg += alphabet[((alphabet.index(msg[i]) - alphabet.index(key[i])) + 26) % len(alphabet)]
    return dmsg

# Main function to encode/decode messages
def cipher(msg, keyword, mode='e'):
    '''Mode is 'e' for encoding & 'd' for decoding. '''
    message = ''
    if mode == 'e':
        message = v_encode(msg.lower(), keyword.lower())
    else:
        message = v_decode(msg.lower(), keyword.lower())
    print(message)

# Test / Debug Statements
cipher('pbgecz pe hpea. kods wyrs!', 'pineapple', 'd')
cipher('Attack at dawn. Good Luck!', 'pineapple', 'e')
cipher('barry is the spy', 'dog', 'e')
cipher('dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!', 'friends', 'd')