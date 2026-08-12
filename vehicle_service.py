import json
from datetime import date

vehicles = [
    {
        "vehicle_id": "V001",
        "vehicle_number": "TN-37-AB-1234",
        "owner": "Arun Kumar",",
        "service_due": "2026-08-15",
        "status": "Due Soon"
    },
    {
        "vehicle_id": "V002",
        "vehicle_number": "TN-38-CD-5678",
        "owner": "Priya",
        "service_due": "2026-08-05",
        "status": "Overdue"
    },
    {
        "vehicle_id": "V003",
        "vehicle_number": "TN-39-EF-9012",
        "owner": "Kumar",
        "service_due": "2026-09-10",
        "status": "Scheduled"
    },
    {
        "vehicle_id": "V004",
        "vehicle_number": "TN-40-GH-3456",
        "owner": "Divya",
        "service_due": "2026-08-20",
        "status": "Due Soon"
    }
]

metrics = {
    "Total_Vehicles": len(vehicles),
    "Overdue": sum(v["status"] == "Overdue" for v in vehicles),
    "Due_Soon": sum(v["status"] == "Due Soon" for v in vehicles),
    "Scheduled": sum(v["status"] == "Scheduled" for v in vehicles),
    "Vehicles": vehicles
}

with open("vehicle_metrics.json", "w") as file:
    json.dump(metrics, file, indent=4)

print("====================================")
print(" VEHICLE SERVICE MONITORING SYSTEM")
print("====================================")
print("Total Vehicles :", metrics["Total_Vehicles"])
print("Overdue        :", metrics["Overdue"])
print("Due Soon       :", metrics["Due_Soon"])
print("Scheduled      :", metrics["Scheduled"])
print("====================================")
print("Metrics generated successfully!")
