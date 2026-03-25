# API Structure

This document describes the API used in the AI Web Dashboard.

---

## 1. Get Dashboard Data

- **URL:** /api/data/
- **Method:** GET
- **Description:** Returns all data required for the dashboard including summary, logs, and analytics.

---

### Response:

```json
{
  "summary": {
    "totalTasks": 10,
    "runningTasks": 3,
    "completedTasks": 5,
    "failedTasks": 2
  },
  "logs": [
    {
      "time": "2026-03-25T10:00:00",
      "status": "Running",
      "message": "Task started"
    }
  ],
  "metrics": {
    "labels": ["10:00", "10:05"],
    "running": [2, 3],
    "completed": [1, 2]
  }
}
