class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            my_map = {}
            for c in s:
               my_map[c] = my_map.get(c, 0) + 1
            key = tuple(sorted(my_map.items()))
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())