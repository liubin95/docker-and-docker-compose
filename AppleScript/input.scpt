display notification "message" with title "title" subtitle "subtitle"
# 输入框
try
  set input to display dialog "Input a number here"  default answer 10
on error
end

# 单选
choose from list {"选项1", "选项2", "选项3"} with title "选择框" with prompt "请选择选项"

-- 选择文件夹
choose folder with prompt "指定提示信息"
-- 选取文件名称Choose File Name
choose file  with prompt "指定提示信息"
choose file  with prompt "指定提示信息" of type {"sql"}
