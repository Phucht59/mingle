import 'package:flutter/material.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/semantics.dart';
import 'package:mingo_ui/mingo_ui.dart';

// Compile-time review parameters, never a learner-facing QA toolbar.
void main() {
  WidgetsFlutterBinding.ensureInitialized();
  if(kIsWeb){SemanticsBinding.instance.ensureSemantics();}
  runApp(const FoundationApp());
}
class FoundationApp extends StatelessWidget {
  const FoundationApp({super.key});
  @override Widget build(BuildContext context) => const StaffApp(
    initialScreen: String.fromEnvironment('MINGO_REVIEW_SCREEN',defaultValue:'S-010'),
    reviewState: bool.hasEnvironment('MINGO_REVIEW_STATE') ? String.fromEnvironment('MINGO_REVIEW_STATE') : null,
  );
}
