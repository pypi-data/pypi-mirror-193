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
    Evaluate a trained model.

    Example: rubbrband eval lora
    """
    pass


@app.command()
def dreambooth_stable_diffusion(
    ctx: typer.Context,
    input_prompt: str = typer.Option(..., help="The prompt to input into the trained model."),
):
    eval(ctx, "Dreambooth_Stable_Diffusion")


@app.command()
def lora(
    ctx: typer.Context,
    input_prompt: str = typer.Option(..., help="The prompt to input into the trained model."),
):
    eval(ctx, "LoRA")


@app.command()
def controlnet(
    ctx: typer.Context,
    input_prompt: str = typer.Option(..., help="The prompt to input into your finetuned model."),
):
    eval(ctx, "ControlNet")


def eval(ctx: typer.Context, model: str):
    model_name = model.lower()

    try:
        container = client.containers.get(f"rb-{model_name}")
    except docker.errors.NotFound:
        typer.echo(f"Container rb-{model_name} does not exist. Please train the model first.")
        return

    if container.status != "running":
        container.start()

    this_dir = os.path.dirname(os.path.abspath(__file__))

    # Convert the parameters to a list of strings
    params = []
    for key, value in ctx.params.items():
        params.append(f"--{key}")
        params.append(value)

    with yaspin():
        typer.echo(["/bin/bash", f"{this_dir}/models/{model}/infer.sh"] + params)
        subprocess.run(["chmod", "a+x", f"{this_dir}/models/{model}/infer.sh"])
        # add a parameter for prompt
        subprocess.run(["/bin/bash", f"{this_dir}/models/{model}/infer.sh"] + params)

        # move file from docker container to local directory
        # the file is located at /home/engineering/samples/output.jpg
        # the file is moved to the current directory
        subprocess.run(["docker", "cp", f"rb-{model_name}:/home/engineering/samples/output.jpg", "."])

    typer.echo("Inference complete. Check the current directory for the output image.")


if __name__ == "__main__":
    app()
