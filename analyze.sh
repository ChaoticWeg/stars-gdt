#!/usr/bin/env bash
thisdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export TZ='America/Chicago'
parse_date() { date -d "$(cat "${thisdir}/logs/next_game_date.log")" +"%A, %B %Y at %H:%M %Z"; };

python "${thisdir}/analyze.py" > "${thisdir}/logs/analyze.log"
bash "${thisdir}/test-deps/discord.sh" \
    --username "Stars GDT Analyzer" \
    --avatar-url "https://raw.githubusercontent.com/ChaoticWeg/stars-gdt/master/assets/avatars/analyze.png" \
    --title "Next Game Time" \
    --color "0x006847" \
    --timestamp \
    --description "The Stars' next game is $(parse_date)" \
    --text "$(cat "${thisdir}/logs/analyze.log")"

