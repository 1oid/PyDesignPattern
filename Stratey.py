"""
策略模式
    定义了算法族，分别封装起来，让它们之间可相互替换，此模式让算法的变化独立于使用算法的客户。
    可以让客户自由定义方法

    对于每个角色的display，attack，defend，run都是有可能变化的，于是我们必须把这写独立出来
"""


class IDisplayBehavior:
    """
    行为接口
    """
    def display(self):
        pass


class IRunBehavior:
    """
    跑接口
    """
    def run(self):
        pass


class IAttackBehavior:
    """
    攻击接口
    """
    def attack(self):
        pass


class Role(object):

    name = ""
    iDisplayBehavior = None
    iRunBehavior = None
    iAttackBehavior = None

    def __init__(self, name):
        self.name = name

    def set_display_behavior(self, behavior: IDisplayBehavior):
        self.iDisplayBehavior = behavior
        return self

    def set_run_behavior(self, behavior: IRunBehavior):
        self.iRunBehavior = behavior
        return self

    def set_attack_behavior(self, behavior: IAttackBehavior):
        self.iAttackBehavior = behavior
        return self

    def display(self):
        self.iDisplayBehavior.display()

    def run(self):
        self.iRunBehavior.run()

    def attack(self):
        self.iAttackBehavior.attack()


"""
自定义方法
"""


class CustomDisplay(IDisplayBehavior):

    def display(self):
        print("自定义Display")


class CustomRun(IRunBehavior):

    def run(self):
        print("自定义Run")


class CustomAttack(IAttackBehavior):

    def attack(self):
        print("自定义Attack")


if __name__ == '__main__':
    role = Role("张三")
    role.set_display_behavior(CustomDisplay())\
        .set_run_behavior(CustomRun())\
        .set_attack_behavior(CustomAttack())

    role.display()
    role.run()
    role.attack()
