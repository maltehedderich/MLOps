from dagster import repository
from dagster_repo.example.graph import wine_rfc_dev_job
from dagster_repo.presets import calories_test_job

# start_repo_marker


@repository
def dev_repo():
    return [calories_test_job, wine_rfc_dev_job]


# end_repo_marker
