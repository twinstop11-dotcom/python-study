def is_palindrome(s):
    if s==s[::-1]:
        print('회문입니다.')
    else:
        print('회문이 아닙니다.')
is_palindrome('racecar')
is_palindrome('reace')
is_palindrome('car')
