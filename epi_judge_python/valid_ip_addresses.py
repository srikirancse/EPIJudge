from test_framework import generic_test

def get_valid_ip_address(s):
    result, valid_parts = [], [None] * 4

    def is_valid_part(part):
        return len(part) == 1 or (part[0] != '0' and int(part) <= 255)

    for i in range(1, min(4, len(s))):
        valid_parts[0] = s[:i]
        if is_valid_part(valid_parts[0]):
            for j in range(1, min(i + 4, len(s) - i)):
                valid_parts[1] = s[i : i + j]
                if is_valid_part(valid_parts[1]):
                    for k in range(1, min(j + 4, len(s) - i - j)):
                        valid_parts[2] = s[i + j : i + j + k]
                        valid_parts[3] = s[i + j + k :]
                        if is_valid_part(valid_parts[2]) and is_valid_part(valid_parts[3]):
                            result.append('.'.join(valid_parts))

    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
