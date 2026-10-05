import 'package:flutter/material.dart';
import 'catalog.dart';
import 'design.dart';
import 'fixtures.dart';
import 'lesson_content.dart';
import 'audio.dart';
import 'journey.dart';

class LessonPage extends StatefulWidget {
  const LessonPage({
    super.key,
    required this.id,
    required this.onNavigate,
    this.reviewState,
    this.practice,
    this.domain = LessonDomain.vocabulary,
    this.audio,
  });
  final String id;
  final void Function(String) onNavigate;
  final String? reviewState;
  final PracticeFixture? practice;
  final LessonDomain domain;
  final SampleAudio? audio;
  @override
  State<LessonPage> createState() => _LessonPageState();
}

class _LessonPageState extends State<LessonPage> {
  late final practice =
      widget.practice ??
      PracticeFixture(check: widget.id == 'L-027' || widget.id == 'L-005');
  bool validation = false;
  late final audio =
      widget.audio ?? SampleAudio(budget: practice.check ? 2 : null);
  @override
  void initState() {
    super.initState();
    final s = (widget.reviewState ?? '').toLowerCase();
    if (s.contains('selected')) practice.choose(0);
    if (s.contains('hint')) practice.hint();
    if (s.contains('result') || s.contains('retry')) {
      practice.choose(s.contains('retry') ? 1 : 0);
      practice.submit();
    }
    if (s.contains('retry-exhausted')) {
      practice.retry();
      practice.choose(1);
      practice.submit();
    }
    if (s.contains('skipped')) practice.skip();
    validation = s.contains('validation-error');
    if (s.contains('play-limit')) {
      audio.requests = 2;
    }
  }

  @override
  void dispose() {
    if (widget.practice == null) {
      practice.dispose();
    }
    if (widget.audio == null) {
      audio.dispose();
    }
    super.dispose();
  }

  void next() {
    const order = [
      'L-021',
      'L-022',
      'L-023',
      'L-024',
      'L-025',
      'L-026',
      'L-027',
      'L-032',
    ];
    final i = order.indexOf(widget.id);
    widget.onNavigate(
      widget.id == 'L-005'
          ? 'L-006'
          : i >= 0 && i < order.length - 1
          ? order[i + 1]
          : 'L-032',
    );
  }

