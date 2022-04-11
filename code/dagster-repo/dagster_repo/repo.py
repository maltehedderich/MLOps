from dagster import repository
from dagster_repo.presets import calories_test_job

# start_repo_marker


@repository
def dev_repo():
    return [calories_test_job]


# end_repo_marker
