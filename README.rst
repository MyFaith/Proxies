|PyPI| |PyPID| |PyPIV| |PyPIL| |PyPIS|

Get latest http proxies
------------------

Install
^^^^

::

    pip install proxies

    OR:

::

    git clone https://github.com/MyFaith/proxies
    python setup.py install

Usage
^^^^

::

    from Proxies import Proxies

    p = Proxies()
    p.get_proxies(20, 1)
    result = p.get_result()
    print(result)

.. |PyPI| image:: https://img.shields.io/pypi/v/proxies.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/proxies
.. |PyPID| image:: https://img.shields.io/pypi/dm/proxies.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/proxies
.. |PyPIV| image:: https://img.shields.io/pypi/pyversions/proxies.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/proxies
.. |PyPIL| image:: https://img.shields.io/pypi/l/proxies.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/proxies
.. |PyPIS| image:: https://img.shields.io/pypi/status/proxies.svg?maxAge=2592000
   :target: https://pypi.python.org/pypi/proxies
