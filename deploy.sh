#!/bin/sh
set -eu

deploy_dir="${1:?Usage: deploy.sh DEPLOY_DIRECTORY}"
mkdir -p "$deploy_dir"
cp app.py "$deploy_dir/app.py"
python3 "$deploy_dir/app.py" > "$deploy_dir/output.txt"
cat "$deploy_dir/output.txt"
test "$(cat "$deploy_dir/output.txt")" = 'Hello, World from Tamer Lammam!'
echo "Application deployed to $deploy_dir"
