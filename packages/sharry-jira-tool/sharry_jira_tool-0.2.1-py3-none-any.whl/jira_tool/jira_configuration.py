from json import loads
from pathlib import Path
from typing import Optional

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"

__all__ = ["get_no_need_sort_statuses"]


def get_no_need_sort_statuses(file: "Optional[str | Path]" = None) -> "list[str]":
    file_path: Optional[str | Path] = None
    if file is None:
        file_path = ASSETS / "jira_configuration.json"
    else:
        file_path = file

    with open(file=file_path, mode="r") as status_mapping_file:
        try:
            raw_data = loads(status_mapping_file.read())

            if (
                "StatusesNoNeedAnticipateSort" in raw_data
                and type(raw_data["StatusesNoNeedAnticipateSort"]) is list
            ):
                return [item for item in raw_data["StatusesNoNeedAnticipateSort"]]
            else:
                return []
        except Exception:
            raise ValueError(
                f"The JSON structure is invalid. File: {file_path}. Please check the documentation: https://github.com/SharryXu/jira-tool"
            )
        finally:
            status_mapping_file.close()
