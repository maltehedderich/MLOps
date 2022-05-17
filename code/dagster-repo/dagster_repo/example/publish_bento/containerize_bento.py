import docker
from dagster import op


@op
def build_image(context, path):
    client = docker.DockerClient()
    image, log_gen = client.images.build(path=str(path), rm=True)
    return image.id


@op
def run_image(context, image_id):
    client = docker.DockerClient()
    client.containers.run(
        image_id, detach=True, ports={"5000/tcp": context.op_config["port"]}
    )
