# coding: utf-8
"""Tests Météo-France module. Forecast class."""
from unittest.mock import Mock

import marshmallow
import pytest
from tests.fixtures import get_file_content

from meteofrance_api import MeteoFranceClient
from meteofrance_api.const import METEOFRANCE_API_URL


def test_rain() -> None:
    """Test rain forecast on a covered zone."""
    client = MeteoFranceClient()

    rain = client.get_rain(latitude=48.8075, longitude=2.24028)

    assert type(rain.geometry) == dict
    assert type(rain.update_time) == int
    assert "rain_intensity" in rain.properties["forecast"][0].keys()
    assert "rain_intensity_description" in rain.properties["forecast"][0].keys()


def test_rain_not_covered() -> None:
    """Test rain forecast result on a non covered zone."""
    client = MeteoFranceClient()

    with pytest.raises(marshmallow.ValidationError):
        client.get_rain(latitude=45.508, longitude=-73.58)


def test_rain_expected(requests_mock: Mock) -> None:
    """Test datecomputation when rain is expected within the hour."""
    client = MeteoFranceClient()

    requests_mock.request(
        "get",
        f"{METEOFRANCE_API_URL}/rain",
        text=get_file_content("tests/fixtures/rain_expected.json"),
    )

    rain = client.get_rain(latitude=48.8075, longitude=2.24028)
    date_rain = rain.next_rain_date_locale()
    assert str(date_rain) == "2020-05-20 19:50:00+02:00"
    assert (
        str(rain.timestamp_to_locale_time(rain.properties["forecast"][3]["time"]))
        == "2020-05-20 19:50:00+02:00"
    )


def test_no_rain_expected(requests_mock: Mock) -> None:
    """Test datecomputation when rain is expected within the hour."""
    client = MeteoFranceClient()

    requests_mock.request(
        "get",
        f"{METEOFRANCE_API_URL}/rain",
        text=get_file_content("tests/fixtures/rain_not_expected.json"),
    )

    rain = client.get_rain(latitude=48.8075, longitude=2.24028)
    assert rain.next_rain_date_locale() is None
