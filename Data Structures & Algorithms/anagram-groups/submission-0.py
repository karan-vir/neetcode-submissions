class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashset of unique keys:
        # act  and cat both have act -> unique key
        # For each unique key , map the words that belong to that key
        # and add them to a list

        unique = {}
        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word in unique:
                unique[sort_word].append(word)
            else:
                unique[sort_word] = [word]

        return list(unique.values())