from algora.api.data.query.model import TimeseriesQueryRequest


def _query_datasets_request_info(id: str, data=None, json=None) -> dict:
    return {"endpoint": f"data/datasets/query/{id}", "data": data, "json": json}


def _query_dataset_csv_request_info(id: str, data=None) -> dict:
    return {"endpoint": f"data/datasets/query/{id}.csv", "data": data}


def _query_timeseries_request_info(request: TimeseriesQueryRequest) -> dict:
    return {"endpoint": f"data/timeseries", "json": request.request_dict()}
