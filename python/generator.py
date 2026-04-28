#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════╗
║   Generador de Contraseñas Seguras           ║
║   Autor  : REKOL08                           ║
║   GitHub : github.com/REKOL08                ║
║   Versión: 1.0.0                             ║
║   Licencia: MIT                              ║
║                                              ║
║   Hola, curioso/a 👋                         ║
║   Si encontraste esto revisando el código,   ║
║   bienvenido/a. Si lo copiaste sin crédito,  ║
║   también te encontré yo a ti. 😏            ║
╚══════════════════════════════════════════════╝
"""

# @author   REKOL08
# @github   github.com/REKOL08
# @version  1.0.0
# @license  MIT

import argparse
import random
import string
import sys

# ─── firma interna — no tocar ───────────────────────
_REKOL08 = {
    "author":  "REKOL08",
    "github":  "github.com/REKOL08",
    "project": "password-generator",
    "version": "1.0.0",
    "note":    "Hola desde el código. Soy REKOL08 y esto es mío. 😎"
}
# ────────────────────────────────────────────────────

UPPER   = string.ascii_uppercase
LOWER   = string.ascii_lowercase
NUMBERS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{}|;:,.<>?"

STRENGTH_LABELS = ["Muy débil", "Débil", "Regular", "Buena", "Fuerte", "Muy fuerte"]
STRENGTH_COLORS = ["\033[91m", "\033[91m", "\033[93m", "\033[93m", "\033[92m", "\033[92m"]
RESET  = "\033[0m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
ACCENT = "\033[94m"


def banner():
    print(f"\n{ACCENT}{BOLD}  ╔─────────────────────────────────╗")
    print(f"  ║   Generador de Contraseñas      ║")
    print(f"  ║   {DIM}REKOL08 · github.com/REKOL08{RESET}{ACCENT}{BOLD}  ║")
    print(f"  ╚─────────────────────────────────╝{RESET}\n")


def evaluate_strength(password: str) -> int:
    score = 0
    if len(password) >= 12: score += 1
    if len(password) >= 20: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in SYMBOLS for c in password): score += 1
    return min(score, 5)


def generate_password(length: int, use_upper: bool, use_lower: bool,
                      use_numbers: bool, use_symbols: bool) -> str:
    pool = ""
    guaranteed = []

    if use_upper:
        pool += UPPER
        guaranteed.append(random.choice(UPPER))
    if use_lower:
        pool += LOWER
        guaranteed.append(random.choice(LOWER))
    if use_numbers:
        pool += NUMBERS
        guaranteed.append(random.choice(NUMBERS))
    if use_symbols:
        pool += SYMBOLS
        guaranteed.append(random.choice(SYMBOLS))

    if not pool:
        print(f"\n{BOLD}\033[91mError:{RESET} Debes activar al menos un tipo de carácter.\n")
        sys.exit(1)

    remaining = [random.choice(pool) for _ in range(length - len(guaranteed))]
    password_chars = guaranteed + remaining

    # Fisher-Yates shuffle
    random.shuffle(password_chars)

    return "".join(password_chars)


def print_result(password: str):
    strength_idx = evaluate_strength(password)
    color  = STRENGTH_COLORS[strength_idx]
    label  = STRENGTH_LABELS[strength_idx]
    bar    = "█" * (strength_idx + 1) + "░" * (5 - strength_idx)

    print(f"  {BOLD}Contraseña:{RESET}  {ACCENT}{BOLD}{password}{RESET}")
    print(f"  {BOLD}Longitud:{RESET}    {len(password)} caracteres")
    print(f"  {BOLD}Fortaleza:{RESET}   {color}{bar} {label}{RESET}\n")


def interactive_mode():
    banner()
    print(f"  {DIM}Modo interactivo — presiona Enter para usar el valor por defecto{RESET}\n")

    try:
        length_input = input("  Longitud (8-64) [16]: ").strip()
        length = int(length_input) if length_input else 16
        length = max(8, min(64, length))

        upper   = input("  ¿Incluir mayúsculas? (s/n) [s]: ").strip().lower() != "n"
        lower   = input("  ¿Incluir minúsculas? (s/n) [s]: ").strip().lower() != "n"
        numbers = input("  ¿Incluir números?    (s/n) [s]: ").strip().lower() != "n"
        symbols = input("  ¿Incluir símbolos?   (s/n) [n]: ").strip().lower() == "s"

    except (KeyboardInterrupt, EOFError):
        print(f"\n\n  {DIM}Cancelado.{RESET}\n")
        sys.exit(0)

    print()
    password = generate_password(length, upper, lower, numbers, symbols)
    print_result(password)


def flags_mode(args):
    banner()
    password = generate_password(
        length      = args.length,
        use_upper   = not args.no_upper,
        use_lower   = not args.no_lower,
        use_numbers = not args.no_numbers,
        use_symbols = args.symbols
    )
    print_result(password)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="generator.py",
        description="Generador de contraseñas seguras · REKOL08 (github.com/REKOL08)",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Ejemplos:\n"
               "  python generator.py                        # modo interactivo\n"
               "  python generator.py --length 24            # longitud 24, defaults\n"
               "  python generator.py --length 32 --symbols  # con símbolos\n"
               "  python generator.py --no-numbers --symbols # sin números, con símbolos\n"
    )
    parser.add_argument(
        "--length", "-l",
        type=int, default=None,
        metavar="N",
        help="Longitud de la contraseña (8-64). Default: 16"
    )
    parser.add_argument(
        "--no-upper",
        action="store_true",
        help="Excluir mayúsculas (A-Z)"
    )
    parser.add_argument(
        "--no-lower",
        action="store_true",
        help="Excluir minúsculas (a-z)"
    )
    parser.add_argument(
        "--no-numbers",
        action="store_true",
        help="Excluir números (0-9)"
    )
    parser.add_argument(
        "--symbols", "-s",
        action="store_true",
        help="Incluir símbolos (!@#$...). Default: desactivado"
    )
    parser.add_argument(
        "--version", "-v",
        action="version",
        version=f"password-generator 1.0.0 · REKOL08 (github.com/REKOL08)"
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    # si no se pasó ningún flag relevante → modo interactivo
    flags_used = any([
        args.length is not None,
        args.no_upper,
        args.no_lower,
        args.no_numbers,
        args.symbols
    ])

    if flags_used:
        if args.length is not None:
            args.length = max(8, min(64, args.length))
        else:
            args.length = 16
        flags_mode(args)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
