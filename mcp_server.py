import sys
import json
from client import SprintCapacityForecaster

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "forecast_sprint_capacity",
                        "description": "Simulates sprint completion probability based on historical velocity distributions and PTO burden.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "planned_points": {"type": "number"},
                                "engineers": {"type": "integer"},
                                "pto_days": {"type": "integer"},
                                "tech_debt_buffer_pct": {"type": "number"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        forecaster = SprintCapacityForecaster()
        res = forecaster.forecast(
            args.get("planned_points", 68.0),
            args.get("engineers", 6),
            args.get("pto_days", 4),
            args.get("tech_debt_buffer_pct", 15.0)
        )
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    forecaster = SprintCapacityForecaster()
    print(json.dumps(forecaster.forecast(), indent=2))

if __name__ == "__main__":
    main()
