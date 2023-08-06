#!/bin/bash

# Parse command-line options
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -c|--class_name)
    class_name="$2"
    shift # past argument
    shift # past value
    ;;
    -r|--regulation_prompt)
    regulation_prompt="$2"
    shift # past argument
    shift # past value
    ;;
    -i|--inference_prompt)
    inference_prompt="$2"
    shift # past argument
    shift # past value
    ;;
    *)  # unknown option
    echo "Unknown option: $key"
    exit 1
    ;;
esac
done

# Check if mandatory options are present
if [[ -z "$class_name" || -z "$regulation_prompt" || -z "$inference_prompt" ]]; then
  echo "Missing mandatory option(s). Usage: $0 --class_name <class_name> --regulation_prompt <regulation_prompt> --inference_prompt <inference_prompt>" >&2
  exit 1
fi

# Your script code goes here



docker run --name rb-dreambooth-stable-diffusion -gpus all -it -d dreambooth:latest

docker exec -it rb-dreambooth-stable-diffusion /bin/bash

wget https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4-full-ema.ckpt

python scripts/stable_txt2img.py --ddim_eta 0.0 --n_samples 10 --n_iter 1 --scale 10.0 --ddim_steps 50  --ckpt sd-v1-4-full-ema.ckpt --prompt ${regulation_prompt}

python main.py --base configs/stable-diffusion/v1-finetune_unfrozen.yaml  -t  --actual_resume sd-v1-4-full-ema.ckpt   -n Fernie --gpus 1  --data_root imgs/ --reg_data_root imgs/  --class_word ${class_name} --no-test

python scripts/stable_txt2img.py --ddim_eta 0.0 --n_samples 8  --n_iter 1  --scale 10.0  --ddim_steps 100  --ckpt logs/imgs2023-02-17T21-48-16_Fernie/checkpoints/last.ckpt --prompt ${inference_prompt}
