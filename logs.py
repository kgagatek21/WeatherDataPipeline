from datetime import datetime


def execution_log_append(logs, run_id, pipeline_name, df, passed):
    logs.append({
        "run_id": run_id,
        "pipeline_name": pipeline_name,
        "start_time": datetime.now(),
        "end_time": datetime.now(),
        "rows_processed": len(df),
        "status": "PASS" if passed else "FAIL",
        "error_message": ""
    })


def quality_log_append(logs, run_id, check_name, value, passed):
    logs.append({
        "run_id": run_id,
        "timestamp": datetime.now(),
        "check_name": check_name,
        "value": value,
        "status": "PASS" if passed else "FAIL"
    })
