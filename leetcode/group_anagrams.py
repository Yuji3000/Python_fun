# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters 
# of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]




def groupAnagrams(strs):
  anagrams = {}
  for word in strs:
    import ipdb; ipdb.set_trace()
    sorted_word = "".join(sorted(word))
    # sorted(word) will turn the "word" into a sorted array e.g. ['a', 'e', 't']
    # "".join(sorted(word)) = ['a', 'e', 't'] => "aet"

    if sorted_word in anagrams:
      anagrams[sorted_word].append(word)
    else:
        anagrams[sorted_word] = [word]
  return list(anagrams.values())
  # to return a list(Array) must put list(the actual list of things)
           
           
    






test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = groupAnagrams(test_input)
print(result)