# look-talks: every task is a recipe here. `just` lists them.

# Each word after a recipe's name reaches its commands whole, as "$1", "$2" and so on
set positional-arguments

# Python comes from uv, so the machine needs just and uv only
python := "uv run --no-project --quiet python"
smalldocs := "uvx --from smalldocs==0.5.5 smalldocs"

# The checker for prose, check.py of nossaifd, at a fixed commit of its main branch. Move it when
# check.py changes there.
nossaifd_commit := "ec80717f074c68dfa5fecb0c8c19ba49398a2f76"
# htmpres for just example, at a fixed commit of its main branch: PR 28, which fixed the picture slides.
htmpres_commit := "120a105cb579118097d46f4e291db4d517f3dc15"

[private]
default:
    @just --list --unsorted

# Copy the guide, the example deck and the checker into the skill, which ships copies of them
sync:
    mkdir -p .agents/skills/look-talks/references .agents/skills/look-talks/scripts
    cp LOOK.md .agents/skills/look-talks/references/LOOK.md
    cp examples/cache/slides.qmd .agents/skills/look-talks/references/example-slides.qmd
    cp check_look.py .agents/skills/look-talks/scripts/check_look.py

# Check the Python and the JSON for syntax
lint:
    {{python}} -I -m py_compile check_look.py scripts/books_check.py tests/*.py
    {{python}} -I -m json.tool skill-package.json > /dev/null

# Check the example deck with the look checker
look:
    {{python}} -I check_look.py -v examples/cache/slides.qmd

# Lint, render and verify the example deck with htmpres from GitHub, at the pinned commit unless you name one,
# in a temporary folder: just example, or just example main. It writes to no htmpres checkout.
example ref=htmpres_commit:
    #!/usr/bin/env bash
    set -euo pipefail
    work="$(mktemp -d)"
    trap 'rm -rf -- "$work"' EXIT
    cp -R examples/cache/. "$work/"
    rm -rf -- "$work/_extensions"
    mkdir -p "$work/htmpres"
    curl -fsSL "https://codeload.github.com/rahuldave/htmpres/tar.gz/$1" | tar -xz -C "$work/htmpres" --strip-components=1
    mv "$work/htmpres/_extensions" "$work/_extensions"
    rm -rf -- "$work/htmpres"
    cd "$work"
    quarto run _extensions/htmpres/htmpres.ts lint slides.qmd --json
    quarto run _extensions/htmpres/htmpres.ts render slides.qmd
    quarto run _extensions/htmpres/htmpres.ts verify slides.qmd

# Build the site into _site with smalldocs
site:
    {{smalldocs}} render .

# Check the site with smalldocs: the options, the links and the Markdown
site-check:
    {{smalldocs}} check .

# Check skill-package.json with skill-package-maker at a fixed commit
package-lint:
    #!/usr/bin/env bash
    set -euo pipefail
    tool_root="$(mktemp -d)"
    trap 'rm -rf -- "$tool_root"' EXIT
    git clone --quiet https://github.com/rahuldave/agent_skill_package_maker.git "$tool_root/package-maker"
    git -C "$tool_root/package-maker" checkout --quiet 6a5938c49ca71c374dc1a234a4d15134c484a741
    {{python}} "$tool_root/package-maker/skills/skill-package-maker/scripts/lint_skill_bundle.py" .

# Check the Markdown pages with check.py of nossaifd
prose:
    #!/usr/bin/env bash
    set -euo pipefail
    tool_root="$(mktemp -d)"
    trap 'rm -rf -- "$tool_root"' EXIT
    curl -fsSL "https://raw.githubusercontent.com/rahuldave/nossaifd/{{nossaifd_commit}}/check.py" -o "$tool_root/check.py"
    git ls-files -z '*.md' | xargs -0 {{python}} -I "$tool_root/check.py"

# Check that no book is in Git, because the books are under copyright. Add --history to check every name in the history
books-check *args:
    {{python}} -I scripts/books_check.py "$@"

# Run the tests. Extra arguments go to unittest
test *args:
    {{python}} -I -m unittest discover -s tests -q "$@"

# Install a pre-commit hook in this clone, which runs the books check before each commit
hooks:
    #!/usr/bin/env bash
    set -euo pipefail
    hook="$(git rev-parse --git-path hooks)/pre-commit"
    marker="# look-talks books check"
    if [ -e "$hook" ] && ! grep -qF "$marker" "$hook"; then
        echo "$hook exists and is not ours. Add 'just books-check' to it by hand." >&2
        exit 1
    fi
    printf '#!/bin/sh\n%s\nif ! command -v just >/dev/null 2>&1; then\n  echo "The books check needs just on the PATH." >&2\n  exit 1\nfi\nexec just books-check\n' "$marker" > "$hook"
    chmod +x "$hook"
    echo "Installed $hook"

# Everything a commit must pass
check:
    just books-check --history
    just lint
    just test
    just look
    just prose
    just site-check
