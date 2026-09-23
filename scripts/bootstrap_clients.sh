#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
# Run on a developer/CI machine with Flutter 3.32.8 installed.
# Generate platform host files from that pinned SDK, retaining authored lib/test files.
flutter create --no-pub --platforms=android,web --project-name adaptive_learner apps/learner
flutter create --no-pub --platforms=web --project-name adaptive_staff apps/staff
