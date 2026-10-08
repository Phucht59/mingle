# M3.X Git publication — 2026-10-08

The proof slice was built and audited while uncommitted on 2026-10-07. The original run reports and source ZIP preserve that capture state. This later publication adds the complete learner code, tests, generated iOS host source, scoped governance and reviewable host evidence to the dedicated Git branch. The branch was fast-forwarded to the current `origin/main` before committing; that main update contained only five GitHub template files.

The Git repository is public. The two owner-supplied intake ZIPs, their extracted originals, the full BA paragraph extract and the source-build ZIP remain in the local handoff directory. Their SHA records and the resulting proof conclusions are retained. These original input bytes are not necessary to build the learner and are not part of this public Git commit.

To build from a clone of this branch on a Mac, use `01_San_pham/apps/learner/` directly; its `ios/` source host is included. Run `flutter pub get`, set a development team and a unique bundle ID in `ios/Runner.xcworkspace`, then follow `M3X_IPHONE_RUNBOOK.md` starting with environment capture and simulator build. The runbook's `cp -R generated-ios/ios ...` step is only for the standalone source ZIP, whose directory layout differs from this Git branch.

The iOS host is an unbuilt Flutter 3.32.8 template. Generated registrants/config, signing secrets, IPA, simulator/physical-device results and production infrastructure are absent. Propagation remains HOLD until the physical protocol is executed. No historical BA seal or M3 gate is altered by publishing code.
