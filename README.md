[![PyPI](https://img.shields.io/pypi/v/proxies.svg?maxAge=2592000)](https://pypi.python.org/pypi/proxies)
[![PyPI](https://img.shields.io/pypi/dm/proxies.svg?maxAge=2592000)](https://pypi.python.org/pypi/proxies)
[![PyPI](https://img.shields.io/pypi/pyversions/proxies.svg?maxAge=2592000)](https://pypi.python.org/pypi/proxies)
[![PyPI](https://img.shields.io/pypi/l/proxies.svg?maxAge=2592000)](https://pypi.python.org/pypi/proxies)
[![PyPI](https://img.shields.io/pypi/status/proxies.svg?maxAge=2592000)](https://pypi.python.org/pypi/proxies)

## 获取最新的HTTP代理
#### 安装
```
pip install proxies
```

> OR:

```
git clone https://github.com/MyFaith/proxies
python setup.py install
```

#### 使用
```
from Proxies import Proxies

p = Proxies()
p.get_proxies(20, 1)
# quantity: 数量
# type: 类型 (1.国内高匿代理 2.国内普通代理 3.国外高匿代 4.国外普通代理)
result = p.get_result()
print(result)
```
