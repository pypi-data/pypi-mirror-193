import pytest
from whitebox.tests.v1.mock_data import (
    model_monitor_accuracy_create_payload,
    model_monitor_f1_create_payload,
    model_monitor_data_drift_create_payload,
    model_monitor_concept_drift_create_payload,
    model_monitor_precision_create_payload,
    model_monitor_r_square_create_payload,
)
from whitebox import schemas
from whitebox.tests.v1.conftest import get_order_number, state
from fastapi import status


@pytest.mark.order(get_order_number("model_monitor_create"))
def test_model_monitor_create(client, api_key):
    accuracy_monitor = client.post(
        "/v1/model-monitors",
        json={
            **model_monitor_accuracy_create_payload,
            "model_id": state.model_multi["id"],
        },
        headers={"api-key": api_key},
    )

    f1_monitor = client.post(
        "/v1/model-monitors",
        json={
            **model_monitor_f1_create_payload,
            "model_id": state.model_multi["id"],
        },
        headers={"api-key": api_key},
    )

    data_drift_monitor = client.post(
        "/v1/model-monitors",
        json={
            **model_monitor_data_drift_create_payload,
            "model_id": state.model_binary["id"],
        },
        headers={"api-key": api_key},
    )

    concept_drift_monitor = client.post(
        "/v1/model-monitors",
        json={
            **model_monitor_concept_drift_create_payload,
            "model_id": state.model_binary["id"],
        },
        headers={"api-key": api_key},
    )

    precision_monitor = client.post(
        "/v1/model-monitors",
        json={
            **model_monitor_precision_create_payload,
            "model_id": state.model_binary["id"],
        },
        headers={"api-key": api_key},
    )

    r_square_monitor = client.post(
        "/v1/model-monitors",
        json={
            **model_monitor_r_square_create_payload,
            "model_id": state.model_regression["id"],
        },
        headers={"api-key": api_key},
    )

    assert accuracy_monitor.status_code == status.HTTP_201_CREATED
    validated = schemas.ModelMonitor(**accuracy_monitor.json())


@pytest.mark.order(get_order_number("model_monitors_get_model_all"))
def test_model_monitors_get_model_all(client, api_key):
    response_multi = client.get(
        f"/v1/model-monitors?model_id={state.model_multi['id']}",
        headers={"api-key": api_key},
    )
    response_all = client.get(
        f"/v1/model-monitors",
        headers={"api-key": api_key},
    )
    response_wrong_model = client.get(
        f"/v1/model-monitors?model_id=wrong_model_id",
        headers={"api-key": api_key},
    )

    assert len(response_multi.json()) == 2
    assert len(response_all.json()) == 6

    assert response_multi.status_code == status.HTTP_200_OK
    assert response_all.status_code == status.HTTP_200_OK
    assert response_wrong_model.status_code == status.HTTP_404_NOT_FOUND

    validated = [schemas.ModelMonitor(**m) for m in response_multi.json()]
    validated = [schemas.ModelMonitor(**m) for m in response_all.json()]
