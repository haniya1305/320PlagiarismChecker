def search(pattern, text, prime):
    ALPHABET_SIZE = 256 # number of characters in input alphabet
    pattern_length = len(pattern)
    text_length = len(text)
    i = 0
    j = 0
    pattern_hash = 0
    text_hash = 0
    hash_multiplier = 1

    # Calculate hash multiplier as pow(ALPHABET_SIZE, pattern_length-1) % prime
    for i in range(pattern_length-1):
        hash_multiplier = (hash_multiplier * ALPHABET_SIZE) % prime

    # Calculate the hash value of pattern and first window of text
    for i in range(pattern_length):
        pattern_hash = (ALPHABET_SIZE * pattern_hash + ord(pattern[i])) % prime
        text_hash = (ALPHABET_SIZE * text_hash + ord(text[i])) % prime

    # Slide the pattern over text one by one
    for i in range(text_length - pattern_length + 1):
        # Check the hash values of current window of text and pattern
        # If the hash values match then only check for characters one by one
        if pattern_hash == text_hash:
            # Check for characters one by one
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            # If p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if j == pattern_length:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < text_length - pattern_length:
            text_hash = (ALPHABET_SIZE * (text_hash - ord(text[i]) * hash_multiplier) + ord(text[i + pattern_length])) % prime
            # We might get negative values of text_hash, converting it to positive
            if text_hash < 0:
                text_hash += prime

def RapinKarpSearch(pattern, text):
    search(pattern=pattern, text=text, prime=101)