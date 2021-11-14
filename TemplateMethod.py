"""
模板方法
    定义了一个算法的骨架，而将一些步骤延迟到子类中，模版方法使得子类可以在不改变算法结构的情况下，重新定义算法的步骤。

需求：
    本公司有程序猿、测试、HR、项目经理等人，下面使用模版方法模式，记录下所有人员的上班情况
"""
import time


class Worker(object):

    def __init__(self, name):
        self.name = name

    def work_one_day(self):
        print("WORK START")
        self._enter_company()
        self._computer_on()
        self.work()
        self._computer_off()
        self._exit_company()
        print("WORK END")

    # 抽象方法, 需要子类实现
    def work(self):
        pass

    def is_need_print_date(self) -> bool:
        """勾子方法"""
        return False

    def _exit_company(self):
        if self.is_need_print_date():
            print("离开公司, ", time.strftime("%Y-%m-%d %H:%M"))
        print(self.name, "离开公司")

    def _computer_on(self):
        print("打开电脑")

    def _computer_off(self):
        print("关闭电脑")

    def _enter_company(self):
        print("进入公司")


class Programmer(Worker):

    def work(self):
        print("写一天的代码")

    def is_need_print_date(self) -> bool:
        return True


class HRWork(Worker):

    def work(self):
        print("招了一天的人")


if __name__ == '__main__':
    hr = HRWork("翠花")
    programmer = Programmer("张三")

    hr.work_one_day()
    programmer.work_one_day()
