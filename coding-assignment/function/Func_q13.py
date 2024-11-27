# Function to Check if a String is a Palindrome
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("radar"))
print(is_palindrome("hello"))
