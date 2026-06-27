from app.services.cleaner import clean_csv
from app.services.anomaly import detect_anomalies
from app.services.llm_service import generate_summary

from app.services.report import save_report

def process_pipeline(file_path):

    df = clean_csv(file_path)

    df = detect_anomalies(df)

    summary = generate_summary(df)

    save_report(job_id, ai_summary)
    
    return df, summary