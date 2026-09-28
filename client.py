"""Autonomous Sprint Velocity & Capacity Forecaster Engine.
100% Python Standard Library.
"""

from typing import Dict, Any

class SprintCapacityForecaster:
    """Simulates sprint completion probability based on historical velocity distributions and PTO burden."""
    def __init__(self, historical_velocity: float = 62.5):
        self.base_velocity = historical_velocity

    def forecast(self, planned_points: float = 68.0, engineers: int = 6, pto_days: int = 4, tech_debt_buffer_pct: float = 15.0) -> Dict[str, Any]:
        effective_days = (engineers * 10) - pto_days
        capacity_ratio = effective_days / (engineers * 10)
        net_capacity = round((self.base_velocity * capacity_ratio) * (1.0 - (tech_debt_buffer_pct / 100.0)), 1)
        load_ratio = round(planned_points / max(1.0, net_capacity), 2)
        prob = round(max(0.20, min(0.98, 1.0 - max(0.0, (load_ratio - 1.0) * 1.5))), 2)
        risk = "HEALTHY" if prob >= 0.85 else ("MODERATE_OVERCOMMIT" if prob >= 0.65 else "CRITICAL_OVERCOMMIT")
        return {
            "planned_points": planned_points,
            "net_capacity": net_capacity,
            "load_ratio": load_ratio,
            "completion_probability": prob,
            "risk_assessment": risk,
            "recommended_action": "Scope on track" if risk == "HEALTHY" else f"Descope approximately {int(planned_points - net_capacity)} points before sprint freeze."
        }
