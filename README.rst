## 获取最新的HTTP代理
---------------------

安装
^^^^

::

    pip install proxies

    OR:

::

    git clone https://github.com/MyFaith/proxies
    python setup.py install

使用
^^^^

::

    from Proxies import Proxies

    p = Proxies()
    p.get_proxies(20, 1)
    # quantity: 数量
    # type: 类型 (1.国内高匿代理 2.国内普通代理 3.国外高匿代 4.国外普通代理)
    result = p.get_result()
    print(result)
