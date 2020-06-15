"""
Have the function BinaryReversal(str) take the str parameter being passed, which will be a positive integer,
take its binary representation (padded to the nearest N * 8 bits), reverse that string of bits,
and then finally return the new reversed string in decimal form. For example: if str is "47"
then the binary version of this integer is 101111 but we pad it to be 00101111.
Your program should reverse this binary string which then becomes: 11110100 and then
finally return the decimal version of this string, which is 244.
Examples
Input: "213"
Output: 171
Input: "4567"
Output: 60296
"""
def BinaryReversal(str1):
    n = bin(int(str1))
    n = n[2:]  #Slice the number and take only the binary part of it
    if len(n) % 8 == 0:
        N = len(n) // 8    # This condition is checking if the length is within 8 bits or more. If 8 then N=1
    else:
        N = len(n) // 8 + 1  # For bigger number N=2
    k = n[::-1]  # Reverse the binary number
    while len(k) < N * 8:
        k += "0"  # keep adding 0 until the binary becomes either 8 bit or 16 bit

    return int(k, 2)

print(BinaryReversal('4567'))