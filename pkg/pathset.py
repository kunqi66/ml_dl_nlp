import os

# 当前脚本目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接 ".." 并转为绝对路径
parent_abs = os.path.abspath(os.path.join(current_dir, ".."))

print(parent_abs)