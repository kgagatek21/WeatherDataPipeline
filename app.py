from transform import transform_data, basic_statistics
from api import api_data
import pandas as pd
from sqlalchemy import create_engine
import uuid
from logs import execution_log_append


# Weather data for Buckingham Palace, London UK
buckingham_coords = (51.501476, -0.140634)
start_date = "2026-09-22"
end_date = "2026-09-22"
df = pd.DataFrame(api_data(buckingham_coords, start_date, end_date))

run_id = str(uuid.uuid4())
quality_logs = []

clean_df = transform_data(df, quality_logs, run_id)

quality_logs_df = pd.DataFrame(data=quality_logs)

execution_log = []
execution_log_append(
    execution_log,
    run_id,
    "weather data",
    df,
    (quality_logs_df["status"] != "FAIL").any()
)
execution_log_df = pd.DataFrame(data=execution_log)

engine = create_engine("sqlite:///weather.db")
clean_df.to_sql("hourly_weather", engine, if_exists="append", index=False)
quality_logs_df.to_sql("quality_logs", engine, if_exists="append", index=False)
execution_log_df.to_sql("execution_logs", engine,
                        if_exists="append", index=False)

# df_from_sql = pd.read_sql("SELECT * FROM hourly_weather", engine)

# print(df_from_sql)
