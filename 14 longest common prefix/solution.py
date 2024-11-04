from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """
    Returns the longest common prefix of a list of strings
    >>> longest_common_prefix(["flower","flow","flight"])
    :param strs:
    :return:
    """
    if not strs:
        return ""

    prefix = strs[0]
    for i in range(len(prefix)):
        for word in strs[1:]:
            if i >= len(word) or word[i] != prefix[i]:
                return prefix[:i]
    return prefix
