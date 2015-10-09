'''
Created on Aug 23, 2015

@author: ljiang
'''

def solution(S):
    # write your code in Python 2.7
    reversed_list=[]
    word_i=-1
    for i in xrange(len(S)):
        if S[i] == ' ':
            reversed_list.append(S[i])
            word_i=i
        else:   
            reversed_list.insert(word_i+1,S[i])
    return ''.join(reversed_list)

