#!/usr/bin/env python3

from __future__ import annotations

import argparse
from pathlib import Path


def order_tarballs(tarballs: list[str], version: str) -> list[str]:
    primary_tarball = f"dist/npm/codex-npm-{version}.tgz"
    ordered = [tarball for tarball in tarballs if tarball != primary_tarball]
    if primary_tarball in tarballs:
        ordered.append(primary_tarball)
    return ordered


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Order npm release tarballs with the main codex package last."
    )
    parser.add_argument("--version", required=True)
    parser.add_argument("tarballs", nargs="+")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    for tarball in order_tarballs(args.tarballs, args.version):
        print(tarball)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
