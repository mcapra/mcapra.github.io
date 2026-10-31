#!/usr/bin/env bash
# Run a command in the dev container image (.devcontainer/Dockerfile) with Podman or Docker.
#
#   ./dev.sh                          Hugo dev server with drafts on http://localhost:1313
#   ./dev.sh python build_card_db.py  any other command
#
# Works from a Flatpak editor's terminal (e.g. VSCodium) by re-running itself on the
# host, and runs commands directly when already inside the devcontainer or Codespaces.
set -euo pipefail
cd "$(dirname "$0")"

# Flatpak sandbox: podman lives on the host
if [ -f /.flatpak-info ]; then
  exec flatpak-spawn --host "$PWD/dev.sh" "$@"
fi

in_container=false
if [ -f /.dockerenv ] || [ -f /run/.containerenv ]; then
  in_container=true
fi

if [ $# -eq 0 ]; then
  # --noHTTPCache: the theme's main.min.css keeps one URL, and iOS Safari would
  # otherwise keep using its cached copy after edits
  set -- hugo server -D --bind 0.0.0.0 --noHTTPCache
  if [ -n "${CODESPACE_NAME:-}" ]; then
    # Codespaces serves the site from a forwarded URL rather than localhost
    set -- "$@" --baseURL "https://$CODESPACE_NAME-1313.$GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN/" --appendPort=false
  elif ! $in_container; then
    # hugo server writes localhost into every link; use the LAN address so other
    # devices can follow them. Set HUGO_HOST to override the detected address.
    host=${HUGO_HOST:-$(ip -4 route get 1.1.1.1 2>/dev/null | sed -n 's/.* src \([0-9.]*\).*/\1/p')}
    if [ -n "$host" ]; then
      set -- "$@" --baseURL "http://$host:1313/"
      echo "Serving on http://$host:1313/" >&2
    fi
  fi
fi

# Already in a container: run directly
if $in_container; then
  exec "$@"
fi

engine=$(command -v podman || command -v docker || true)
if [ -z "$engine" ]; then
  echo "dev.sh: needs podman or docker" >&2
  exit 1
fi

if [ ! -f themes/paper/theme.toml ]; then
  git submodule update --init themes/paper
fi

echo "Building dev image (the first run downloads about 1 GB) ..." >&2
"$engine" build -q -t mcapra-dev -f .devcontainer/Dockerfile . >/dev/null

args=(--rm -i --init --security-opt label=disable -v "$PWD":/workspaces/site -w /workspaces/site)
[ -t 0 ] && args+=(-t)
[ "${1:-}" = hugo ] && [ "${2:-}" = server ] && args+=(-p 1313:1313)

exec "$engine" run "${args[@]}" mcapra-dev "$@"
