"""
* Assignment: Str Methods Normalize
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Use `str` methods to clean `DATA`
    2. Run doctests - all must succeed

Polish:
    1. Wykorzystaj metody `str` do oczyszczenia `DATA`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result
    'Jana Twardowskiego III'
"""

DATA = 'UL. jana \tTWArdoWskIEGO 3'

# str: Jana Twardowskiego III
result = DATA.replace('UL. ', '').replace('\t', '').title().replace('3', 'III')