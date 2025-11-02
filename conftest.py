import pytest

def pytest_terminal_summary(terminalreporter, exitstatus):
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get("passed", []))
    failed = len(terminalreporter.stats.get("failed", []))
    skipped = len(terminalreporter.stats.get("skipped", []))

    terminalreporter.write_sep("-", "📊 PODSUMOWANIE TESTÓW 📊")
    terminalreporter.write_line(f"✅ ZDANE TESTY: {passed}")
    terminalreporter.write_line(f"❌ NIEZALICZONE TESTY: {failed}")
    terminalreporter.write_line(f"⏭️ POMINIĘTE TESTY: {skipped}")
    terminalreporter.write_line(f"📦 ŁĄCZNIE TESTÓW: {total}")
