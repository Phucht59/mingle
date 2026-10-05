import 'package:flutter/material.dart';
import 'design.dart';

/// Static learner composition. Every activity/outcome remains a preview fixture.
class CompanionCard extends StatelessWidget {
  const CompanionCard({
    super.key,
    required this.title,
    required this.subtitle,
    required this.child,
  });
  final String title, subtitle;
  final Widget child;
  @override
  Widget build(BuildContext c) => Container(
    width: double.infinity,
    clipBehavior: Clip.antiAlias,
    decoration: BoxDecoration(
      color: Theme.of(c).colorScheme.surfaceContainerLowest,
      borderRadius: BorderRadius.circular(28),
      border: Border.all(color: Theme.of(c).colorScheme.outlineVariant),
    ),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(24, 24, 24, 20),
          child: heading(c, title, subtitle),
        ),
        const ScenicWindow(aspectRatio: 2.2),
        Padding(padding: const EdgeInsets.all(24), child: child),
      ],
    ),
  );
}

class ScenicWindow extends StatelessWidget {
  const ScenicWindow({super.key, this.aspectRatio = 2.6});
  final double aspectRatio;
  @override
  Widget build(BuildContext c) => ExcludeSemantics(
    child: AspectRatio(
      aspectRatio: aspectRatio,
      child: LayoutBuilder(
        builder: (c, bounds) => Image.asset(
          'assets/exploration.png',
          package: 'mingo_ui',
          fit: BoxFit.cover,
          alignment: const Alignment(.35, .25),
          cacheWidth:
              ((aspectRatio < 1.5 ? bounds.maxHeight * 1.5 : bounds.maxWidth) *
                      MediaQuery.devicePixelRatioOf(c))
                  .ceil()
            .clamp(16, 1536),
        ),
      ),
    ),
  );
}

class TopicCard extends StatelessWidget {
  const TopicCard({
    super.key,
    required this.title,
    required this.detail,
    required this.label,
    required this.icon,
    required this.onTap,
  });
  final String title, detail, label;
  final IconData icon;
  final VoidCallback onTap;
  @override
  Widget build(BuildContext c) {
    final compact = MediaQuery.textScalerOf(c).scale(1) > 1.3;
    final visual = ExcludeSemantics(
      child: Container(
        width: compact ? double.infinity : 82,
        height: compact ? 96 : 104,
        decoration: BoxDecoration(
          color: Theme.of(
            c,
          ).colorScheme.primaryContainer.withValues(alpha: .25),
          borderRadius: BorderRadius.circular(16),
        ),
        child: Stack(
          alignment: Alignment.center,
          children: [
            const Mascot(height: 90),
            Positioned(
              bottom: 8,
              right: 8,
              child: DecoratedBox(
                decoration: BoxDecoration(
                  color: Theme.of(c).colorScheme.surfaceContainerLowest,
                  shape: BoxShape.circle,
                ),
                child: Padding(
                  padding: const EdgeInsets.all(6),
                  child: Icon(
                    icon,
                    size: 18,
                    color: Theme.of(c).colorScheme.primary,
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
    final words = Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: Theme.of(
            c,
          ).textTheme.labelLarge?.copyWith(fontWeight: FontWeight.w600),
        ),
        const SizedBox(height: 6),
        Text(
          title,
          style: Theme.of(
            c,
          ).textTheme.titleMedium?.copyWith(fontWeight: FontWeight.w700),
        ),
        const SizedBox(height: 6),
        Text(detail, style: Theme.of(c).textTheme.bodyMedium),
      ],
    );
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: OutlinedButton(
        onPressed: onTap,
        style: OutlinedButton.styleFrom(
          padding: const EdgeInsets.all(16),
          backgroundColor: Theme.of(c).colorScheme.surfaceContainerLowest,
          side: BorderSide(color: Theme.of(c).colorScheme.outlineVariant),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(24),
          ),
        ),
        child: compact
            ? Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [visual, const SizedBox(height: 16), words],
              )
            : Row(
                children: [
                  visual,
                  const SizedBox(width: 16),
                  Expanded(child: words),
                  const SizedBox(width: 8),
                  const Icon(Icons.arrow_forward_rounded, size: 20),
                ],
              ),
      ),
    );
  }
}

class JourneyMilestone extends StatelessWidget {
  const JourneyMilestone({
    super.key,
    required this.title,
    required this.detail,
    required this.icon,
    required this.onTap,
    this.current = false,
  });
  final String title, detail;
  final IconData icon;
  final VoidCallback onTap;
  final bool current;
  @override
  Widget build(BuildContext c) {
    final large = MediaQuery.textScalerOf(c).scale(1) > 1.3;
    final island = ExcludeSemantics(
      child: SizedBox(
        width: 80,
        height: 96,
        child: Stack(
          alignment: Alignment.center,
          children: [
            ClipOval(
              child: SizedBox(
                width: 80,
                height: 80,
                child: const ScenicWindow(aspectRatio: 1),
              ),
            ),
            Positioned(
              bottom: 0,
              child: Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: Theme.of(c).colorScheme.surfaceContainerLowest,
                ),
                child: Icon(
                  icon,
                  size: 24,
                  color: Theme.of(c).colorScheme.primary,
                ),
              ),
            ),
          ],
        ),
      ),
    );
    final words = Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: Theme.of(c).textTheme.titleLarge),
        const SizedBox(height: 8),
        Text(detail, style: Theme.of(c).textTheme.bodyMedium),
        if (current) ...[
          const SizedBox(height: 8),
          const Text(
            'Bước hiện tại',
            style: TextStyle(fontSize: 14, fontWeight: FontWeight.w600),
          ),
        ],
      ],
    );
    return OutlinedButton(
      onPressed: onTap,
      style: OutlinedButton.styleFrom(
        padding: const EdgeInsets.all(20),
        backgroundColor: current
            ? Theme.of(c).colorScheme.primaryContainer.withValues(alpha: .3)
            : Colors.transparent,
        side: current
            ? BorderSide(color: Theme.of(c).colorScheme.primary)
            : BorderSide.none,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(28)),
      ),
      child: large
          ? Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [island, const SizedBox(height: 12), words],
            )
          : Row(
              children: [
                island,
                const SizedBox(width: 16),
                Expanded(child: words),
              ],
            ),
    );
  }
}

