from collections import OrderedDict


def _build_counts_map(string):
    counts_map = OrderedDict()
    for char in string:
        if char in counts_map:
            counts_map[char] += 1
        else:
            counts_map[char] = 1
    return counts_map


def find_power_set(string):
    if string is None:
        return string
    if string == '':
        return ['']
    counts_map = _build_counts_map(string)
    curr_results = []
    results = []
    _find_power_set(counts_map, curr_results,
                         results, index=0)
    results.append('')
    return results


def _find_power_set(counts_map, curr_result,
                    results, index):
    for curr_index, char in enumerate(counts_map):
        if curr_index < index or counts_map[char] == 0:
            continue
        curr_result.append(char)
        counts_map[char] -= 1
        results.append(''.join(curr_result))
        _find_power_set(counts_map, curr_result,
                             results, curr_index)
        counts_map[char] += 1
        curr_result.pop()