import matplotlib.pyplot as plt
import numpy as np

# origin class
class DrawSin:
    def __init__(self, amp, freq, bias, end_time):
        self.amp = amp
        self.freq = freq
        self.bias = bias
        self.end_time = end_time

    def calc_sin(self):
        self.t = np.arange(0, self.end_time, 0.01)
        return self.amp * np.sin(2 * np.pi * self.freq * self.t) + self.bias

    def draw_sin(self):
        y = self.calc_sin()
        plt.figure(figsize=(12, 6))
        plt.plot(self.t, y)
        plt.grid()
        plt.show()


# class_inheritance
class DrawSinusoidal(DrawSin):
  def calc_cos(self):
    self.t = np.arange(0, self.end_time, 0.01)
    return self.amp * np.cos(2*np.pi * self.freq * self.t) + self.bias

  def draw_cos(self):
    y = self.calc_cos()
    plt.figure(figsize=(12,6))
    plt.plot(self.t, y)
    plt.grid()
    plt.show()


# method overriding
class DrawSinusoidal2(DrawSinusoidal):
  # DrawSin 내 draw_sin method overriding
  def draw_sin(self):
    y = self.calc_sin()
    plt.figure(figsize=(12,6))
    plt.plot(self.t, y)
    plt.title('Sin Graph')
    plt.ylabel('Sin')
    plt.xlabel('time (sec)')
    plt.grid()
    plt.show()


# dc = DrawSinusoidal(1, 1, 0, 3)
# dc.__dict__
# dc.__dir__()
# dc.draw_cos()
# dc.draw_sin()


# super class
class DrawSinusoidal3(DrawSinusoidal2):
  def __init__(self, amp, freq, bias, end_time, ts):  # ts를 새로 추가
    self.ts = ts

      
# ds3 = DrawSinusoidal3(1, 1, 0, 3, 0.01)
# dc.__dict__
# dc.__dir__()
# dc.draw_cos()
# dc.draw_sin()