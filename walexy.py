class Solution:
    def reverseOnlyLetters(self, S):
        if not S:
            return S
        str_ = ""
        index1 = 0
        index2 = len(S)-1
        while index1<len(S):
            #print(index1,index2)
            if index2 >=0 and S[index1].isalpha() and S[index2].isalpha():
                str_ +=S[index2]
                index1 -= 1
                index2 += 1
            elif S[index1].isalpha():
                index2 -= 1
            elif not S[index1].isalpha():
                str_ += S[index1]
                index1 +=1
            else:
                index2 -= 1
                index1 += 1
        return str_
ob1 = Solution()    
print(ob1.reverseOnlyLetters("a-bC-dEf-ghIj"))