import hashlib

def crack_hash(hash_to_crack, wordlist):
    """
    Attempts to crack a hash using a brute force approach.

    Parameters:
    hash_to_crack (str): The hash to crack.
    wordlist (list): A list of possible passwords.

    Returns:
    str: The cracked password if found, otherwise None.
    """
    for password in wordlist:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == hash_to_crack:
            return password
    return None

# Example usage
hash_to_crack = "5ebe2294ecd0e0f08eab7690d2a6ee69"  # Example SHA-256 hash of "test"
wordlist = ["test", "password", "123456", "qwerty", "abc123"]  # Example wordlist

cracked_password = crack_hash(hash_to_crack, wordlist)
if cracked_password:
    print(f"Cracked password: {cracked_password}")
else:
    print("Password not found in the wordlist.")