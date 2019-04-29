# cipher
Toy encryption based on historical ciphers. Two types of cipher are currently available, including a transposition cipher **add link to transposition README** and substitution cipher **add link to Ceaser README**. All ciphers are able to encrypt and decrypt from text files, or can be used in a python session. The available cipher methods are described **link to the base Cipher (docs?)**.

# Install
Install the package using `pip install cipher`.  To install an editable package for development use `pip install -e cipher`.

# Env for Dev
To create the cipher environment from environment file run `conda env create -f environment.yml`

# TODO
- [ ] add logging
- [ ] add tests
- [ ] ciphers from ch2 of the code book
- [ ] clean up and upload to pypi

- allow seeding (nothing is random currently)