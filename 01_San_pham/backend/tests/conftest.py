import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--run-postgres", action="store_true", help="Run destructive tests in disposable *_test DB"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "postgres: requires a real disposable PostgreSQL database")


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run-postgres"):
        for item in items:
            if "postgres" in item.keywords:
                item.add_marker(
                    pytest.mark.skip(
                        reason="Use --run-postgres with TEST_DATABASE_URL; NOT verified"
                    )
                )
