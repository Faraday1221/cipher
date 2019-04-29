# Base Cipher
- Explain what methods will be available to all ciphers that inherit from the base cipher
- If the base class allows removal of punctuation / spaces as args document that here (TBD)

# Text Transformations
Keep in mind that anything removed cannot be replaced
- how to treat punctuation (spaces)?
    - once removed, it cannot be put back in
- how to treat with upper and lowercase letters?
    - All alphabets are matched upper and lowercase; i.e. a:b will map A:B also
    - provide an option to remove case?