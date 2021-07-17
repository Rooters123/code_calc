# encoding = utf-8
# 有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。
# 对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。
# 并返回一个包含给定查询 queries 所有结果的数组。
# 输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# 输出：[2,7,14,8]
class Solution:
    # 这种是暴力破解，是过不了leetcode的，因此需要优化
    # def xorQueries(self, arr, queries):
    #     new_list = []
    #     for i in range(len(queries)):
    #         # print(queries[i][0] ^ queries[i][1])
    #         base_num = 0
    #         start = queries[i][0]
    #         end = queries[i][1]
    #         while start <= end:
    #             base_num = base_num ^ arr[start]
    #             start += 1
    #         new_list.append(base_num)
    #     return new_list
    #

    # 优化点在于如果queries中数组长度很长，那么在遍历的时候，需要一次次的去进行异或运算
    # 我们可以通过一次异或运算记录arr数组的计算，并以此推断，从start-end之间的关系
    def xorQueries(self, arr, queries):
        xors = [0]
        for i in arr:
            xors.append(xors[-1] ^ i)
        for start,end in queries:
            return xors[start] ^ xors[end + 1]
s = Solution()
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(s.xorQueries(arr,queries))