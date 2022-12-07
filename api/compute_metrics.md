# compute_metrics {#sec-compute_metrics}

`compute_metrics(data: pd.DataFrame, date_var: str, period: timedelta, metric_set: list, truth: str, estimate: str, kw)`

Compute metrics for given time period

## Parameters

| Name         | Type               | Description                                                                | Default   |
|--------------|--------------------|----------------------------------------------------------------------------|-----------|
| `data`       | DataFrame          | Pandas dataframe                                                           | required  |
| `date_var`   | str                | Column in `data` containing dates                                          | required  |
| `period`     | datetime.timedelta | Defining period to group by                                                | required  |
| `metric_set` | list               | List of metrics to compute, that have the parameters `y_true` and `y_pred` | required  |
| `truth`      | str                | Column name for true results                                               | required  |
| `estimate`   | str                | Column name for predicted results                                          | required  |

Example
-------
>>> from datetime import timedelta
>>> import pandas as pd
>>> from sklearn.metrics import mean_squared_error, mean_absolute_error
>>> df = pd.DataFrame(
...   {
...        "index": ["2021-01-01", "2021-01-02", "2021-01-03"],
...        "truth": [200, 201, 199],
...        "pred": [198, 200, 199],
...   }
... )
>>> td = timedelta(days = 1)
>>> metric_set = [mean_squared_error, mean_absolute_error]
>>> metrics = compute_metrics(df, "index", td, metric_set, "truth", "pred")