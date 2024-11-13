import time

def input1():
    global final_time
    try:
        time1 = int(input("你要让圈圈转多少圈呢: "))
        final_time = int(time1 * 4 + 2)
    except ValueError:
        print("我让你输入数字！", end="")
        time.sleep(1)
        print("\r搞错啦，再来！")
        time.sleep(1)
        return input1()

input1()

# final_time = pass
lst = ["\\", "|", "/", "-"]
print("加载中 ...")
for i in range(final_time):
    j = i % 4
    print("\r" + lst[j], end="")
    time.sleep(0.35)