def caesar_encrypt(text, shift):
    encrypted_text = ""
    
    # Iterate through each character in the text
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            
            # Perform the encryption shift
            encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += encrypted_char
        else:
            # Non-alphabetical characters are not encrypted
            encrypted_text += char
    
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    
    # Iterate through each character in the text
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            
            # Perform the decryption shift
            decrypted_char = chr(start + (ord(char) - start - shift) % 26)
            decrypted_text += decrypted_char
        else:
            # Non-alphabetical characters are not decrypted
            decrypted_text += char
    
    return decrypted_text

def main():
    print("Caesar Cipher Encryption and Decryption")
    
    # Input the action (encryption or decryption)
    action = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    
    # Input the message and the shift value
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    # Perform the action
    if action == 'E':
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif action == 'D':
        decrypted_message = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice! Please choose either 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
