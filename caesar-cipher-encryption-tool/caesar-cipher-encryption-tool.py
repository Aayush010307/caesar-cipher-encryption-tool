alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Enter the word 'encode' to encrypt and 'decode' to decrypt:\n").lower()
text = input("Enter your message:\n").lower()
shift = int(input("Enter the number of places to shift the encryption by:\n"))

def caesar(og_text, shift, enc_dec):
    cypher_text = ""
    if enc_dec == "decode":
        shift *= -1
    for letter in og_text:
        if letter not in alphabets:
            cypher_text += letter
        else:
            shifted_pos = (alphabets.index(letter) + shift) % len(alphabets)
            cypher_text += alphabets[shifted_pos]
    print(f"Here is your {enc_dec}d text: {cypher_text}")

caesar(text, shift, direction)