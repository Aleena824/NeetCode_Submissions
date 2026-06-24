class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map sorted string keys to lists of original strings
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the word to create a unique key
            sorted_key = "".join(sorted(word))
            # Append the original word to its matching key group
            anagram_map[sorted_key].append(word)
            
        # Return all grouped values as a list of lists
        return list(anagram_map.values())