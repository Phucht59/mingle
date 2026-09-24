"""Always fail closed until a reviewed adapter to the original suite is supplied."""
import json
raise SystemExit(json.dumps({"status": "BLOCKED", "reason": "Exact V3.2 sources and original suites absent", "contract_checks": "NOT_RUN", "sql_checks": "NOT_RUN"}))
