enum LessonDomain { vocabulary, grammar, listening }

abstract final class LessonContent {
  static String title(LessonDomain d) => switch (d) {
    LessonDomain.vocabulary => 'Chào hỏi và làm quen',
    LessonDomain.grammar => 'Giới thiệu một người',
    LessonDomain.listening => 'Nghe lời chào',
  };
  static String question(LessonDomain d, String id) => switch (d) {
    LessonDomain.grammar =>
      id == 'L-025'
          ? 'Bạn giới thiệu hai người bạn. Điền từ còn thiếu: They ___ classmates.'
          : id == 'L-027'
          ? 'Bạn giới thiệu giáo viên. Điền từ còn thiếu: He ___ my teacher.'
          : id == 'L-022'
          ? 'Chọn câu giới thiệu đúng.'
          : 'Điền từ còn thiếu: She ___ a student.',
    LessonDomain.listening =>
      id == 'L-025'
          ? 'Một người bạn mới nói lời trong đoạn nghe. Chọn cách đáp lại phù hợp.'
          : id == 'L-027'
          ? 'Nhận biết lời chào trong đoạn nghe ở lớp học.'
          : 'Bạn nghe lời nào trong đoạn âm thanh?',
    LessonDomain.vocabulary =>
      id == 'L-025'
          ? 'Trong chuyến du lịch, bạn gặp người hàng xóm mới vào buổi sáng. Bạn chào thế nào?'
          : id == 'L-027'
          ? 'Bạn đến lớp vào buổi sáng. Bạn chào giáo viên thế nào?'
          : 'Bạn gặp một người bạn vào buổi sáng. Bạn nói gì?',
  };
  static List<String> answers(LessonDomain d, String id) => switch (d) {
    LessonDomain.grammar =>
      id == 'L-022'
          ? ['She is a student.', 'She are a student.', 'She am a student.']
          : id == 'L-025'
          ? ['are', 'is', 'am']
          : ['is', 'are', 'am'],
    LessonDomain.listening => ['Hello!', 'Good night!', 'Thank you!'],
    LessonDomain.vocabulary => [
      'Good morning!',
      'Good night!',
      'See you later!',
    ],
  };
  static String example(LessonDomain d) => switch (d) {
    LessonDomain.grammar => 'She is a student.',
    LessonDomain.listening => 'Hello!',
    LessonDomain.vocabulary => 'Good morning!',
  };
  static String explanation(LessonDomain d, String id) => switch (d) {
    LessonDomain.grammar =>
      id == 'L-025'
          ? 'Với “they”, dùng “are” để giới thiệu nhiều người.'
          : 'Với “she” hoặc “he”, dùng “is” để giới thiệu một người.',
    LessonDomain.listening =>
      'Đoạn mẫu nói “Hello”, một lời chào. Yêu cầu phát không chứng minh rằng bạn đã nghe.',
    LessonDomain.vocabulary => '“Good morning” dùng vào buổi sáng.',
  };
}