/// Decorative trail, excluded from semantic order; labels carry all real status.
class TrailConnector extends StatelessWidget {
  const TrailConnector({super.key, this.reverse = false});
  final bool reverse;
  @override
  Widget build(BuildContext c) => ExcludeSemantics(
    child: SizedBox(
      height: 40,
      width: double.infinity,
      child: CustomPaint(
        painter: _TrailPainter(Theme.of(c).colorScheme.outlineVariant, reverse),
      ),
    ),
  );
}

class _TrailPainter extends CustomPainter {
  _TrailPainter(this.color, this.reverse);
  final Color color;
  final bool reverse;
  @override
  void paint(Canvas canvas, Size size) {
    final a = size.width * (reverse ? .62 : .38);
    final b = size.width * (reverse ? .38 : .62);
    final path = Path()
      ..moveTo(a, 0)
      ..cubicTo(a, size.height * .65, b, size.height * .35, b, size.height);
    canvas.drawPath(
      path,
      Paint()
        ..color = color
        ..style = PaintingStyle.stroke
        ..strokeWidth = 3
        ..strokeCap = StrokeCap.round,
    );
  }

  @override
  bool shouldRepaint(covariant _TrailPainter old) =>
      old.color != color || old.reverse != reverse;
}

class CompletionMoment extends StatelessWidget {
  const CompletionMoment({super.key, required this.title});
  final String title;
  @override
  Widget build(BuildContext c) => Container(
    width: double.infinity,
    padding: const EdgeInsets.all(24),
    decoration: BoxDecoration(
      color: Theme.of(c).colorScheme.primaryContainer.withValues(alpha: .25),
      borderRadius: BorderRadius.circular(28),
    ),
    child: Column(
      children: [
        const Mascot(height: 128, use: CompanionUse.completion),
        const SizedBox(height: 12),
        Semantics(
          header: true,
          child: Text(
            title,
            textAlign: TextAlign.center,
            style: Theme.of(c).textTheme.headlineMedium,
          ),
        ),
        const SizedBox(height: 12),
        const Text(
          'Một bước nhỏ để dùng ngôn ngữ trong cuộc sống.',
          textAlign: TextAlign.center,
        ),
      ],
    ),
  );
}

class EvidenceFact extends StatelessWidget {
  const EvidenceFact({
    super.key,
    required this.value,
    required this.label,
    required this.icon,
  });
  final String value, label;
  final IconData icon;
  @override
  Widget build(BuildContext c) => Padding(
    padding: const EdgeInsets.symmetric(vertical: 12),
    child: Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Icon(icon, color: Theme.of(c).colorScheme.primary),
        const SizedBox(width: 16),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(value, style: Theme.of(c).textTheme.titleLarge),
              Text(label, style: Theme.of(c).textTheme.bodyMedium),
            ],
          ),
        ),
      ],
    ),
  );
}
