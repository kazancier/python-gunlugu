"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true", help ="Prova modu")

args = parser.parse_args()

if args.dry_run:
    print("prova_modu")
else:
    print("gerçek mod")
    """

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("klasor")

args = parser.parse_args()

print(args.klasor)