  Widget primary(String title, VoidCallback action) => SizedBox(
    width: double.infinity,
    child: FilledButton(
      onPressed: action,
      child: Text(title, textAlign: TextAlign.center),
    ),
  );
  @override
  Widget build(BuildContext c) => ListenableBuilder(
    listenable: Listenable.merge([practice, audio]),
    builder: (c, _) {
      final id = widget.id, spec = screenById(id);
      final intro = ['L-021', 'L-023', 'L-026'].contains(id);
      final standalone = [
        'L-028',
        'L-029',
        'L-030',
        'L-031',
        'L-032',
      ].contains(id);
      final audioUnavailable =
          audio.failed ||
          (widget.reviewState ?? '').contains('audio-unavailable');
      final state = (widget.reviewState ?? '').toLowerCase();
      if (state == 'submitting' ||
          state == 'loading' ||
          state.contains('content-unavailable') ||
          state.contains('revision-invalid') ||
          state.contains('corrupt')) {
        return PageBody(
          children: [
            StateNotice(state: state),
            heading(c, spec.title),
            const Notice(
              title: 'Chưa thể tiếp tục câu này',
              detail:
                  'Nội dung cần hợp lệ và không có câu đang chờ xử lý. Chưa ghi nhận thêm câu trả lời hoặc kết quả.',
            ),
            primary('Quay về danh sách bài', () => widget.onNavigate('L-020')),
          ],
        );
      }
      return PageBody(
        children: [
          if (widget.reviewState != null)
            StateNotice(state: widget.reviewState!),
          if (!standalone)
            Semantics(
              label: 'Tiến độ bài mẫu',
              value: id == 'L-027' ? 'Bước 5 trên 5' : 'Bước trong bài học',
              child: LinearProgressIndicator(
                value: id == 'L-027'
                    ? 1.0
                    : id == 'L-021'
                    ? 0.1
                    : 0.5,
                minHeight: 4,
                borderRadius: BorderRadius.circular(4),
              ),
            ),
          if (id != 'L-032')
            heading(
              c,
              id == 'L-021' ? LessonContent.title(widget.domain) : spec.title,
              intro
                  ? id == 'L-026'
                        ? 'Một câu mới, không dùng gợi ý hay thử thêm. Bạn vẫn có thể quay lại.'
                        : widget.domain == LessonDomain.grammar
                        ? 'Mục tiêu: giới thiệu người khác bằng một câu đơn giản.'
                        : 'Mục tiêu: nhận biết và đáp lại một lời chào.'
                  : standalone
                  ? null
                  : LessonContent.question(widget.domain, id),
            ),
          if (intro) ...[
            if (id == 'L-021') const Center(child: Mascot(height: 150)),
            Surface(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    id == 'L-026'
                        ? 'Đến lượt bạn tự thử'
                        : LessonContent.example(widget.domain),
                    style: Theme.of(c).textTheme.headlineMedium,
                  ),
                  const SizedBox(height: 12),
                  Text(
                    id == 'L-026'
                        ? 'Không gợi ý · Một câu trả lời đầu tiên được giữ riêng.'
                        : LessonContent.explanation(widget.domain, id),
                  ),
                  if (id == 'L-023') ...[
                    const SizedBox(height: 16),
                    const Text(
                      'Bạn có thể ôn lại trước khi tự thử. Lần luyện có hỗ trợ được giữ riêng.',
                    ),
                  ],
                ],
              ),
            ),
            if (widget.domain == LessonDomain.listening && id == 'L-023')
              audioControl(c, audioUnavailable),
            primary(id == 'L-026' ? 'Sẵn sàng, thử một câu' : 'Tiếp tục', next),
          ] else if (standalone) ...[
            if (id == 'L-032') ...[
              CompletionMoment(title: spec.title),
              Notice(
                title: widget.domain == LessonDomain.grammar
                    ? 'Bạn đã luyện câu giới thiệu'
                    : 'Bạn đã luyện lời chào',
                detail:
                    'Mẫu: một lần tự trả lời và một lần có hỗ trợ. Không suy ra điểm năng lực từ bài ngắn này.',
              ),
              const Surface(
                child: Text(
                  'Bước tiếp theo\nThử lời chào trong một tình huống khác. Câu bỏ qua và lần thử thêm được giữ riêng.',
                ),
              ),
              primary('Đến bước tiếp theo', () => widget.onNavigate('L-040')),
              TextButton(
                onPressed: () => widget.onNavigate('L-051'),
                child: const Text('Xem bằng chứng mẫu'),
              ),
            ] else ...[
              Notice(
                title: id == 'L-028'
                    ? 'Đúng với tình huống này'
                    : id == 'L-030'
                    ? 'Nhìn vào thời điểm trong ngày'
                    : id == 'L-031'
                    ? 'Bạn có thể quay lại'
                    : 'Lần thử thêm có giới hạn',
                detail: id == 'L-028'
                    ? LessonContent.explanation(widget.domain, id)
                    : id == 'L-030'
                    ? '${LessonContent.explanation(widget.domain, id)} Lần dùng gợi ý được ghi riêng.'
                    : id == 'L-031'
                    ? 'Bỏ qua không được tính là trả lời đúng hoặc hoàn thành.'
                    : 'Câu trả lời đầu tiên vẫn giữ nguyên; thêm tối đa một lần luyện.',
              ),
              primary('Tiếp tục luyện', () => widget.onNavigate('L-024')),
            ],
          ] else ...[
            Surface(
              tint: true,
              child: Text(
                widget.domain == LessonDomain.vocabulary
                    ? 'Hãy thử nhớ lời chào buổi sáng.'
                    : LessonContent.question(widget.domain, id),
                style: Theme.of(c).textTheme.titleLarge,
              ),
            ),
            if (widget.domain == LessonDomain.listening ||
                (widget.reviewState ?? '').contains('audio-') ||
                (widget.reviewState ?? '').contains('play-limit'))
              audioControl(c, audioUnavailable),
            for (final (index, answer) in LessonContent.answers(
              widget.domain,
              id,
            ).indexed)
              Semantics(
                selected: practice.selected == index,
                child: ActionRow(
                  title: answer,
                  detail: practice.selected == index ? 'Đang chọn' : '',
                  selected: practice.selected == index,
                  icon: practice.selected == index
                      ? Icons.radio_button_checked
                      : Icons.radio_button_unchecked,
                  onTap: () => practice.choose(index),
                ),
              ),
            if (validation)
              const Notice(
                title: 'Chọn một câu trả lời trước',
                detail: 'Bạn chưa chọn đáp án. Câu này chưa được ghi nhận.',
                error: true,
              ),
            if (practice.hinted)
              Notice(
                title: widget.domain == LessonDomain.vocabulary
                    ? 'Gợi ý: nghĩ đến buổi sáng'
                    : widget.domain == LessonDomain.grammar
                    ? 'Gợi ý: nhìn vào người được giới thiệu'
                    : 'Gợi ý: đây là một lời chào',
                detail: 'Lần này có hỗ trợ, không phải một lần tự trả lời.',
              ),
            if (practice.skipped)
              const Notice(
                title: 'Đã bỏ qua trong bản xem trước',
                detail: 'Không được tính là hoàn thành hay trả lời đúng.',
              ),
            if (practice.submitted) ...[
              Notice(
                title: practice.correct
                    ? widget.domain == LessonDomain.vocabulary
                          ? 'Phù hợp với buổi sáng!'
                          : 'Phù hợp với câu này!'
                    : widget.domain == LessonDomain.vocabulary
                    ? 'Nhìn lại thời điểm trong ngày'
                    : 'Cùng xem lại câu này',
                detail:
                    '${LessonContent.explanation(widget.domain, id)} ${practice.assisted ? 'Lần này có hỗ trợ.' : 'Câu trả lời đầu tiên được giữ riêng.'} Đây là phản hồi mẫu.',
              ),
              if (practice.canRetry)
                OutlinedButton(
                  onPressed: () => practice.retry(),
                  child: const Text('Thử thêm một lần'),
                ),
              primary('Tiếp tục', next),
            ] else if (practice.skipped)
              primary('Tiếp tục', next)
            else if (audioUnavailable && practice.check)
              primary('Quay về bài học', () => widget.onNavigate('L-020'))
            else
              primary('Kiểm tra câu trả lời', () {
                if (!practice.submit()) {
                  setState(() => validation = true);
                } else {
                  setState(() => validation = false);
                }
              }),
            if (!practice.check && !practice.submitted && !practice.skipped)
              Wrap(
                spacing: 12,
                children: [
                  TextButton(
                    onPressed: () => practice.hint(),
                    child: const Text('Xem gợi ý'),
                  ),
                  TextButton(
                    onPressed: () => practice.skip(),
                    child: const Text('Bỏ qua câu này'),
                  ),
                ],
              ),
            if (practice.check)
              const Text(
                'Câu tự thử: không dùng gợi ý hoặc thử thêm. Bản xem trước không ghi điểm máy chủ.',
              ),
          ],
        ],
      );
    },
  );
  Widget audioControl(BuildContext c, bool unavailable) => Surface(
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        if (unavailable)
          const Notice(
            title: 'Âm thanh chưa sẵn sàng',
            detail:
                'Câu nghe chưa thể được ghi nhận. Bạn có thể quay về hoặc thử lại khi tệp hợp lệ.',
            error: true,
          )
        else ...[
          OutlinedButton(
            onPressed: audio.busy || audio.limited ? null : audio.play,
            child: Text(
              audio.busy
                  ? 'Đang yêu cầu phát'
                  : audio.limited
                  ? 'Lượt nghe mẫu đã hết'
                  : 'Nghe mẫu',
            ),
          ),
          const SizedBox(height: 12),
          Text(
            practice.check
                ? 'Lượt nghe mẫu: ${audio.requests} / 2'
                : 'Bạn có thể nghe lại khi luyện.',
          ),
          const Text(
            'Âm thanh “Hello” · Dvortygirl · Public domain',
            style: TextStyle(fontSize: 14),
          ),
        ],
      ],
    ),
  );
}
