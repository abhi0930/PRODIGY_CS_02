from PIL import Image
import numpy as np

# Encryption function
def encrypt_image(input_image_path, output_image_path, key=10):
    # Open the image
    image = Image.open(input_image_path)
    
    # Convert image to numpy array (pixel values)
    image_pixels = np.array(image)

    # Apply XOR operation or shifting to manipulate pixels
    encrypted_pixels = np.bitwise_xor(image_pixels, key)

    # Convert the manipulated pixels back to an image
    encrypted_image = Image.fromarray(encrypted_pixels)
    
    # Save the encrypted image
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

# Decryption function
def decrypt_image(input_image_path, output_image_path, key=10):
    # Open the encrypted image
    image = Image.open(input_image_path)
    
    # Convert image to numpy array (pixel values)
    encrypted_pixels = np.array(image)
    
    # Reverse the XOR operation or shifting
    decrypted_pixels = np.bitwise_xor(encrypted_pixels, key)

    # Convert the manipulated pixels back to an image
    decrypted_image = Image.fromarray(decrypted_pixels)
    
    # Save the decrypted image
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

# Example usage
if _name_ == "_main_":
    # Define input and output file paths
    input_path = "input_image.png"  # Replace with your image path
    encrypted_path = "encrypted_image.png"
    decrypted_path = "decrypted_image.png"
    
    # Encrypt the image
    encrypt_image(input_path, encrypted_path, key=10)
    
    # Decrypt the image
    decrypt_image(encrypted_path, decrypted_path, key=10)
