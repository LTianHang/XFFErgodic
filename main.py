# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


ipa = 172
ipb = 172
ipc = 172
ipd = 172

ip = ""
file = open("all_ip.txt", mode="w")
for a in range(ipa, 1, -1):
    for b in range(ipb, 1, -1):
        for c in range(ipc, 1, -1):
            for d in range(ipd, 1, -1):
                ip = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
                file.write(ip + "\n")
file.close()
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
