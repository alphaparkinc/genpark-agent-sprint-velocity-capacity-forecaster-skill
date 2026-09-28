from client import SprintCapacityForecaster

forecaster = SprintCapacityForecaster()
res = forecaster.forecast(68.0, 6, 4, 15.0)
print("=== Sprint Velocity & Capacity Forecast ===")
print("Planned Points:", res["planned_points"])
print("Net Available Capacity:", res["net_capacity"])
print("Completion Probability:", f"{res['completion_probability']*100}%")
print("Risk Level:", res["risk_assessment"])
print("Recommended Action:", res["recommended_action"])
