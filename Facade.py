"""
hello
外观模式
    提供一个统一的接口，用来访问子系统中的一群接口，外观定义了一个高层的接口，让子系统更容易使用。
其实就是为了方便客户的使用，把一群操作，封装成一个方法。

需求：
    我比较喜欢看电影，于是买了投影仪、电脑、音响、设计了房间的灯光、买了爆米花机，
然后我想看电影的时候，我需要一键观影和一键关闭。
"""


class PopcornPopper:

    def on(self):
        print("打开爆米花机")

    def off(self):
        print("关闭爆米花机")

    def make_popcorn(self):
        print("制作爆米花")


class Computer:

    def on(self):
        print("打开电脑")

    def off(self):
        print("关闭电脑")


class HomeTheaterFacade:
    """
    家庭影院
    """

    def __init__(self, computer: Computer, popcorn: PopcornPopper):
        self.computer = computer
        self.popcorn = popcorn

    def watch_movie(self):
        self.popcorn.on()
        self.popcorn.make_popcorn()

        self.computer.on()

    def stop_movie(self):
        self.computer.off()
        self.popcorn.off()


if __name__ == '__main__':
    HomeTheaterFacade(Computer(), PopcornPopper()).watch_movie()
