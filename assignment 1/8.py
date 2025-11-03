def naive_string_search(text, pattern):
    n = len(text)
    m = len(pattern)
    found_indices = []
    comparison_count = 0
    
    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            comparison_count += 1
            i += 1
            j += 1

            if j == m:
                found_indices.append(i - m)
                i = i - j + 1
                j = 0
        else:
            if j > 0:
                i = i - j + 1
            else:
                i += 1
            j = 0

    if not found_indices:
        print("No found\n")
    else:
        print(f"Match found at starting indices: {found_indices}")

    return comparison_count

def compute_lps_array(pattern):
    m = len(pattern)
    lps_array = [0] * m
    comparison_count = 0

    j = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[j]:
            comparison_count += 1
            j += 1
            lps_array[i] = j
            i += 1
        else:
            if j != 0:
                j = lps_array[j - 1]
            else:
                lps_array[i] = 0
                i += 1
                
    return lps_array, comparison_count

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    found_indices = []
    
    if m > n:
        return -1, 0

    lps_array, lps_build_comparisons = compute_lps_array(pattern)
    search_comparisons = 0

    i = 0
    j = 0
    
    while i < n:
        if text[i] == pattern[j]:
            search_comparisons += 1
            i += 1
            j += 1

            if j == m:
                found_indices.append(i - m)
                j = lps_array[j - 1]
        
        else:
            if j != 0:
                j = lps_array[j - 1]
            else:
                i += 1

    if not found_indices:
        print("No found\n")
    else:
        print(f"Match found at starting indices: {found_indices}")
        
    return search_comparisons, lps_build_comparisons

if __name__ == "__main__":
    main_text = "AAAAAAAAAAABBCDDAAACAAABBB"
    search_pattern = "AAABB"

    print(f"Text: '{main_text}'")
    print(f"Pattern: '{search_pattern}'\n")

    kmp_comparisons, lps_comparisons = kmp_search(main_text, search_pattern)
    
    naive_comparisons = naive_string_search(main_text, search_pattern)

    print(f"Comparisons of LPS table: {lps_comparisons}")
    print(f"KMP Search vs Naive Search: {kmp_comparisons} KMP VS {naive_comparisons} Naive")