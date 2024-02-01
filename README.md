# Lab - Class 18

## Project: Caesar Salad

### Immanuel Shin

## Setup

To use Caesar Salad, follow the steps below:

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### Usage

To interact with the Caesar Salad project, follow these steps:

1. **Run the Caesar Cipher Script:**

    Execute the main script `caesar_cipher.py` using the following command:

    ```
    python caesar_cipher.py
    ```

2. **Choose an Option:**

    You will be prompted to choose between the following options:

    - Encrypt (Option 1)
    - Decrypt (Option 2)
    - Crack (Option 3)

3. **Follow the Prompts:**

    Depending on your chosen option, you will be prompted to enter the text and, if applicable, the shift value.

    - For encryption and decryption, enter the text and the shift value.
    - For cracking, enter the encrypted text.

4. **View Results:**

    The script will display the results based on your chosen option:

    - Encrypted or decrypted text.
    - Shift amount (for cracking).
    - Assurance score (for cracking).

## Exportable Functions

For users who want to import and use the Caesar Salad functions in their projects, the following functions are available:

- `encrypt(plain, shift)`: Encrypts a given plain text using the Caesar cipher with a specified shift.
- `decrypt(crypt, shift)`: Decrypts a given encrypted text using the Caesar cipher with a specified shift.
- `crack(crypt)`: Attempts to crack a Caesar cipher by finding the most likely shift, returning the decrypted text, shift value, and assurance score.

Feel free to incorporate these functions into your own projects for Caesar cipher operations.

#### Run Test

pytest tests/test_caesar.py

##### Note

crack function not built to handle non words (i.e 'aaa', 'dfasdf asdfasd asdfasd') when deciding most probable decryption.  
Instead, an unused list (all_candidates on line 57) exists in case human eyes are needed.