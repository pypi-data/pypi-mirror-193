import os
import subprocess

import click
import docker
from yaspin import yaspin

__author__ = "Rubbrband"

try:
    client = docker.from_env()
except docker.errors.DockerException:
    click.echo("Docker is not running. Please start Docker and try again.")
    exit()

# read db from csv file called db.csv and store in a dictionary

db = {
    "ControlNet": {
        "description": "An image model to control diffusion models by adding extra conditions",
        "shape": "(512,512,3)",
    },
    "LoRA": {
        "description": "Fine-tune Stable diffusion models twice as fast than dreambooth method, by Low-rank Adaptation",
        "shape": "anything",
    },
    "Dreambooth-Stable-Diffusion": {
        "description": "Stable diffusion models, trained with dreambooth method",
        "shape": "anything",
    },
}


@click.group()
def main():
    """
    Rubbrband - A CLI for launching ML models.

    The Rubbrband CLI launches a model with all the installed dependencies for a given GitHub repository.

    The user can interact directly with the launched model using a Jupyter Notebook at http://localhost:8888.
    """
    pass


@main.command()
def models():
    """List all supported models"""
    click.echo("Supported Models:")
    click.echo(f"{'NAME':12} DESCRIPTION")
    for key, val in db.items():
        click.echo(f"{key:12} {val['description']}")


@main.command()
def ls():
    """List all running ML models"""
    click.echo("Running Models:")
    containers = client.containers.list()

    # filter containers that start with rb-
    for container in containers:
        if container.name.startswith("rb-"):
            click.echo(container.name)


@main.command()
@click.argument("model")
def launch(model):
    """
    Launch a new MODEL.

    MODEL is the name of the model to launch.

    Example: rubbrband launch ControlNet
    """

    if model not in db:
        click.echo("Model not found")
        return

    with yaspin() as sp:
        sp.text = "Setting Up Environment. This may take up to 10 minutes."
        image_name = f"rubbrband/{model.lower()}"
        # pull image if not already pulled
        try:
            client.images.get(image_name)
        except docker.errors.ImageNotFound:
            client.images.pull(image_name)

    with yaspin() as sp:
        sp.text = f"Finished. Run rubbrband train {model} to train this model on sample data."


@main.command()
@click.argument("model")
def enter(model):
    """
    Enter into a running MODEL.

    MODEL is the name of the model.

    Example: rubbrband enter ControlNet
    """
    # if container not running, start it
    with yaspin() as sp:
        sp.text = "Launching Docker Container"

        container_name = f"rb-{model.lower()}"
        try:
            container = client.containers.get(container_name)
        except docker.errors.NotFound:
            client.containers.run(container_name, detach=True, name=container_name, tty=True, stdin_open=True)

        container = client.containers.get(container_name)

        if container.status != "running":
            container.start()

    subprocess.run(["docker", "exec", "-it", container_name, "/bin/bash"])


# '''name''' corresponds to the name column in db.csv
# the option '''-d''' or '''--dataset_dir''' is the path to the dataset directory
# this directory gets mounted to the container at /home/engineering/data
@main.command(
    context_settings=dict(
        ignore_unknown_options=True,
        allow_extra_args=True,
    )
)
@click.argument("model")
@click.option(
    "-d",
    "--dataset_dir",
    prompt="Path to dataset directory",
    type=click.Path(exists=True),
    help="Path to the local dataset directory that is mounted to the container at /home/engineering/data.",
)
@click.pass_context
def train(ctx, model, dataset_dir):
    """
    Train a MODEL.

    MODEL is the name of the model to train. \n
    --dataset_dir is the local path that gets mounted to the container at /home/engineering/data.

    Example: rubbrband train --dataset_dir /my_data ControlNet
    """

    if model not in db:
        click.echo("Model not found")
        return

    image_name = f"rubbrband/{model.lower()}"
    container_name = f"rb-{model.lower()}"
    if not client.images.get(image_name):
        client.images.pull(image_name)

    abs_path = os.path.abspath(dataset_dir)

    try:
        container = client.containers.get(container_name)

        # stop and remove container if it is already running
        if container.status == "running":
            container.stop()
            container.remove()

    except docker.errors.NotFound:
        pass
    try:
        subprocess.check_output("nvidia-smi")
        device_requests = [docker.types.DeviceRequest(count=-1, capabilities=[["gpu"]])]
    except (
        Exception
    ):  # this command not being found can raise quite a few different errors depending on the configuration
        device_requests = []

    client.containers.run(
        image_name,
        device_requests=device_requests,
        detach=True,
        name=container_name,
        volumes={f"{abs_path}": {"bind": "/home/engineering/data", "mode": "rw"}},
        tty=True,
        stdin_open=True,
    )
    model_name = model.lower()
    container = client.containers.get(f"rb-{model_name}")

    if container.status != "running":
        container.start()

    this_dir = os.path.dirname(os.path.abspath(__file__))

    with yaspin():
        subprocess.run(["chmod", "a+x", f"{this_dir}/models/{model}/train.sh"])
        # ctx.args is a list of arguments passed to the train command
        subprocess.run(["/bin/bash", f"{this_dir}/models/{model}/train.sh"] + ctx.args)


@main.command()
@click.argument("model")
@click.argument("prompt")
def infer(model, prompt):
    model_name = model.lower()
    container = client.containers.get(f"rb-{model_name}")

    if container.status != "running":
        container.start()

    this_dir = os.path.dirname(os.path.abspath(__file__))

    with yaspin():
        subprocess.run(["chmod", "a+x", f"{this_dir}/models/{model}/infer.sh"])
        # add a parameter for prompt
        subprocess.run(["/bin/bash", f"{this_dir}/models/{model}/infer.sh", f"'{prompt}'"])

        # move file from docker container to local directory
        # the file is located at /home/engineering/samples/output.jpg
        # the file is moved to the current directory
        subprocess.run(["docker", "cp", f"rb-{model_name}:/home/engineering/samples/output.jpg", "."])

    click.echo("Inference complete. Check the current directory for the output image.")


if __name__ == "__main__":
    main()
