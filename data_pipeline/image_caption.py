from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info

from tqdm import tqdm
import argparse


# default: Load the model on the available device(s)
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-7B-Instruct", torch_dtype="auto", device_map="cuda"
)
# processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")

min_pixels = 256*28*28
max_pixels = 1280*28*28
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct", min_pixels=min_pixels, max_pixels=max_pixels)


prompt = '''Please describe this image shortly, try to capture main details in the image. 
Here are some examples for image caption styles:

1. A Couple In A Public Display Of Affection
2. A kitten turning its head on a wooden floor
3. An Old Man Doing Exercises For The Body And Mind
4. Man Walking

Now please describe the given image briefly in one sentence, please do not say something like 'The image shows...' or 'The image depicts...'.
'''

animate_prompt = '''
I want to animate this image using an Image-Text-to-Video model. Your task is to generate a detailed and reasonable text prompt that describes how the image should be animated.

Guidelines:

1. Clarity & Realism - The animation description should be logical based on the given image, ensuring the movement makes sense for the scene.

2. Short & Vivid Description - Use expressive language to guide the animation model effectively, ensuring high-quality and visually engaging results.


Ensure that your animation prompt aligns with the content of the provided image and describes a visually compelling motion sequence.

Do not output animation prompts content contains object/scenes did not included in the given image.

Make sure the prompt is short in 1-2 sentences.
'''

import os
import json
import PIL


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', type=int, default=0)
    parser.add_argument('--N', type=int, default=6)
    parser.add_argument('--image_base', type=str, default='/nas-ssd2/shoubin/datasets/veggie/images/')
    parser.add_argument('--save_base', type=str, default='/nas-ssd2/shoubin/datasets/veggie/captions/')
    parser.add_argument('--mode', type=str, default='caption')
    
    args = parser.parse_args()
    data = os.listdir(args.image_base)
    base = args.image_base
    save_base = args.save_base

    if args.mode == 'caption':
        default_prompt = prompt
    elif args.mode == 'animation':
        default_prompt = animate_prompt
    else:
        raise ValueError('Invalid mode')
    
    result = {}
    
    m = len(data) // args.N
    if args.part == (args.N-1):
        part_data = data[args.part*m : ]
    else:
        part_data = data[args.part*m : (args.part+1)*m]
        
    count = 1
    
    for d in tqdm(part_data):
        
        try:
            size = PIL.Image.open(base + d).size
        except:
            count += 1
            print('missing image')
            continue
        
    
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "image": base + d,
                    },
                    {"type": "text", "text": default_prompt},
                    # {"type": "text", "text": animate_prompt},
                ],
            }
        ]
        # Preparation for inference
        text = processor.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        image_inputs, video_inputs = process_vision_info(messages)
        inputs = processor(
            text=[text],
            images=image_inputs,
            videos=video_inputs,
            padding=True,
            return_tensors="pt",
        )
        inputs = inputs.to("cuda")
        
        # Inference: Generation of the output
        generated_ids = model.generate(**inputs, max_new_tokens=128)
        generated_ids_trimmed = [
            out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
        ]
        output_text = processor.batch_decode(
            generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )
        
        print(output_text)
        result[d] = output_text

        
    with open(save_base + 'animation_{}.json'.format(str(args.part)), 'w') as f:
        f.write(json.dumps(result))
        
    print('skipped', count)