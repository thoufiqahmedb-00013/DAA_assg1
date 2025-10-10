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

if __name__ == "__main__":
    s1 = "ABCBCABC"
    arrs1 = [char for char in s1]
    print("Pattern:", arrs1)
    print("LPS table:", compute_lps(s1))