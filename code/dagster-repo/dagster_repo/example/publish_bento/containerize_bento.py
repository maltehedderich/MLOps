import docker
from dagster import op


@op
def build_image(context, path):
    client = docker.DockerClient()
    client.images.build(path=path.absolute())
