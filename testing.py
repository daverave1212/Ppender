import win32clipboard as cb
import sys


hdrop = cb.CF_HDROP
cb.OpenClipboard()

print(cb.IsClipboardFormatAvailable(hdrop))

cb.CloseClipboard()
sys.exit()
#########

data = cb.GetClipboardData()



format_name = cb.GetClipboardFormatName(data)
print(format_name)
data = cb.GetClipboardData(hdrop)

cb.CloseClipboard()

