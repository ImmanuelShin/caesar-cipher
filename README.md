# Lab - Class 18

## Project: Caesar Salad

### Immanuel Shin

### Setup

#### Modules

pip install -r requirements.txt

#### Run Test

pytest tests/test_caesar.py

##### Note

crack function not built to handle non words (i.e 'aaa', 'dfasdf asdfasd asdfasd') when deciding most probable decryption.  
Instead, an unused list (all_candidates on line 57) exists in case human eyes are needed.