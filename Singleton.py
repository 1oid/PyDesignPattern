"""
单例模式
    单例模式主要是为了避免因为创建了多个实例造成资源的浪费，
且多个实例由于多次调用容易导致结果出现错误，而使用单例模式能够保证整个应用中有且只有一个实例。

    饿汉模式
    懒汉模式（推荐）
"""


class SingletonEHan(object):

    class _Ehan:
        pass

    _ehan = _Ehan()

    def _singleton_Ehan(self) -> _Ehan:
        return self._ehan

    def get_instance(self):
        return self._singleton_Ehan()


class SingletonLanHan(object):

    class _LanHan:
        pass

    _lanhan = None

    def get_instance(self):
        """
        这里相比饿汉式，如果在多线程中，可能会由于条件竞争使对象为空，这时候懒汉式在为空的时候新建对象
        :return:
        """
        if self._lanhan is None:
            self._lanhan = self._LanHan()
        return self._lanhan

    def set_instance(self, o):
        self._lanhan = o


if __name__ == '__main__':
    # 饿汉模式
    single_ehan = SingletonEHan()
    print(single_ehan.get_instance())

    # 懒汉式
    single_lanhan = SingletonLanHan()
    single_lanhan.set_instance(None)
    print(single_lanhan.get_instance())
