import subprocess

import docker
import eval
import train
import typer
from yaspin import yaspin

__author__ = "Rubbrband"

app = typer.Typer(no_args_is_help=True)
app.add_typer(train.app, name="train")
app.add_typer(eval.app, name="eval")

try:
    client = docker.from_env()
except docker.errors.DockerException:
    typer.echo("Docker is not running. Please start Docker and try again.")
    exit()


# create our database of models

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

# Pass singleton objects to our subcommands
train.client = client
eval.client = client
train.db = db
eval.db = db


@app.callback()
def main():
    """
    Rubbrband - A CLI for launching ML models.

    The Rubbrband CLI launches a model with all the installed dependencies for a given GitHub repository.

    The user can interact directly with the launched model using a Jupyter Notebook at http://localhost:8888.
    """
    pass


@app.command()
def models():
    """List all supported models"""
    typer.echo("Supported Models:")
    typer.echo(f"{'NAME':12} DESCRIPTION")
    for key, val in db.items():
        typer.echo(f"{key:12} {val['description']}")


@app.command()
def ls():
    """List all running ML models"""
    typer.echo("Running Models:")
    containers = client.containers.list()

    # filter containers that start with rb-
    for container in containers:
        if container.name.startswith("rb-"):
            typer.echo(container.name)


@app.command()
def launch(model: str):
    """
    Launch a new MODEL.

    MODEL is the name of the model to launch.

    Example: rubbrband launch LoRA
    """

    if model not in db:
        typer.echo("Model not found")
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


@app.command()
def enter(model: str):
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


if __name__ == "__main__":
    app()
