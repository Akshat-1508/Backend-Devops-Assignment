import json
import os

from app.core.config import REPORT_FOLDER


def save_report(job_id, summary):

    os.makedirs(REPORT_FOLDER, exist_ok=True)

    report = {
        "job_id": job_id,
        "summary": summary
    }

    filename = os.path.join(
        REPORT_FOLDER,
        f"report_{job_id}.json"
    )

    with open(filename, "w") as file:
        json.dump(report, file, indent=4)

    return filename