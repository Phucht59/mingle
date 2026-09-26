"""Adapter guards; separate from the unchanged original 115 + 22 suites."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

path = Path(__file__).resolve().parents[1] / "scripts/check_original_contracts.py"
spec = importlib.util.spec_from_file_location("original_adapter", path)
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)


class AdapterGuards(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.source.mkdir()
        self.manifest = self.source / "MANIFEST.json"
        self.manifest.write_text(json.dumps({"version": "fixture"}), encoding="utf-8")
        self.sums = self.root / "SHA256SUMS.txt"
        digest = hashlib.sha256(self.manifest.read_bytes()).hexdigest()
        self.sums.write_text(digest + "  MANIFEST.json\n", encoding="utf-8")

    def test_intact_source(self):
        self.assertEqual(adapter.verify_source(self.source, self.sums)[1], 1)

    def test_missing_file_rejected(self):
        self.manifest.unlink()
        with self.assertRaises(ValueError):
            adapter.verify_source(self.source, self.sums)

    def test_changed_bytes_rejected(self):
        self.manifest.write_text("{}", encoding="utf-8")
        with self.assertRaises(ValueError):
            adapter.verify_source(self.source, self.sums)

    def test_extra_file_rejected(self):
        (self.source / "extra").write_text("unexpected", encoding="utf-8")
        with self.assertRaises(ValueError):
            adapter.verify_source(self.source, self.sums)

    def test_path_escape_rejected(self):
        self.sums.write_text("0" * 64 + "  ../escape\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            adapter.verify_source(self.source, self.sums)

    def test_report_counts_derived_from_checks(self):
        report = {"passed": 2, "failed": 0, "checks": ["PASS first", "PASS second"]}
        self.assertEqual(adapter.validate_report(report, "contract", 2)["passed"], 2)

    def test_false_summary_rejected(self):
        report = {"passed": 2, "failed": 0, "checks": ["PASS first", "FAIL second"]}
        with self.assertRaises(ValueError):
            adapter.validate_report(report, "contract", 2)

    def test_missing_checks_rejected(self):
        report = {"passed": 1, "failed": 0, "checks": ["PASS first"]}
        with self.assertRaises(ValueError):
            adapter.validate_report(report, "contract", 2)

    def test_sql_failure_rejected(self):
        report = {"passed": 0, "failed": 1, "checks": [{"status": "FAIL"}]}
        with self.assertRaises(ValueError):
            adapter.validate_report(report, "sql", 1)


if __name__ == "__main__":
    unittest.main()
