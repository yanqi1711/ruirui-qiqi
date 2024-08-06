from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if not list1 or not list2:
            return None
        min_index = float('inf')
        list1Dict = {}
        for i in range(len(list1)):
            list1Dict[list1[i]] = i 
        for j in range(len(list2)):
            if list2[j] in list1Dict:
                if j+list1Dict[list2[j]] < min_index:
                    min_index = j+list1Dict[list2[j]]
                    ans = [list2[j]]
                elif j+list1Dict[list2[j]] == min_index:
                    ans.append(list2[j])
                else:
                    continue
        return ans