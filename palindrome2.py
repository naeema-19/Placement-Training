def isPalindrome(s, low, high):
    if(low==high):
        # We have reached the mid
        return True
    
    if(s[low]!=s[high]):
        # If unequal return false         
        return False
        
    if(low<=high):
        # increasing pointers and passing in recusive call         
        return isPalindrome(s, low+1, high-1)
    
    return True


# initializing string
n=int(input("Enter a no :"))
s = str(n)
print(isPalindrome(s, 0, len(s)-1))
