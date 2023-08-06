import pathlib
from os import environ, remove

import pytest

from jira_tool.excel_definition import *
from jira_tool.excel_operation import *
from jira_tool.jira_client import *
from jira_tool.jira_configuration import *
from jira_tool.sprint_schedule import *

HERE = pathlib.Path(__file__).resolve().parent
SRC_ASSETS: pathlib.Path = HERE.parent / "src/jira_tool/assets"


class TestExcelOperation:
    def test_read_excel_file(self):
        excel_definition = ExcelDefinition()
        excel_definition.load_file(SRC_ASSETS / "excel_definition.json")
        sprint_schedule = SprintScheduleStore()
        sprint_schedule.load_file(SRC_ASSETS / "sprint_schedule.json")

        columns, stories = read_excel_file(
            HERE / "files/happy_path.xlsx", excel_definition, sprint_schedule
        )
        assert len(columns) == 24
        assert len(stories) == 8

    @pytest.mark.skipif(
        environ.get("JIRA_ACCESS_TOKEN") is None, reason="Security Consideration."
    )
    def test_process_excel_file(self):
        process_excel_file(
            HERE / "files/happy_path.xlsx",
            HERE / "files/happy_path_sorted.xlsx",
            excel_definition_file=str(SRC_ASSETS / "excel_definition.json"),
            sprint_schedule_file=str(SRC_ASSETS / "sprint_schedule.json"),
        )

        excel_definition = ExcelDefinition()
        excel_definition.load_file(SRC_ASSETS / "excel_definition.json")
        sprint_schedule = SprintScheduleStore()
        sprint_schedule.load_file(SRC_ASSETS / "sprint_schedule.json")

        _, stories = read_excel_file(
            HERE / "files/happy_path_sorted.xlsx", excel_definition, sprint_schedule
        )

        assert len(stories) == 8

        jira_client = JiraClient(environ["JIRA_URL"], environ["JIRA_ACCESS_TOKEN"])

        noneed_sort_statuses = get_no_need_sort_statuses()

        for i in range(len(stories) - 1):
            story_id_0 = stories[i]["storyId"].lower().strip()
            story_id_1 = stories[i + 1]["storyId"].lower().strip()
            query_result = jira_client.get_stories_status([story_id_0, story_id_1])
            if (
                query_result[story_id_0].upper() not in noneed_sort_statuses
                and query_result[story_id_1].upper() not in noneed_sort_statuses
            ):
                assert stories[i] >= stories[i + 1]

        remove(HERE / "files/happy_path_sorted.xlsx")
