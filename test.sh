#!/usr/bin/env bash
thisdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python "${thisdir}/main.py" > "${thisdir}/logs/script-out.txt"

# escape quotes in output
json_outfile="${thisdir}/logs/test.json"
perl -i.bak -p -e 's/"/\\"/g; s/\n/\\n/' "${json_outfile}"

json_output="$(cat "${json_outfile}")"
bash "${thisdir}/test-deps/discord.sh" --text "\`\`\`json\n${json_output}\n\`\`\`"

