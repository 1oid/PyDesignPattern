"""
命令模式
    将“请求”封装成对象，以便使用不同的请求、队列或者日志来参数化其他对象。命令模式也支持可撤销的操作。
    即 将请求封装成对象，将动作请求者和动作执行者解耦。
"""


class Door:

    def open(self):
        print("打开门")

    def close(self):
        print("关闭门")


class Light:

    def open(self):
        print("打开灯")

    def close(self):
        print("关闭灯")


class ICommand(object):

    def execute(self):
        pass


class DoorOpenCommand(ICommand):

    def __init__(self, door: Door):
        self.door = door

    def execute(self):
        self.door.open()


# 总控制按钮
class ControlPanel(object):

    # 9个按钮
    _control_size = 9
    commands = []

    def __init__(self):
        for i in range(9):
            self.commands.append(None)

    def set_command(self, index, command: ICommand):
        self.commands[index] = command

    def key_pressed(self, index):
        self.commands[index].execute()


if __name__ == '__main__':
    control_panel = ControlPanel()
    control_panel.set_command(0, DoorOpenCommand(Door()))
    control_panel.key_pressed(0)
