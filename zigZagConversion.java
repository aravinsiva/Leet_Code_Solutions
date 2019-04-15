class Solution {
    public String convert(String s, int numRows) {
        if(s == null || s.length() == 0)    return "";
        char[] charArr = s.toCharArray();
        char[] output = new char[charArr.length];
        int counter = 0;
        boolean flag = true;
        // Handling one edge case
        if(numRows == 1)  return s;
        for(int i = 0; i < numRows; i++) {
            int curIndex = i;
            flag = true;
            while(curIndex < charArr.length && counter < charArr.length) {
                output[counter++] = charArr[curIndex];
                // First and last rows are handled seperately since they dont need to switch
                if(i == numRows - 1 || i == 0)  curIndex += (numRows - (1))*2;
                // The rest of rows switch symmetrically thanks to a boolean value
                else    {
                    curIndex += flag ? (numRows - (i + 1))*2 : (i)*2;
                    flag = !flag;
                }
            }
        }
        return new String(output);
    }
}