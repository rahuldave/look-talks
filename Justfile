# look-talks: every task is a recipe here. `just` lists them.

# Each word after a recipe's name reaches its commands whole, as "$1", "$2" and so on
set positional-arguments

# Python comes from uv, so the machine needs just and uv only
python := "uv run --no-project --quiet python"
smalldocs := "uvx --from smalldocs==0.5.5 smalldocs"

# The skills nossaifd and declaude, from github.com/rahuldave/nossaifd, and presentations, from
# github.com/rahuldave/nossaifd-talks, live in .agents/skills/ for the prose flow of nossaifd. The declaude skill
# is by Oskar Austegard (github.com/oaustegard/claude-skills, MIT licence). The package ships only look-talks.
# The map .agents/nossaifd-checkers.json gives the talks to check_talk.py of presentations, and other pages to check.py.
check_py := ".agents/skills/nossaifd/scripts/check.py"
gate_py := ".agents/skills/nossaifd/scripts/prose_gate.py"
# htmpres for just example, at a fixed commit of its main branch: PR 30, which fails a picture with no
# description and fits a picture under a title in the rest of the slide.
htmpres_commit := "0787d97961c938aece8e6d58639ec1ed3ea79f87"

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

# Check each page with the checker that .agents/nossaifd-checkers.json gives it: talks get check_talk.py, others check.py.
# The gate skips .agents/ and AGENTS.md, so the SKILL.md of look-talks and AGENTS.md get check.py by name
prose:
    #!/usr/bin/env bash
    set -euo pipefail
    git ls-files -z '*.md' '*.qmd' | {{python}} -I {{gate_py}} pages -z | xargs -0 -r {{python}} -I {{gate_py}} check
    {{python}} -I {{check_py}} .agents/skills/look-talks/SKILL.md AGENTS.md

# Install the skills nossaifd and declaude from nossaifd, and presentations from nossaifd-talks, for the prose flow
nossaifd-install:
    npx -y skills add rahuldave/nossaifd -a codex --skill '*' -y
    npx -y skills add rahuldave/nossaifd-talks -a codex --skill presentations -y

# Check pages with the checker that .agents/nossaifd-checkers.json gives each one. A path is from the current folder
[no-cd]
prose-check +pages:
    {{python}} -I "{{justfile_directory()}}/{{gate_py}}" check -v "$@"

# List the changed pages that still need the steps of the nossaifd skill
prose-status:
    {{python}} -I .agents/skills/nossaifd/scripts/prose_gate.py status

# Record each page after step 8 of the nossaifd skill: just prose-record page.md. A path is from the current folder
[no-cd]
prose-record +pages:
    {{python}} -I "{{justfile_directory()}}/.agents/skills/nossaifd/scripts/prose_gate.py" record "$@"

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
