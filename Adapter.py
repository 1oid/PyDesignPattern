"""
适配器模式
    将一个类的接口转换成客户期望的另一个接口，
适配器让原本接口不兼容的类可以相互合作。把一个接口转成另一个接口。
"""


class V5Power(object):
    power = 5

    def provide_v5_power(self) -> int:
        return 5


class V220Power(object):
    power = 5

    def provide_v220_power(self) -> int:
        print("提供220v家用电")
        return 220


class V5PowerAdapter(V5Power):

    _v220_power = 0

    def __init__(self, v220power: V220Power):
        self._v220_power = v220power.provide_v220_power()

    def provide_v5_power(self) -> int:
        print("适配器，经过复杂操作，将", str(self._v220_power) + "电压转为5v")
        return 5


class Mobile(object):

    def input_power(self, v5power: V5Power):
        provide_v5_power = v5power.provide_v5_power()
        print("手机接入电源，需要电压5V, 现在接入电压为", str(provide_v5_power))


if __name__ == '__main__':
    mobile = Mobile()
    v5power = V5PowerAdapter(V220Power())
    mobile.input_power(v5power)
