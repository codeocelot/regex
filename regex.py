"""
. matches any single character
* matches zero or more of the preceeding char

isMatch('aa','a') => false
isMatch('aa','aa') => true
isMatch('aa', 'a*') => true
isMatch("aa", ".*") => true
isMatch("ab", ".*") => true
"""


def isMatch(string, pattern):
    """
    The approach is to keep greedly move forward in both arrays, iteratively
    applying a turning machine-esque logic.

    - A matching char or `.` advances both the string and pattern indexes.
    - A * will pull the pattern index back 1, and start again from the top.
    - If it doesn't match, then maybe we hit *'s base case, if so, then jump
    ahead 2 slots to pass the *.

    The entire algorithm has only two base cases:
    - the pattern exhausts before the string has been fully read.
    - the string is fully read, in which case the string matches.
    :param string:
    :type string: str
    :param pattern:
    :type string: str
    :return: boolean
    """
    str_idx = 0
    pattern_idx = 0
    while str_idx < len(string):

        if pattern_idx > len(pattern) - 1:
            return False

        str_char = string[str_idx]
        pattern_char = pattern[pattern_idx]

        if str_char == pattern_char:
            str_idx += 1
            pattern_idx += 1
            continue
        elif pattern_char == '.':
            str_idx += 1
            pattern_idx += 1
            continue

        if pattern_char == '*':
            pattern_idx -= 1
            continue

        """ lookahead for * """
        if pattern_idx < len(pattern) - 1:
            next_pattern_char = pattern[pattern_idx + 1]
            if next_pattern_char == '*':
                pattern_idx += 2

    return True


assert(isMatch("ab", ".....") is True)
assert(isMatch("aa", 'a') is False)
assert(isMatch("aa", 'a*') is True)
assert(isMatch('aaa', 'aa') is False)
assert(isMatch('aa', 'a*') is True)
assert(isMatch('aa', '.*') is True)
assert(isMatch('ab', '.*') is True)
assert(isMatch('aab', 'c*a*b') is True)
assert(isMatch('cccaaab', 'c*a*b') is True)
assert(isMatch('cab', 'c*a*b') is True)
assert(isMatch('b', 'c*a*b') is True)
