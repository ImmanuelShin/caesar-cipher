import nltk
from nltk.corpus import words
import re

nltk.download('words')

def encrypt(plain, shift):
    """
    Encrypts a given plain text using the Caesar cipher with a specified shift.

    Parameters:
    - plain (str): The input plain text.
    - shift (int): The shift value for the Caesar cipher.

    Returns:
    str: The encrypted text.
    """
    encrypted_text = ''

    for char in plain:
        num = ord(char)
        alph = 26
        if char.isalpha():
            a = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((num + shift - a) % alph + a)
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(crypt, shift):
    """
    Decrypts a given encrypted text using the Caesar cipher with a specified shift.

    Parameters:
    - crypt (str): The input encrypted text.
    - shift (int): The shift value for the Caesar cipher.

    Returns:
    str: The decrypted text.
    """
    return encrypt(crypt, -shift)

def crack(crypt):
    """
    Attempts to crack a Caesar cipher by finding the most likely shift.

    Parameters:
    - crypt (str): The encrypted text.

    Returns:
    tuple: A tuple containing the decrypted text, similarity score, and the shift value.
    """
    corpus = set(words.words())
    alph = 26
    best_candidate = ("", 0, 0)
    all_candidates = []

    for shift in range(26):
        cracked_text = ''
        for char in crypt:
            if char.isalpha():
                a = ord('A') if char.isupper() else ord('a')
                if char.isupper():
                    cracked_text += chr((ord(char) - shift - a) % alph + a)
                else:
                    cracked_text += chr((ord(char) - shift - a) % alph + a)
            else:
                cracked_text += char
        similarity_score = calculate_similarity_score(cracked_text, corpus)
        if similarity_score > best_candidate[1]:
            best_candidate = (cracked_text, similarity_score, shift)
        all_candidates.append(cracked_text, similarity_score, shift)
    return best_candidate

def preprocess_text(text):
    """
    Preprocesses a given text by converting it to lowercase and extracting words.

    Parameters:
    - text (str): The input text.

    Returns:
    list: A list of words in the preprocessed text.
    """
    return re.findall(r'\b\w+\b', text.lower())

def calculate_similarity_score(decrypted_text, corpus):
    """
    Calculates the similarity score between the decrypted text and a given corpus of words.

    Parameters:
    - decrypted_text (str): The decrypted text.
    - corpus (set): The set of valid words.

    Returns:
    float: The similarity score.
    """
    words_decrypted = preprocess_text(decrypted_text)
    overlap_words = [word for word in words_decrypted if word in corpus]
    expected_word_count = len(words_decrypted)
    similarity_score = len(overlap_words) / \
        expected_word_count if expected_word_count > 0 else 0
    return similarity_score

