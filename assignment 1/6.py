def compute_lps(pattern):
    lps = [0] * len(pattern)
    prevLPS = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]
    
    return lps

def kmp_search(haystack, pattern):
    if pattern == "":
        return 0

    lps = compute_lps(pattern)
    i = 0 
    j = 0  

    while i < len(haystack):
        if haystack[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

        if j == len(pattern):
            return i - len(pattern)

    return -1

if __name__ == "__main__":
    haystack = "CATSABCBCABCDOGSABCBCABC"
    pattern = "ABCBCABC"
    print("Pattern found at index:", kmp_search(haystack, pattern))