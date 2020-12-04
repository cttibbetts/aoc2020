#!/usr/bin/env python3
import re

with open("input.txt") as file:
    input = [line.strip() for line in file.readlines()]

SAMPLE = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
""".strip().split(
    "\n"
)

INVALIDS = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
""".strip().split(
    "\n"
)

VALIDS = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
""".strip().split(
    "\n"
)


def valid_hgt(x):
    unit = x[-2:]
    if unit == "cm" and 150 <= int(x[:-2]) <= 193:
        return True
    if unit == "in" and 59 <= int(x[:-2]) <= 76:
        return True
    return False


eye_cols = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

field_valid = {
    "byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": valid_hgt,
    "hcl": lambda x: bool(re.match(r"^#[0-9a-f]{6}$", x)),
    "ecl": lambda x: x in eye_cols,
    "pid": lambda x: bool(re.match(r"^[0-9]{9}$", x)),
}


def get_passports(input):
    pp = {}
    for line in input:
        if line == "":
            yield pp
            pp = {}
            continue

        words = line.split(" ")
        for word in words:
            kv = word.split(":")
            pp[kv[0]] = kv[1]
    yield pp


def valid_passport(passport, validate=False):
    for f in field_valid.keys():
        if f not in passport:
            return False
        if validate:
            func = field_valid.get(f)
            val = passport.get(f)
            if not func(val):
                return False
    return True


def solve1(input):
    count = 0
    for pp in get_passports(input):
        if valid_passport(pp):
            count += 1
    return count


def solve2(input):
    count = 0
    for pp in get_passports(input):
        if valid_passport(pp, validate=True):
            count += 1
    return count


if __name__ == "__main__":
    # Tests
    assert solve1(SAMPLE) == 2
    assert solve2(INVALIDS) == 0
    assert solve2(VALIDS) == 4

    assert field_valid["byr"]("2002")
    assert not field_valid["byr"]("2003")
    assert field_valid["hgt"]("60in")
    assert field_valid["hgt"]("190cm")
    assert not field_valid["hgt"]("190in")
    assert not field_valid["hgt"]("190")
    assert field_valid["hcl"]("#123abc")
    assert not field_valid["hcl"]("#123abz")
    assert not field_valid["hcl"]("123abc")
    assert field_valid["ecl"]("brn")
    assert not field_valid["ecl"]("wat")
    assert field_valid["pid"]("000000001")
    assert not field_valid["pid"]("0123456789")

    # Part 1
    part1 = solve1(input)
    assert part1 == 230

    # Part 2
    part2 = solve2(input)
    assert part2 == 156
    print(part2)
