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



class Solution:
    def groupAnagrams(self, strs):
      anagrams = {}
      for word in strs:
        sorted_word = "".join(sorted(word))
        #sorted is a built in method to sort
        #sorted(word) will turn the "word" into a sorted array e.g. ['a', 'e', 't']
        if sorted_word in anagrams:
          anagrams[sorted_word].append(word)
        else:
           anagrams[sorted_word] = [word]
      return list(anagrams.values())
           
           
    




if __name__ == "__main__":
    solution = Solution()
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(test_input)
    print(result)