import pandas as pd
from time import strptime

from .count_burrows_detection import filter_dates


def interval_in_hours(string_time: str):
    time_format = strptime(string_time, "%H:%M:%S")
    return time_format.tm_hour + time_format.tm_min / 60 + time_format.tm_sec / 3600


def add_duration_in_hours_column(effort_data: pd.DataFrame):
    effort_data_copy = effort_data.copy()
    effort_data_copy.loc[:, "Duracion"] = effort_data_copy.Duracion.fillna("00:00:00")
    duration_in_hours = effort_data_copy.Duracion.apply(interval_in_hours)
    effort_data_copy = effort_data_copy.assign(Duration_hr=duration_in_hours)
    return effort_data_copy


def make_summary_of_effort_and_distance(
    effort_df: pd.DataFrame, start_date="2000-01-01", end_date="2023-01-30"
):
    filtered_dataframe = filter_dates(effort_df, start_date, end_date)
    column_added = add_duration_in_hours_column(filtered_dataframe)
    grouped_dataframe = column_added.groupby("Nombre_k9")[["Distancia", "Duration_hr"]].aggregate(
        "sum"
    )
    return grouped_dataframe.rename(
        columns={"Distancia": "Total_distance", "Duration_hr": "Total_time"}
    )
