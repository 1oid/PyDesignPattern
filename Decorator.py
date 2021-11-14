"""
装饰者模式
    若要扩展功能，装饰者提供了比集成更有弹性的替代方案，动态地将责任附加到对象上。
    当我们设计好了一个类，我们需要给这个类添加一些辅助的功能，并且不希望改变这个类的代码
"""


class IEquip:
    """
    装备接口
    可以实现 武器、护腕、鞋子、戒指
    """

    def caculate_attack(self) -> int:
        """
        计算攻击力
        :return:
        """
        return 0

    def description(self) -> str:
        """
        装备的描述
        :return:
        """
        return ""


class ArmEquip(IEquip):
    """
    武器
    攻击力 20
    """
    def caculate_attack(self):
        return 20

    def description(self) -> str:
        return "神之右手"


class IEuipDecorator(IEquip):

    """
    装饰品接口
    """
    pass


class BlueGemDecorator(IEuipDecorator):
    """
    蓝宝石装饰品
    攻击力 +5
    和武器不一样，它可以叠加
    """

    def __init__(self, i_equip: IEquip):
        self.i_equip = i_equip

    def caculate_attack(self):
        return 5 + self.i_equip.caculate_attack()

    def description(self) -> str:
        return self.i_equip.description() + "+ 蓝宝石"


class RedGemDecorator(IEuipDecorator):
    """
    红宝石装饰品
    攻击力 +10
    和武器不一样，它可以叠加
    """

    def __init__(self, i_equip: IEquip):
        self.i_equip = i_equip

    def caculate_attack(self):
        return 10 + self.i_equip.caculate_attack()

    def description(self) -> str:
        return self.i_equip.description() + " + 红宝石"


if __name__ == '__main__':
    # 两个红宝石 + 一个蓝宝石 + 一把武器
    i_equip = BlueGemDecorator(
        RedGemDecorator(RedGemDecorator(ArmEquip()))
    )

    print("攻击力: ", i_equip.caculate_attack())
    print("装备: ", i_equip.description())
