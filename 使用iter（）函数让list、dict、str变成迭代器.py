from collections.abc import Iterator

print(isinstance(iter([]),Iterator))

print(isinstance(iter('abc'),Iterator))