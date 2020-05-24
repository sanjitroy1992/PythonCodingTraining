# Searching algorithm
def search(sub_string, main_string):
    Sublen = len(pat)
    Mainlen = len(txt)
    print("Sublen: {} & Mainlen: {}".format(Sublen, Mainlen))
    # print(Mainlen - Sublen + 1)
    # A loop to slide pat[] one by one */
    for i in range(Mainlen - Sublen + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while (j < Sublen):
            # print(i,j)
            if (main_string[i + j] != sub_string[j]):
                break
            j += 1

        if (j == Sublen):
            print("Pattern found at index ", i)

        # Driver Code


# if __name__ == '__main__':
#     txt = "ABCDBC"
#     pat = "BC"
#     search(pat, txt)
