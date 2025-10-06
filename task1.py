# 1. Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
# Example:
# Input: 7
# Output: Odd


# 2. Find the maximum and minimum element in a list
lst = [3, 7, 1, 9, 4]
max_num = lst[0]
min_num = lst[0]
for i in lst:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print("List:", lst)
print("Max:", max_num, "Min:", min_num)
# Example:
# Output:
# List: [3, 7, 1, 9, 4]
# Max: 9 Min: 1


# 3. Reverse a string without using slicing
s = input("Enter a string: ")
rev = ""
for i in range(len(s) - 1, -1, -1):
    rev += s[i]
print("Reversed string:", rev)
# Example:
# Input: hello
# Output: olleh


# 4. Check if a string is a palindrome
s = input("Enter a string to check palindrome: ")
rev = ""
for i in range(len(s) - 1, -1, -1):
    rev += s[i]
if s == rev:
    print("Palindrome")
else:
    print("Not palindrome")
# Example:
# Input: madam
# Output: Palindrome


# 5. Find the factorial of a number (using loop)
n = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)
# Example:
# Input: 5
# Output: Factorial: 120


# 6. Count the frequency of each character in a string
s = input("Enter a string: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Character frequencies:", freq)
# Example:
# Input: banana
# Output: Character frequencies: {'b': 1, 'a': 3, 'n': 2}


# 7. Find the second largest number in a list
lst = [10, 4, 8, 15, 6]
largest = lst[0]
second = lst[0]
for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("List:", lst)
print("Second largest:", second)
# Example:
# Output:
# List: [10, 4, 8, 15, 6]
# Second largest: 10


# 8. Count how many vowels and consonants are in a string
s = input("Enter a string: ").lower()
vowels = 0
consonants = 0
for ch in s:
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1
print("Vowels:", vowels, "Consonants:", consonants)
# Example:
# Input: Hello World
# Output: Vowels: 3 Consonants: 7


# 9. Calculate the sum of digits of a number
num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print("Sum of digits:", total)
# Example:
# Input: 1234
# Output: Sum of digits: 10


# 10. Print the multiplication table of a number
n = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
# Example:
# Input: 5
# Output:
# 5 x 1 = 5
# ...
# 5 x 10 = 50


# 11. Find the largest word in a given sentence
sentence = input("Enter a sentence: ").split()
largest = sentence[0]
for word in sentence:
    if len(word) > len(largest):
        largest = word
print("Largest word:", largest)
# Example:
# Input: Python is amazing
# Output: Largest word: amazing


# 12. Remove all duplicate elements from a list
lst = [1, 2, 2, 3, 4, 4, 5]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print("Original list:", lst)
print("List without duplicates:", new_lst)
# Example:
# Output:
# Original list: [1, 2, 2, 3, 4, 4, 5]
# List without duplicates: [1, 2, 3, 4, 5]


# 13. Sort a list without using .sort()
lst = [5, 2, 8, 1, 3]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("Sorted list:", lst)
# Example:
# Output: Sorted list: [1, 2, 3, 5, 8]


# 14. Merge two lists into a single sorted list
lst1 = [1, 4, 6]
lst2 = [2, 3, 5]
merged = lst1 + lst2
for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]
print("Merged and sorted list:", merged)
# Example:
# Output: Merged and sorted list: [1, 2, 3, 4, 5, 6]


# 15. Check if a number is a prime number
n = int(input("Enter a number: "))
if n <= 1:
    print("Not prime")
else:
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1
            break
    if count == 0:
        print("Prime")
    else:
        print("Not prime")
# Example:
# Input: 7
# Output: Prime


# 16. Find all pairs in a list that sum up to a target value
lst = [2, 4, 3, 5, 7, 8, 9]
target = int(input("Enter target sum: "))
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i], "+", lst[j], "=", target)
# Example:
# Input: 10
# Output:
# 2 + 8 = 10
# 3 + 7 = 10


# 17. Rotate a list by k positions
lst = [1, 2, 3, 4, 5, 6]
k = int(input("Enter number of positions to rotate: "))
k = k % len(lst)
rotated = []
for i in range(k, len(lst)):
    rotated.append(lst[i])
for i in range(0, k):
    rotated.append(lst[i])
print("Rotated list:", rotated)
# Example:
# Input: 2
# Output: Rotated list: [3, 4, 5, 6, 1, 2]


# 18. Find the missing number in a list of consecutive integers
lst = [1, 2, 3, 5, 6]
expected_sum = 0
for i in range(lst[0], lst[-1] + 1):
    expected_sum += i
actual_sum = 0
for i in range(len(lst)):
    actual_sum += lst[i]
