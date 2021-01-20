'''
基于 inet.log完成
编写程序，通过输入一个端口名称（每段首个单词）
打印出这个端口描述信息中的address is 的值

提示：段落之间有空行
'''
import re

inet = open("inet.log")

#     date = ""
#     for line in inet:
#         if line == "\n":
#             break
#         date += line
#         if not date:
#             break
date = inet.read()

address = re.match("\S+", date).group()
import01 = input("请输入端口名称:")
if import01 == address:
    print(re.search("([0-9a-f]{4}\.){2}[0-9a-f]{4}", date).group())
elif import01 != date:
    print("错误")
