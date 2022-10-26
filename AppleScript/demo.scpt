# 变量
# 数字
set x to 25
set x to x+15
# list
set exampleList to {100, 200.0, "300", -10}
get item 1 of exampleList
get item -1 of exampleList
get length of exampleList
set item 3 of exampleList to "3"
#record
set myRecord to {name:"exchen", blog:"https://www.exchen.net", body:"hehe"}
set myName to get name of myRecord
# 字符串
set str to "hello apple"
get length of str

set domainName to "www.exchen.net"
if domainName contains "exchen" then
  display dialog "包含 exchen"
else
  display dialog "不包含 exchen"
end if

# 拼接字符串
set str to "hello apple" & " nihao"
# 拼接数组
set exampleList to {100, 200.0, "300", -10} & {10}

# 弹窗
display alert str
# 对话框
display dialog myName
try
# 用户取消，出异常
  display dialog "是否同意用户协议？"
  display alert "让我们继续愉快的玩耍"
on error
  display alert "呜呜呜，你不要我了"
end try

# if else
if x > 25 then
  display alert "x > 25"
else
  display alert "x < 25"
  # 必须的
end if

# 循环
set sum to 0
repeat 100 times
  set sum to sum + 1
end repeat
get sum

repeat with counter from 0 to 10 by 2
  display alert counter
end repeat

repeat with myIt in exampleList
  display alert myIt
end repeat

# 函数
on getSum(numList)
  set sum to 0
  repeat with myIt in numList
    set sum to sum + myIt
  end repeat
  return sum
end getSum

set sum to getSum({1,221,20,15})
display alert "sum = " & sum

# 异常
try
  set x to 1 / 0
on error the error_message number the error_number
  display dialog "Error: " & the error_number & "." & the error_message buttons {"OK"}
end try

