# Python program that counts the frequency of each word in a sentence or paragraph.

test_string = input("Enter string:")
word_list = test_string.split()
word_freq = [word_list.count(word) for word in word_list]
result = dict(zip(word_list, word_freq))
print(result)