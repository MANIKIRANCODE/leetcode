class Solution {
    public boolean isPalindrome(int x) {
        int result = 0 , digits;
        int temp = x;
        if(x < 0){
            return false;
        }
        while(x !=0){
            digits = x%10;
            result = (result*10) + digits;
            x = x/10;

        } 
        
        return result == temp;
    }
}