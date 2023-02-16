from PyQt5.QtGui import QFontDatabase

font_database = QFontDatabase()

# 获取所有字体
fonts = font_database.families()

# 打印字体列表
print(fonts)