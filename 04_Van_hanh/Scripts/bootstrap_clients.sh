#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"
# Run on a developer/CI machine with Flutter 3.32.8 installed.
# Generate platform host files from that pinned SDK, retaining authored lib/test files.
flutter create --no-pub --platforms=android,web --project-name adaptive_learner 01_San_pham/apps/learner
flutter create --no-pub --platforms=web --project-name adaptive_staff 01_San_pham/apps/staff
