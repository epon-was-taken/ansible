import bcrypt
import getpass

def hash_password(password):
    """
    Hash a password using bcrypt.
    
    Args:
        password (str): The password to hash
        
    Returns:
        str: The hashed password
    """
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(password, hashed_password):
    """
    Verify a password against a bcrypt hash.
    
    Args:
        password (str): The password to verify
        hashed_password (str): The bcrypt hash to verify against
        
    Returns:
        bool: True if the password matches, False otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

if __name__ == "__main__":
    # Get password from user (hidden input)
    password = getpass.getpass("Enter password to hash: ")
    
    # Hash the password
    hashed = hash_password(password)
    print(f"\nHashed password: {hashed}")
    
    # Optional: verify the password
    verify = getpass.getpass("\nEnter password to verify (or press Enter to skip): ")
    if verify:
        if verify_password(verify, hashed):
            print("✓ Password matches!")
        else:
            print("✗ Password does not match!")
