def rabin_karp(text, pattern, prime=101):
    d = 256
    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        print("Pattern not found")
        return

    hash_pattern = 0
    hash_text = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        hash_pattern = (d * hash_pattern + ord(pattern[i])) % prime
        hash_text = (d * hash_text + ord(text[i])) % prime

    found = False

    for i in range(n - m + 1):
        if hash_pattern == hash_text:
            match = True

            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break

            if match:
                print("Pattern found at index", i)
                found = True

        if i < n - m:
            hash_text = (
                d * (hash_text - ord(text[i]) * h)
                + ord(text[i + m])
            ) % prime

            if hash_text < 0:
                hash_text += prime

    if not found:
        print("Pattern not found")


text = "ABCCDABCAB"
pattern = "ABC"

rabin_karp(text, pattern)
