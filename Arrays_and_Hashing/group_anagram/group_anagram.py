def groupAnagrams(strs):
        sorted_ana = {}

        for string in strs:
            sorted_list = ''.join(sorted(string))
            if sorted_list not in sorted_ana:
                sorted_ana[sorted_list] = []
            sorted_ana[sorted_list].append(string)

        return list(sorted_ana.values())

if __name__ == "__main__":
    strs = list(map(str, input().split()))
    print(groupAnagrams(strs))
