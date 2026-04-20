# fix: publish @openai/codex after platform npm packages

Issue: https://github.com/openai/codex/issues/17432

Invited follow-up for: https://github.com/openai/codex/issues/17432#issuecomment-4283804701

## What?

This changes the npm release workflow so the main `@openai/codex` tarball is published after the other tarballs for the same version.

Before this change, the `publish-npm` step in `.github/workflows/rust-release.yml` iterated over `dist/npm/*-"${VERSION}".tgz` in shell glob order. That causes `codex-npm-${VERSION}.tgz` to be published before the platform tarballs because it sorts first lexicographically.

After this change, tarballs are still discovered dynamically, but the publish order is adjusted so `codex-npm-${VERSION}.tgz` is emitted last when it is present.

## Why?

The linked issue discussion suggested that npm publish order may be part of the release problem. If the main `@openai/codex` package is published before the matching platform packages exist on npm, clients may briefly resolve a package state that references artifacts that are not yet available.

This PR narrows that window by publishing the platform-specific tarballs first and the main package last, without replacing the workflow with a hardcoded tarball list.

## How?

- Added `.github/scripts/order_npm_release_tarballs.py` to encapsulate the tarball ordering rule.
- Updated `.github/workflows/rust-release.yml` to call that helper before the publish loop.
- Added `.github/scripts/test_order_npm_release_tarballs.py`.
- The test coverage verifies that `codex-npm-${VERSION}.tgz` moves to the end when present.
- The test coverage verifies that the original order is preserved when the main tarball is absent.

## Validation

Ran locally:

- `python3 .github/scripts/test_order_npm_release_tarballs.py`
- `python3 -m py_compile .github/scripts/order_npm_release_tarballs.py .github/scripts/test_order_npm_release_tarballs.py`

## Documentation

This change is workflow-only and does not affect README text, CLI help, or user-facing examples.

## CLA

I have read the CLA Document and I hereby sign the CLA
