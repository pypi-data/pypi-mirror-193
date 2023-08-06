import pytest
from whitebox import schemas
from whitebox.tests.v1.conftest import get_order_number, state
from fastapi import status


@pytest.mark.order(get_order_number("model_integrity_metrics_get_model_all"))
def test_model_integrity_metric_get_model_all(client, api_key):
    response_multi = client.get(
        f"/v1/model-integrity-metrics?model_id={state.model_multi['id']}",
        headers={"api-key": api_key},
    )
    response_binary = client.get(
        f"/v1/model-integrity-metrics?model_id={state.model_binary['id']}",
        headers={"api-key": api_key},
    )
    response_wrong_model = client.get(
        f"/v1/model-integrity-metrics?model_id=wrong_model_id",
        headers={"api-key": api_key},
    )

    assert len(response_multi.json()) == 1
    assert len(response_binary.json()) == 1

    assert response_multi.status_code == status.HTTP_200_OK
    assert response_binary.status_code == status.HTTP_200_OK
    assert response_wrong_model.status_code == status.HTTP_404_NOT_FOUND

    validated = [schemas.ModelIntegrityMetric(**m) for m in response_multi.json()]
    validated = [schemas.ModelIntegrityMetric(**m) for m in response_binary.json()]
