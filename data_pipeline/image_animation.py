import torch
from diffusers import CogVideoXImageToVideoPipeline
from diffusers.utils import export_to_video, load_image
import json
import PIL
import argparse
from tqdm import tqdm 
import os

# default: Load the model on the available device(s)
pipe = CogVideoXImageToVideoPipeline.from_pretrained(
    "THUDM/CogVideoX1.5-5B-I2V",
    torch_dtype=torch.bfloat16
).to('cuda')
# pipe.enable_sequential_cpu_offload()
pipe.vae.enable_tiling()
pipe.vae.enable_slicing()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int, default=0)
    parser.add_argument('--N', type=int, default=16)
    parser.add_argument('--prompt', type=str, default='/nas-ssd2/shoubin/datasets/veggie/animation_prompts.json')
    parser.add_argument('--image_base', type=str, default='/nas-ssd2/shoubin/datasets/veggie/images/')
    parser.add_argument('--save_base', type=str, default='/nas-ssd2/shoubin/datasets/veggie/animated_videos/')
    
    args = parser.parse_args()
    
    data = json.load(open(args.prompt)) # captions.json --> still
    
    keys = os.listdir(args.image_base)

    image_base = args.image_base
    save_base = args.save_base
    
    m = len(keys) // args.N
    if args.part == (args.N-1):
        part_keys = keys[args.part*m : ]
    else:
        part_keys = keys[args.part*m : (args.part+1)*m]
        
    count = 0
    
    for key in tqdm(part_keys):
        
        if os.path.exists(save_base + key.split('.')[0] + '.mp4'):
            print('continue')
            continue
        
        # try:
        prompt = data[key][0] + ' Make the image move and become a video.'
        image = load_image(image=image_base+key)
        video = pipe(
            prompt=prompt,
            image=image,
            num_videos_per_prompt=1,
            num_inference_steps=50,
            num_frames=81,
            height=480,
            width=720,
            guidance_scale=6,
            generator=torch.Generator(device="cuda"),
        ).frames[0]
        
        export_to_video(video, save_base + key.split('.')[0] + '.mp4', fps=8)
        
        
    print('skipped', count)
