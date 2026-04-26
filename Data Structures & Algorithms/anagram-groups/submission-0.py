class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angr_hash_map : Dict[str, List[str]] = {}
        n : int = len(strs)
        for i in range(n): 
            sorted_str : str = "".join(sorted(strs[i]))
            if sorted_str in angr_hash_map:
                angr_hash_map[sorted_str].append(strs[i])
            else : 
                angr_hash_map[sorted_str] = [strs[i]]
        return list(angr_hash_map.values())