print("Missing number:", expected_sum - actual_sum)
# Example:
# Output: Missing number: 4


# 19. Check if two strings are anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

a1 = ""
for ch in s1:
    if 'A' <= ch <= 'Z':
        ch = chr(ord(ch) + 32)
    if ch != ' ':
        a1 += ch

a2 = ""
for ch in s2:
    if 'A' <= ch <= 'Z':
        ch = chr(ord(ch) + 32)
    if ch != ' ':
        a2 += ch

if len(a1) != len(a2):
    print("Not anagrams")
else:
    freq1 = [0] * 26
    freq2 = [0] * 26

    for i in range(len(a1)):
        freq1[ord(a1[i]) - ord('a')] += 1
    for i in range(len(a2)):
        freq2[ord(a2[i]) - ord('a')] += 1

    same = True
    for i in range(26):
        if freq1[i] != freq2[i]:
            same = False
            break

    if same:
        print("Anagrams")
    else:
        print("Not anagrams")
# Example:
# Input:
# listen
# silent
# Output: Anagrams


# 20. Count number of words in a sentence
sentence = input("Enter a sentence: ")
count = 0
in_word = False
for ch in sentence:
    if ch != ' ' and not in_word:
        count += 1
        in_word = True
    elif ch == ' ':
        in_word = False
print("Number of words:", count)
# Example:
# Input: Python is fun
# Output: Number of words: 3


# 21. Remove all duplicate words from a sentence
sentence = input("Enter a sentence: ")
result = ""
word = ""
unique = ""

for ch in sentence + " ":
    if ch != " ":
        word += ch
    else:
        found = False
        temp = ""
        for c in unique + " ":
            if c != " ":
                temp += c
            else:
                if temp == word:
                    found = True
                    break
                temp = ""
        if not found and word != "":
            if result != "":
                result += " "
            result += word
            if unique != "":
                unique += " "
            unique += word
        word = ""

print("Sentence without duplicates:", result)
# Example:
# Input: this is is a test test
# Output: Sentence without duplicates: this is a test


# 22. Invert a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
inverted = {}
for key in d:
    val = d[key]
    inverted[val] = key
print("Inverted dictionary:", inverted)
# Example:
# Output: Inverted dictionary: {1: 'a', 2: 'b', 3: 'c'}


# 23. Find the intersection of two lists
lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
intersection = []
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i] == lst2[j]:
            intersection.append(lst1[i])
            break
print("Intersection:", intersection)
# Example:
# Output: Intersection: [4, 5]


# 24. Print the transpose of a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows = len(matrix)
cols = len(matrix[0])
transpose = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)
print("Transpose of matrix:")
for i in range(len(transpose)):
    print(transpose[i])
# Example:
# Output:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]


# 25. Implement bubble sort
lst = [5, 3, 8, 4, 2]
n = len(lst)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            temp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = temp
print("Sorted list (Bubble Sort):", lst)
# Example:
# Output: Sorted list (Bubble Sort): [2, 3, 4, 5, 8]


# 26. Find the first non-repeating character in a string
s = input("Enter a string: ")
found = False
for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1
    if count == 1:
        print("First non-repeating character:", s[i])
        found = True
        break
if not found:
    print("No non-repeating characters")
# Example:
# Input: swiss
# Output: First non-repeating character: w


# 27. Find the longest word in a sentence
sentence = input("Enter a sentence: ")
words = []
word = ""
for ch in sentence + " ":
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""
longest = words[0]
for i in range(1, len(words)):
    if len(words[i]) > len(longest):
        longest = words[i]
print("Longest word:", longest)
# Example:
# Input: I love programming
# Output: Longest word: programming


# 28. Find the second smallest number in a list
lst = [5, 2, 8, 1, 3]
smallest = lst[0]
for i in range(1, len(lst)):
    if lst[i] < smallest:
        smallest = lst[i]
second_smallest = None
for i in range(len(lst)):
    if lst[i] != smallest:
        if second_smallest is None or lst[i] < second_smallest:
            second_smallest = lst[i]
print("Second smallest:", second_smallest)
# Example:
# Output: Second smallest: 2


# 29. Check if a number is an Armstrong number
num = int(input("Enter a number: "))
temp = num
digits = 0
while temp > 0:
    digits += 1
    temp //= 10
temp = num
sum_of_powers = 0
while temp > 0:
    digit = temp % 10
    power = 1
    for i in range(digits):
        power *= digit
    sum_of_powers += power
    temp //= 10
if sum_of_powers == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
# Example:
# Input: 153
# Output: Armstrong number
