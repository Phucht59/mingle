# Repository preservation

Baseline git status and dirty files were captured before tests/candidate edits. Final comparison: 2803 existing files hashed, 0 changed, 0 missing; 116 Excel paths hashed again, 0 changed. HEAD remains a112f762ab08f6fa688cc4857b21d95d1055ab5c. No unexpected git status changes outside dedicated audit directories: True.

Canonical workbook/source/code/tests/V3.2/migrations/schema/package-lock/pubspec-lock and prior completed reports are untouched. No commit/push or destructive Git operation. Full before/after statuses and hashes are stored in evidence. Flutter may refresh ignored build/.dart_tool test caches in its existing package. No cache cleanup attempted. Dependency resolution suppressed with --no-pub; pubspec/package-lock/source bytes compared. V3 npm artifacts only in new isolated audit work copy. Temporary test resources have normal test lifecycle; no user file deletion/restoration.

| Status difference | Count | Boundary |
| --- | --- | --- |
| Added entries | 188 | New dedicated report/evidence only |
| Removed entries | 0 | No pre-existing status removed |
| Changed protected bytes | 0 | [] |
| Missing protected files | 0 | [] |
| Excel hash changes | 0 | [] |
