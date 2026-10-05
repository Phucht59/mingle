# Motion V2

Navigation currently uses an immediate cut: no added waiting or novelty movement. Standard Flutter focus/pressed/dialog feedback remains; decorative assets are static. No looping mascot, reward/confetti or spring bounce. Future optional fades must be <=160ms, cancellable and never the only status cue; this future parameter is a specification, not a claim of an implemented custom transition.

Learner setting “Giảm chuyển động” combines with MediaQuery.disableAnimations; OS preference wins. Text scaling remains inherited independently. Status is expressed with live-region text and icon, not motion. Test checks that reduced-motion reaches the descendant MediaQuery at scale2. Real OS reduced-motion response and assistive-technology speech require manual verification.

[Apple Motion](https://developer.apple.com/design/human-interface-guidelines/motion?changes=l_9_3) supports purposeful brief optional motion. Mingo chooses a restrained subset appropriate to frequent learning tasks; no claim of Apple certification.
