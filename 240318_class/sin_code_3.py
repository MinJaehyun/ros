import matplotlib.pyplot as plt
import numpy as np

# 드디어 class의 시작
class DrawSin:
    def __init__(self, amp, freq, bias, end_time):
        self.amp = amp
        self.freq = freq
        self.bias = bias
        self.end_time = end_time

    # 삼각 함수 설정 
    def calc_sin(self):
        self.t = np.arange(0, self.end_time, 0.01)
        return self.amp * np.sin(2 * np.pi * self.freq * self.t) + self.bias

    def draw_sin(self):
        y = self.calc_sin()
        plt.figure(figsize=(12, 6))
        plt.plot(self.t, y)
        plt.grid()
        plt.show()


# ds = DrawSin(1, 1, 0, 3)
# ds.draw_sin()

# 모든 코드는 ipynb에서 실행하기!