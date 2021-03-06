"""
* Assignment: Mapping Dict Translate
* Required: no
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Ask user to input single letter
    2. Convert to lowercase
    3. If letter is in `PL` then use conversion value as letter
    4. `MagicMock` will simulate inputting of a letter by user
    5. Use `input()` function as normal
    6. Run doctests - all must succeed

Polish:
    1. Poproś użytkownika o wprowadzenie jednej litery
    2. Przekonwertuj literę na małą
    3. Jeżeli litera jest w `PL` to użyj skonwertowanej wartości jako litera
    4. `MagicMock` zasymuluje wpisanie litery przez użytkownika
    5. Skorzytaj z funkcji `input()` tak jak normalnie
    6. Uruchom doctesty - wszystkie muszą się powieść

Example:
    | Input | Output |
    |-------|--------|
    |   A   |    a   |
    |   x   |    x   |
    |   Ł   |    ł   |
    |   ś   |    s   |
    |   Ź   |    z   |

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> import string

    >>> type(result)
    <class 'str'>
    >>> result not in PL.keys()
    True
    >>> result in string.ascii_letters
    True
"""

from unittest.mock import MagicMock


# Simulate user input (for test automation)
input = MagicMock(side_effect=['Ł'])

PL = {'ą': 'a', 'ć': 'c', 'ę': 'e',
      'ł': 'l', 'ń': 'n', 'ó': 'o',
      'ś': 's', 'ż': 'z', 'ź': 'z'}

# str: with letter from user
letter = input("Podaj literę").strip().lower()

# str: with converted letter without PL diacritic chars
result = PL.get(letter, letter)
print(result)