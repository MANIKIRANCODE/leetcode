class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        i = 0
        j = len(arr)-1
        for i in range(0,len(arr)):
            for j in range(len(arr)-1,-1,-1):
                if i != j and arr[i] == 2*arr[j]:
                    return True
                else:pass
                
        return False
