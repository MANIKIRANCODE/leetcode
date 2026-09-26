class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for  i in range(0,len(letters)):
            if ord(letters[i]) > ord(target):
                print(letters[i])
                return letters[i]
                
           
        return letters[0]