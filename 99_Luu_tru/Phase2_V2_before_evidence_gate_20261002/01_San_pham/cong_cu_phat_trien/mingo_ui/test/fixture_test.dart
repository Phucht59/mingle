import 'dart:math';
import 'package:flutter_test/flutter_test.dart';
import 'package:mingo_ui/mingo_ui.dart';

void main() {
  test(
    'sample audio request budget is bounded and does not imply listening',
    () async {
      var calls = 0;
      final a = SampleAudio(
        budget: 2,
        requestPlayback: () async {
          calls++;
        },
      );
      await a.play();
      await a.play();
      await a.play();
      expect(calls, 2);
      expect(a.requests, 2);
      expect(a.limited, isTrue);
      a.dispose();
    },
  );
  test(
    'failed sample audio remains an error, never a successful assessment',
    () async {
      final a = SampleAudio(
        requestPlayback: () async {
          throw StateError('media missing');
        },
      );
      await a.play();
      expect(a.failed, isTrue);
      expect(a.busy, isFalse);
      a.dispose();
    },
  );
  test(
    'grammar and listening sample answer keys match task-specific explanation',
    () {
      expect(LessonContent.answers(LessonDomain.grammar, 'L-025').first, 'are');
      expect(
        LessonContent.explanation(LessonDomain.grammar, 'L-025'),
        contains('they'),
      );
      expect(
        LessonContent.answers(LessonDomain.listening, 'L-027').first,
        'Hello!',
      );
      expect(
        LessonContent.question(LessonDomain.vocabulary, 'L-024'),
        isNot(LessonContent.question(LessonDomain.vocabulary, 'L-025')),
      );
    },
  );
  test(
    'all catalogue routes resolve, including exact query and dynamic fixtures',
    () {
      for (final s in screens) {
        expect(screenByRoute(s.route)?.id, s.id);
      }
      expect(screenByRoute('/staff/learners/sample/evidence')?.id, 'S-022');
      expect(screenByRoute('/home?offline=1')?.id, 'L-011');
      expect(screenByRoute('/unmapped'), isNull);
    },
  );
  test('first wrong answer survives a correct bounded practice retry', () {
    final p = PracticeFixture();
    p.choose(1);
    expect(p.submit(), isTrue);
    expect(p.firstResponse, 1);
    expect(p.retry(), isTrue);
    p.choose(0);
    p.submit();
    expect(p.correct, isTrue);
    expect(p.firstResponse, 1);
    expect(p.assisted, isTrue);
    expect(p.retry(), isFalse);
  });
  test('hint marks practice as assisted', () {
    final p = PracticeFixture();
    expect(p.hint(), isTrue);
    p.choose(0);
    p.submit();
    expect(p.assisted, isTrue);
  });
  test('Check has neither hints nor retries nor skip', () {
    final p = PracticeFixture(check: true);
    expect(p.hint(), isFalse);
    expect(p.skip(), isFalse);
    p.choose(1);
    p.submit();
    expect(p.retry(), isFalse);
    expect(p.firstResponse, 1);
  });
  test('missing selection and duplicate submission add no response', () {
    final p = PracticeFixture();
    expect(p.submit(), isFalse);
    expect(p.firstResponse, isNull);
    p.choose(0);
    expect(p.submit(), isTrue);
    expect(p.submit(), isFalse);
  });
  test('skip is not a response or completion', () {
    final p = PracticeFixture();
    p.skip();
    expect(p.firstResponse, isNull);
    expect(p.submit(), isFalse);
    expect(p.submitted, isFalse);
  });
  test('published fixture cannot be changed through editable draft', () {
    final f = ContentFixture();
    f.draftTitle = 'Changed draft';
    expect(ContentFixture.publishedTitle, 'Chào hỏi và làm quen');
    expect(f.previewAllowed, isFalse);
    f.licenseVerified = true;
    expect(f.previewAllowed, isFalse);
    f.reviewed = true;
    expect(f.previewAllowed, isTrue);
    f.newDraft();
    expect(f.previewAllowed, isFalse);
  });
  test('fallback remains explainable when recommendation is disabled', () {
    expect(
      nextLessonReason(recommendationEnabled: false, due: false),
      'Bài tiếp theo trong lộ trình của bạn.',
    );
    expect(
      nextLessonReason(recommendationEnabled: false, hasResume: true),
      contains('học dở'),
    );
  });
  test('token foregrounds meet normal text contrast', () {
    double ratio(int foreground, int background) {
      double lum(int c) {
        final values = [(c >> 16) & 255, (c >> 8) & 255, c & 255].map((v) {
          final s = v / 255;
          return s <= .04045 ? s / 12.92 : powValue((s + .055) / 1.055);
        }).toList();
        return values[0] * .2126 + values[1] * .7152 + values[2] * .0722;
      }

      final a = lum(foreground), b = lum(background);
      return (a > b ? a + .05 : b + .05) / (a > b ? b + .05 : a + .05);
    }

    for (final color in [
      MingoColors.ink,
      MingoColors.muted,
      MingoColors.blue,
      MingoColors.error,
      MingoColors.success,
      MingoColors.orange,
    ]) {
      expect(ratio(color.toARGB32(), 0xFFFFFFFF), greaterThanOrEqualTo(4.5));
    }
    expect(
      ratio(0xFFFFFFFF, MingoColors.blue.toARGB32()),
      greaterThanOrEqualTo(4.5),
    );
  });
}

double powValue(double value) => pow(value, 2.4).toDouble();
