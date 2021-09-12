"""
* Assignment: Conditional Statement IP
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. To `result: bool` assign whether `IP_ADDRESS` is IPv4 or IPv6 protocol
       a. `IPv4` if dot `.` is in the IP address
       b. `IPv6` if dot `.` is not in the IP address
    3. Use one line `if`
    4. Run doctests - all must succeed

Polish:
    1. Do `result: bool` przypisz czy `IP_ADDRESS` jest protokołu IPv4 czy IPv6
       a. `IPv4` jeżeli jest kropka `.` w adresie IP
       b. `IPv6` jeżeli kropki nie ma
    2. Wykorzystaj jednolinikowego `if`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> result
    'IPv4'
"""

IP_ADDRESS = '127.0.0.1'

# str: Whether 'Adult' or 'Young'
result = "IPv4" if "." in IP_ADDRESS else "IPv6"
