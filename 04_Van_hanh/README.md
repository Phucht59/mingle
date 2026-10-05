# Vận hành Mingo

- [Runbook](Runbook/) — chạy nền tảng, API/worker, database, Flutter và originals V3.2.
- [Cau_hinh](Cau_hinh/) — môi trường và secrets.
- [Trien_khai](Trien_khai/) — CI/CD; workflow thực thi vẫn ở `.github/workflows/` tại root.
- [Scripts](Scripts/) — bootstrap và verification executables.
- [tests](tests/) — adapter guards gắn với scripts.

Database: application role `mingo_app`, application database `mingo`, disposable automated-test database `mingo_test`. API và worker chia sẻ backend codebase. Không tạo database/service theo phase. Chưa có production deployment hoặc Monitoring/runbook artifacts độc lập mới trong migration này; không tạo folder rỗng để giả định đã triển khai.
