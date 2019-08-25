from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number):
    mnemonic_map = ['0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    result = []

    def make_mnemonics(digit):
        if digit == len(phone_number):
            mnemonics.append(''.join(partial_mnemonic))
            return

        for i in mnemonic_map[int(phone_number[digit])]:
            partial_mnemonic[digit] = i
            make_mnemonics(digit + 1)

    mnemonics, partial_mnemonic = [], [0] * len(phone_number)
    make_mnemonics(0)
    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
