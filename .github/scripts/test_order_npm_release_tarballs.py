#!/usr/bin/env python3

from __future__ import annotations

import unittest

import order_npm_release_tarballs


class OrderNpmReleaseTarballsTest(unittest.TestCase):
    def test_moves_primary_codex_tarball_to_end(self) -> None:
        tarballs = [
            "dist/npm/codex-npm-1.2.3.tgz",
            "dist/npm/codex-npm-darwin-arm64-1.2.3.tgz",
            "dist/npm/codex-npm-linux-x64-1.2.3.tgz",
            "dist/npm/codex-sdk-npm-1.2.3.tgz",
        ]

        ordered = order_npm_release_tarballs.order_tarballs(tarballs, "1.2.3")

        self.assertEqual(
            [
                "dist/npm/codex-npm-darwin-arm64-1.2.3.tgz",
                "dist/npm/codex-npm-linux-x64-1.2.3.tgz",
                "dist/npm/codex-sdk-npm-1.2.3.tgz",
                "dist/npm/codex-npm-1.2.3.tgz",
            ],
            ordered,
        )

    def test_leaves_order_unchanged_when_primary_tarball_is_missing(self) -> None:
        tarballs = [
            "dist/npm/codex-npm-darwin-arm64-1.2.3.tgz",
            "dist/npm/codex-npm-linux-x64-1.2.3.tgz",
            "dist/npm/codex-sdk-npm-1.2.3.tgz",
        ]

        ordered = order_npm_release_tarballs.order_tarballs(tarballs, "1.2.3")

        self.assertEqual(tarballs, ordered)


if __name__ == "__main__":
    unittest.main()
