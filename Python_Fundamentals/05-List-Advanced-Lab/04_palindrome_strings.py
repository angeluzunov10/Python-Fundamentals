words = input().split()
searched_palindrome = input()

palindromes_found = [palindrome for palindrome in words if palindrome == palindrome[::-1]]
count_of_palindromes = palindromes_found.count(searched_palindrome)

print(palindromes_found)
print(f"Found palindrome {count_of_palindromes} times")
