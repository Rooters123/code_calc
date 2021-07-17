# encoding = utf-8
class Solution:
    def longestCommonPrefix(self, strs):
        # 自己的解法
        # index_list = []
        # for i in strs:
        #     index_list.append(len(i))
        # min_index = index_list.index(min(index_list))
        # for j in range(len(strs[min_index])):
        #     sets = [strs[x][j] for x in range(len(strs))]
        #     if len(set(sets)) != 1 :
        #         return strs[min_index][:j]
        # return strs[min_index]

        # 官方解答之一
        # 这里有一点不同的是，官方解法是没有先去找数组中字符最少的那个索引，而是默认了第一个元素
        # lens = len(strs[0])
        # count = len(strs)
        # for i in range(lens):
        #     if any(i == len(strs[j]) or strs[j][i] !=strs[0][i] for j in range(1,count)):
        #         return strs[:i]
        # return strs[0]
        # 解法3：

        res = ""
        for tmp in zip(*strs):
            print(tmp)
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res

s= Solution()
alist = ["a0ows","b0ow","al0wxas"]
print(s.longestCommonPrefix(alist))

# print(zip(*alist))
