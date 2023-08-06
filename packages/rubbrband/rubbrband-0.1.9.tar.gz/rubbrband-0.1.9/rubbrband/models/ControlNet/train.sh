curl -L https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.ckpt --output $(pwd)/v1-5-pruned.ckpt

docker run --name rb-control -gpus all -it -d -v $(pwd)/v1-5-pruned.ckpt:/home/engineering/ControlNet/models/v1-5-pruned.ckpt control:latest

docker exec -it rb-control bash

conda run control

python tool_add_control.py ./models/v1-5-pruned.ckpt ./models/control_sd15_ini.ckpt

python tutorial_train.py