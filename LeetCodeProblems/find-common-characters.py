'''
Input: ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
Output: []

dict = {'a': 2, 'c': 2, 'b':1, 'd':3}

check 2nd word
dict1 = {'b': 4, 'c': 2, 'd': 2}

compare and take minimums:

dict1 = {'b': 1, 'c': 2, }

Build - compare - take min vals
dict1= {'b': 3, 'a': 2, 'd': 3}



'''



class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        dict = self.getDictionary(A)
        lst = []
        for key in dict.keys():
            for i in range(dict[key]):
                lst.append(key)

        return lst

    def getDictionary(self, A):
        dary = {}

        for i in range(len(A)):
            word = A[i]
            if i == 0:
                for j in range(len(word)):
                    ind = word[j]
                    if ind in dary:
                        dary[ind] = dary[ind] + 1
                    else:
                        dary[ind] = 1
            else:
                dict2 = {}
                for j in range(len(word)):
                    if word[j] in dict2:
                        dict2[word[j]] = dict2[word[j]] + 1
                    else:
                        dict2[word[j]] = 1
                dict = {}
                print(dary)
                print(dict2)
                for key in dict2.keys():
                    if key in dary and key in dict2:
                        dict[key] = min(dary[key], dict2[key])
                dary = dict

                print(dary)
        return dary


obj = Solution()
A = ["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]

obj.commonChars(A)
