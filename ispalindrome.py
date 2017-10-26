'''
Created on 27 Dec 2011

@author: Campbell

Checks if the passed string s is a palindrome
'''
 
def ispalindrome(s):
    "check if string s is a palindrome"

    if s == s[::-1]:
        return True
    else:
        return False


if __name__=='__main__':
    #testing
    

    print ("a", ispalindrome("a"))
    print ("ab", ispalindrome("ab"))
    print ("aba", ispalindrome("aba"))
    print ("abba", ispalindrome("abba"))
    print ("aabba", ispalindrome("aabba"))
    print ("2447", ispalindrome(str(247)))



    
