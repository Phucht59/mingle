import 'learning_store.dart';

Future<LearningStore> openNativeStore(String name) => Future.error(
  UnsupportedError(
    'Durable native proof requires Android/iOS/desktop storage.',
  ),
);
