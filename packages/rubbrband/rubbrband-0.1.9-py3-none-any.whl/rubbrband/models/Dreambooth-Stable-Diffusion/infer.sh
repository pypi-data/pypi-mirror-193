#!/bin/sh

# Parse command-line options
while [ $# -gt 0 ]
do
key="$1"

case $key in
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

if [ -z "$inference_prompt" ]; then
  echo "Missing mandatory option(s). Usage: $0 --inference_prompt <inference_prompt>" >&2
  echo "inference_prompt is the prompt that you want to pass to your finetuned model." >&2
  exit 1
fi

docker exec -it rb-dreambooth-stable-diffusion /bin/bash -c " \
python scripts/stable_txt2img.py --ddim_eta 0.0 --n_samples 8  --n_iter 1  --scale 10.0  --ddim_steps 100  --ckpt experiment_logs/*/checkpoints/last.ckpt --prompt \"${inference_prompt}\""
