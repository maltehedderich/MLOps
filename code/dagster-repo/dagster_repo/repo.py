from dagster import repository
from dagster_repo.example.wine_rfc.graph import wine_rfc_dev_job
from dagster_repo.example.publish_model.graph import publish_bento_job
from dagster_repo.example.create_buckets import create_buckets_dev_job

# start_repo_marker


@repository
def dev_repo():
    return [
        wine_rfc_dev_job,
        create_buckets_dev_job,
        publish_bento_job,
    ]


# end_repo_marker
