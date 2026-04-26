class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angr_hash_map : Dict[str, List[str]] = {}
        n : int = len(strs)
        for i in range(n): 
            m = len(strs[i])
            hash_map_alphabet :Dict[str, int] = {
                k:v for k,v in zip("abcdefghijklmnopqrstuvwxyz", [0]*26)
            }
            for j in range(m):
                hash_map_alphabet[strs[i][j]] += 1
            hashed : str = str(hash(str(hash_map_alphabet)))
            if hashed in angr_hash_map:
                angr_hash_map[hashed].append(strs[i])
            else: 
                angr_hash_map[hashed] = [strs[i]]
        return list(angr_hash_map.values())