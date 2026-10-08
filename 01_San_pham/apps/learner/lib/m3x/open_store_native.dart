import 'package:path_provider/path_provider.dart';
import 'learning_store.dart';

Future<FileLearningStore> openNativeStore(String name) async {
  final directory = await getApplicationSupportDirectory();
  return FileLearningStore(
    '${directory.path}/m3x_authenticated_fixture/$name.json',
  );
}
