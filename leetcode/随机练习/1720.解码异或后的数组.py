# encoding = utf-8
# 未知 整数数组 arr 由 n 个非负整数组成。
# 经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。
# 给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。
# 请解码返回原数组 arr 。可以证明答案存在并且是唯一的。


# encode[i] = arr[i]^a[i+1] ->a[i+1] = encode[i]^arr[i]
class Solution:
    def decode(self, encoded, first):
        arr = [first]
        for i in encoded:
            arr.append(arr[-1] ^ i)
        return arr
s = Solution()
print(s.decode([1,2,3],1))

