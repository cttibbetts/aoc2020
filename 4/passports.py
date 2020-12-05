import re


def valid_hgt(x):
    unit = x[-2:]
    if unit == "cm" and 150 <= int(x[:-2]) <= 193:
        return True
    if unit == "in" and 59 <= int(x[:-2]) <= 76:
        return True
    return False


eye_cols = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

validate_field = {
    "byr": lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    "hgt": valid_hgt,
    "hcl": lambda x: bool(re.match(r"^#[0-9a-f]{6}$", x)),
    "ecl": lambda x: x in eye_cols,
    "pid": lambda x: bool(re.match(r"^[0-9]{9}$", x)),
    # "cid": lambda x: True,
}


def validate_passport(passport, validate=True):
    for field, validator in validate_field.items():
        value = passport.get(field)
        if not value:
            return False
        if validate and not validator(value):
            return False
    return True


def read_passports(input):
    passport = {}
    for line in input:
        if not line:
            yield passport
            passport = {}
            continue

        words = line.split(" ")
        for word in words:
            kv = word.split(":")
            passport[kv[0]] = kv[1]
    yield passport


assert validate_field["byr"]("2002")
assert not validate_field["byr"]("2003")
assert validate_field["hgt"]("60in")
assert validate_field["hgt"]("190cm")
assert not validate_field["hgt"]("190in")
assert not validate_field["hgt"]("190")
assert validate_field["hcl"]("#123abc")
assert not validate_field["hcl"]("#123abz")
assert not validate_field["hcl"]("123abc")
assert validate_field["ecl"]("brn")
assert not validate_field["ecl"]("wat")
assert validate_field["pid"]("000000001")
assert not validate_field["pid"]("0123456789")
