import os
import subprocess

import docker
import typer
from yaspin import yaspin

db = {}
client = None
app = typer.Typer(no_args_is_help=True)


@app.callback()
def main():
    """
    Train a model.

    Example: rubbrband train lora
    """
    pass


@app.command()
def dreambooth_stable_diffusion(
    ctx: typer.Context,
    class_name: str = typer.Option(
        ..., help="The name that you want to give to the class of images that you'll want to generate"
    ),
    regulation_prompt: str = typer.Option(
        ..., help="The prompt to regulate the images. Try to describe the type of images you want to generate"
    ),
    dataset_dir: str = typer.Option(..., help="The full path that contains the images you want to finetune on"),
    log_dir: str = "experiment_logs",
):
    train(ctx, "Dreambooth_Stable_Diffusion")


@app.command()
def lora(
    ctx: typer.Context,
    dataset_dir: str = typer.Option(..., help="The full path that contains the images you want to finetune on"),
):
    train(ctx, "LoRA")


@app.command()
def controlnet(
    ctx: typer.Context,
    dataset_dir: str = typer.Option(..., help="The full path that contains the images you want to finetune on"),
):
    train(ctx, "ControlNet")


# '''name''' corresponds to the name column in db.csv
# the option '''-d''' or '''--dataset_dir''' is the path to the dataset directory
# this directory gets mounted to the container at /home/engineering/data
def train(ctx: typer.Context, model: str):
    """Entrypoint for training a model."""

    if model not in db:
        typer.echo("Model not found")
        return

    image_name = f"rubbrband/{model.lower()}"
    container_name = f"rb-{model.lower()}"
    if not client.images.get(image_name):
        client.images.pull(image_name)

    abs_path = os.path.abspath(ctx.params["dataset_dir"])

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

    # Convert the parameters to a list of strings
    params = []
    for key, value in ctx.params.items():
        params.append(f"--{key}")
        params.append(value)

    with yaspin():
        subprocess.run(["chmod", "a+x", f"{this_dir}/models/{model}/train.sh"])
        # ctx.args is a list of arguments passed to the train command
        subprocess.run(["/bin/bash", f"{this_dir}/models/{model}/train.sh"] + params)


if __name__ == "__main__":
    app()
