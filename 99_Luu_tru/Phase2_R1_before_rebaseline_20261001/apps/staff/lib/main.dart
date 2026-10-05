import 'package:flutter/material.dart';

void main() => runApp(const FoundationApp());

class FoundationApp extends StatelessWidget {
  const FoundationApp({super.key});

  @override
  Widget build(BuildContext context) => MaterialApp(
    debugShowCheckedModeBanner: false,
    title: 'Adaptive Language Learning',
    theme: ThemeData(
      colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF216B5D)),
      useMaterial3: true,
    ),
    home: Scaffold(
      appBar: AppBar(title: const Text('Learning workspace')),
      body: const SafeArea(
        child: Center(
          child: Padding(
            padding: EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(Icons.menu_book_outlined, size: 64),
                SizedBox(height: 24),
                Text('Content and learner tools will appear here.', textAlign: TextAlign.center),
              ],
            ),
          ),
        ),
      ),
    ),
  );
}
