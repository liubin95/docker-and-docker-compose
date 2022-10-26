tell application "WeChat" to activate
tell application "System Events"
  key code 3 using {command down}
  keystroke "mbqst"
  delay 2
  -- 回车
  keystroke return
  keystroke 1 using {command down}
  keystroke "v" using {command down}
  keystroke return
end tell