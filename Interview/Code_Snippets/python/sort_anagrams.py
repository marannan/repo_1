import os
import sys

def find_anagram(word, words_list):
    anagrams_words = []
    for rest_word in words_list:  
        if sorted(word) != sorted(rest_word):
            continue    
        
        anagrams_words.append(rest_word)   
    
    return anagrams_words

def sort_anagrams(word_list):

    words_list_sorted = []
    for i in range (0,len(words_list)):
        if words_list[i] not in words_list_sorted:
            new_words_list = []
            words_list_sorted.append(word_list[i])
            new_words_list = list(words_list)
            new_words_list.pop(i)
            anagram_words = find_anagram(word_list[i],new_words_list)
            words_list_sorted.extend(anagram_words)
            
            
    return words_list_sorted


if __name__ == "__main__":

    words_list = ["kirthu", "manoj", "ashok", "god", "boob", "gopal", "kosha", "bobo", "palgo", "okash", "dog", "abcdef"]
    words_list_sorted = sort_anagrams(words_list)
    print words_list_sorted
    #print list(set(words_list_sorted))