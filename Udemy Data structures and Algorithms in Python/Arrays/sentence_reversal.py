'''Sentence Reversal
Problem
Given a string of words, reverse all the words. For example:

Given:

'This is the best'

Return:

'best the is This'

As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:

'  space here'  and 'space here      '

both become:

'here space'

'''

def rev_word1(s):
    s=s.strip()
    #print(s,"dee")
    print(" ".join(reversed(s.split())))
def rev_word2(s):
    s=s.strip()
    #print(s,"dee")
    print(" ".join(s.split()[::-1]))


'''While these are valid solutions, 
in an interview setting you'll have to 
work out the basic algorithm that is used. 
In this case what we want to do is loop over the text and extract words 
form the string ourselves. Then we can push the words to a "stack" and in 
the end opo them all to reverse. Let's see what this actually looks like:
'''
rev_word1("Deepu Mangal")
rev_word2('Hi John,   are you ready to go?')

def rev_word3(s):
    spaces=[" "]
    words=[]
    length=len(s)
    i=0
    while i<length:
        if(s[i] not in spaces):
            word_start=i
            while i<length and s[i] not in spaces:
                i+=1
            words.append(s[word_start:i])
            # Add to index
        i += 1

        # Join the reversed words
    return " ".join(reversed(words))


print(rev_word3("Deepu Mangal"))
