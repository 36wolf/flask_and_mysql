# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import pyopenjtalk
from scipy.io import wavfile
import numpy as np
x, sr = pyopenjtalk.tts("おめでとうございます")
wavfile.write("test.wav", sr, x.astype(np.int16))


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
