# encoding = utf-8
# 给出一个字符串 s（仅含有小写英文字母和括号）。
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
# 注意，您的结果中 不应 包含任何括号。
def reverse(str):
    # 括号处理一般使用栈来进行转置
    stack = []
    for i in range(len(str)):
        if str[i] != ')':
            stack.append(str[i])
        else:
            tep = []
            while stack and  stack[-1] != '(':
                tep.append(stack.pop())
            # 去除'('
            if stack:
                stack.pop()
            stack += tep
    return stack
print(reverse("(abc(def))"))


