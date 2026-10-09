# Finance Sync

Retired bank-scraper implementation retained for reference. Active account
collection and transaction review use the
[finance-review skill](https://github.com/alexjmiller5/agent-config/tree/main/skills/finance-review)
and Soma.

## Current workflow

Start a finance-review conversation and select the accounts to collect.
The workflow reads authenticated source records, preserves their evidence,
reconciles account coverage, then reviews categories, shares and rewards
with the account owner. Soma owns the financial records; Networth
consumes them for display.

Collection is ad hoc. Source access, uncertain classifications and shared
expenses require the owner's participation. A balance or rewards snapshot
is evidence for its observation date, not a substitute for transaction
history or a complete rewards ledger.

## Repository scope

This repository contains the retired Notion writer, scrapers, tests, Nix
module and deployment material. They are retained as implementation
reference, not the active service or installation path. The commands and
setup instructions in `docs/`, `deploy/` and the old module describe that
retired pipeline; do not use them to provision a new installation, restart
a schedule or migrate a live financial database.

The active skill owns source playbooks and collection/review tooling.
Soma owns schema validation, provenance, history and synchronization.
Application configuration and personal financial data stay outside this
repository.
