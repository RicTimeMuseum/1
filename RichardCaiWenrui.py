global character

line = input("请输入线路名称：")
terminal_1 = input("请输入起点：")
terminal_2 = input("请输入终点：")
via = input("请输入途经地点：")
stop_cn = input("请输入第一站中文站名：")
stop_en = input("请输入第一站英文站名：")

if terminal_2:
    character = f"从{terminal_1}开往{terminal_2}"
else:
    character = f"{terminal_1}环线"

print(f"""各位乘客你们好，欢迎您乘坐{line}路公共汽车，本线路是{character}，途经{via}等地。
公交文明需要您的参与，欢迎您对我们的工作提出宝贵意见。
请坐好扶稳。前面站是：{stop_cn}。下车的乘客前准备。
The next stop is :{stop_en}. 

{stop_cn}到了，下车的乘客请带齐您的行李物品从指定门下车。
We're arriving at: {stop_en}. """)
