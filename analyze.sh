#!/usr/bin/env bash
thisdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python "${thisdir}/analyze.py" > "${thisdir}/logs/analyze.log"
bash "${thisdir}/test-deps/discord.sh" --username "Stars GDT Analyzer" --text "$(cat "${thisdir}/logs/analyze.log")"

