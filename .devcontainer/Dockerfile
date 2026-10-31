FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Keep in sync with HUGO_VERSION in .github/workflows/hugo.yaml
ARG HUGO_VERSION=0.115.4
RUN curl -fsSL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz" \
    | tar -xz -C /usr/local/bin hugo \
    && hugo version

# Python dependencies for the deck scripts (import_decks.py, build_card_db.py, check_decks.py)
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --quiet --root-user-action=ignore --disable-pip-version-check -r /tmp/requirements.txt
