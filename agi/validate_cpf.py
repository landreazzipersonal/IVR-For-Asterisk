#!/usr/bin/env python3
import re
import sys


def read_agi_env():
    env = {}
    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            env[key.strip()] = value.strip()
    return env


def agi_write(command: str):
    sys.stdout.write(f"{command}\n")
    sys.stdout.flush()
    return sys.stdin.readline().strip()


def agi_set_variable(name: str, value: str):
    agi_write(f'SET VARIABLE {name} "{value}"')


def agi_verbose(message: str, level: int = 1):
    safe = message.replace('"', '\\"')
    agi_write(f'VERBOSE "{safe}" {level}')


def normalize_cpf(value: str) -> str:
    return re.sub(r"\D", "", value or "")


def is_repeated_sequence(cpf: str) -> bool:
    return cpf == cpf[0] * len(cpf)


def calculate_digit(cpf_partial: str) -> str:
    weight = len(cpf_partial) + 1
    total = sum(int(num) * (weight - idx) for idx, num in enumerate(cpf_partial))
    remainder = (total * 10) % 11
    return "0" if remainder == 10 else str(remainder)


def validate_cpf(cpf: str) -> bool:
    cpf = normalize_cpf(cpf)

    if len(cpf) != 11:
        return False

    if not cpf.isdigit():
        return False

    if is_repeated_sequence(cpf):
        return False

    digit_1 = calculate_digit(cpf[:9])
    digit_2 = calculate_digit(cpf[:9] + digit_1)

    return cpf[-2:] == digit_1 + digit_2


def main():
    read_agi_env()

    cpf_input = ""
    if len(sys.argv) > 1:
        cpf_input = sys.argv[1]

    cpf = normalize_cpf(cpf_input)

    if not cpf:
        agi_verbose("No CPF received", 1)
        agi_set_variable("CPF_VALIDO", "NAO")
        agi_set_variable("CPF_NORMALIZADO", "")
        sys.exit(0)

    is_valid = validate_cpf(cpf)

    agi_set_variable("CPF_NORMALIZADO", cpf)
    agi_set_variable("CPF_VALIDO", "SIM" if is_valid else "NAO")

    agi_verbose(f"CPF validation result for {cpf}: {'SIM' if is_valid else 'NAO'}", 1)
    sys.exit(0)


if __name__ == "__main__":
    main()
