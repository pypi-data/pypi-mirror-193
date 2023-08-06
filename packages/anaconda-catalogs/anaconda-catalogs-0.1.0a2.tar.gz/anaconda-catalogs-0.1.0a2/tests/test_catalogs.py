from __future__ import annotations

from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING
from typing import Any

import intake
import pytest
import yaml

import anaconda_catalogs
from anaconda_catalogs import AnacondaCatalog

if TYPE_CHECKING:
    from _pytest.monkeypatch import MonkeyPatch


@pytest.fixture()
def mocked_catalogs_service(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    """Monkey-patch `anaconda_catalogs.AnacondaCatalog` to return test data from a mock API."""
    catalog_yaml = dedent(
        """\
        sources:
            wind_turbines:
              args:
                urlpath: "zip://*.csv::https://eerscmap.usgs.gov/uswtdb/assets/data/uswtdbCSV.zip"

                csv_kwargs:
                  assume_missing: true

              description: "US Wind Turbine Database"
              driver: csv
        """
    )

    def _get_mocked_catalog_spec(self: AnacondaCatalog) -> dict[str, Any]:
        return yaml.safe_load(catalog_yaml)

    monkeypatch.setattr(
        AnacondaCatalog,
        "_get_catalog_spec",
        _get_mocked_catalog_spec,
    )


@pytest.mark.parametrize("method", ["direct_import", "plugin"])
@pytest.mark.usefixtures("mocked_catalogs_service")
def test_open_catalog(method: str):
    # Open the catalog
    if method == "direct_import":
        cat = anaconda_catalogs.open_catalog("cid/not-a-real-catalog")
    elif method == "plugin":
        cat = intake.open_anaconda_catalog("cid/not-a-real-catalog")
    else:
        raise ValueError("Unreachable")

    # There are data sources
    assert list(cat)

    # The "wind_turbine" data source exists in the catalog
    assert "wind_turbines" in cat
