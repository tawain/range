# range 範圍
# python內建功能：清單產生器
import random

range(5) # [0, 1, 2, 3, 4] 
# 5為結尾值（不包含）；未設定開始值：自動從零開始。
range(3) # [0, 1, 2]

for i in range(100):
	r = random.randint(1, 1000)
	print('第', i + 1, '次產生隨機數：', r)
# for i in range 的for loop 只是為了讓它的內容重複執行某個固定次數


# range三種用法：
#1. range(結尾值)
#2. range(開始值, 結尾值)
#3. range(開始值, 結尾值, 遞增值)
# 開始值有包含，結尾值不包含。

range(3) # [0, 1, 2]
range(2, 5) # [2, 3, 4]
range(2, 10, 3) #[2, 5, 8]
range(10, 3, -2) # [10, 8, 6, 4]




