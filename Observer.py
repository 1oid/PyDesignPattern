"""
观察者模式
    定义了对象之间的一对多的依赖，这样一来，当一个对象改变时，它的所有的依赖者都会收到通知并自动更新。
"""


class Observer:

    def update(self, msg):
        print("Update Message,", msg)


class IObserver(object):

    def register_observer(self, o: Observer):
        """
        注册一个观察者
        :param o:
        :return:
        """
        pass

    def remove_observer(self, o: Observer):
        """
        移除一个观察者
        :param o:
        :return:
        """
        pass

    def notify_observer(self):
        """
        通知所有观察者
        :return:
        """
        pass


class ObserverRunner(IObserver):
    """
    实现类
    """

    observers = []
    msg = ""

    def register_observer(self, o: Observer):
        self.observers.append(o)

    def remove_observer(self, o: Observer):
        if self.observers.index(o):
            self.observers.remove(o)

    def notify_observer(self):
        for o in self.observers:
            o.update(self.msg)

    def set_message(self, msg: str):
        self.msg = msg
        self.notify_observer()


class ObserverUser1(Observer):
    """
    模拟第一个使用者
    """
    def __init__(self, runner: ObserverRunner):
        runner.register_observer(self)

    def update(self, msg):
        print("我是Obserserver1", msg)


class ObserverUser2(Observer):
    """
    模拟第二个使用者
    """
    def __init__(self, runner: ObserverRunner):
        runner.register_observer(self)

    def update(self, msg):
        print("我是Obserserver2", msg)


if __name__ == '__main__':
    runner = ObserverRunner()

    # 创建两个订阅者(观察者)
    observer_user_1 = ObserverUser1(runner)
    observer_user_2 = ObserverUser2(runner)

    # 两个观察者，发送两条消息
    runner.set_message("observer_user_1, ID: 1")
    runner.set_message("observer_user_2, ID: 2")

