# VEGGIE: Instructional Editing and Reasoning Video Concepts with Grounded Generation

This is automatic instructional video editing data generation pipeline proposed in VEGGIE paper.


## Step 0: Image Data Preparation
We start from instructional image editing data ([OmniEdit](https://arxiv.org/abs/2411.07199)), please refer to their page for data downloading.

## Step 1: Image Captioning + Animation Prompt Generation via VLM

We generate caption for each original instructional image data using VLM (Qwen2-VL-7B)

--part (which part is for running) and --N (split data into N splits) are for paralle running

```bash
CUDA_VISIBLE_DEVICES=0 python image_caption.py \
--part 0 \
--N 4 \
--base IMAGE_DATA_BASE_DIR \
--save_base SAVE_BASE_DIR \
--mode caption
```

We will also generate image animation prompt via VLM

```bash
CUDA_VISIBLE_DEVICES=0 python image_caption.py \
--part 0 \
--N 4 \
--image_base IMAGE_DATA_BASE_DIR \
--save_base SAVE_BASE_DIR \
--mode animation
```


## Step 2: Image Animation via I2V Model

We then animate orignal image into a short video via Image-to-Video model (CogVideoX1.5-5B-I2V)

```bash
CUDA_VISIBLE_DEVICES=0 python image_animation.py \
--part 0 \
--N 4 \
--prompt ANIMATION_PROMPT_FILE \
--image_base IMAGE_DATA_BASE_DIR \
--save_base SAVE_BASE_DIR 
```

## Step 3: 1st-Frame-Guided Video Editing

We then run inversion-based + frame-guided video editing method ([AnyV2V](https://arxiv.org/abs/2403.14468)) for paried, editied video generation.

Please refer to their page for environment setup.

```bash
cd AnyV2V/i2vgen-xl/

CUDA_VISIBLE_DEVICES=0 python run_edit.py \
--part 0 \
--N 4 \
--caption IMAGE_CAPTION_FILE \
--animated_video_base ANIMATED_VIDEO_BASE \
--image_base IMAGE_DATA_BASE_DIR \
--save_base SAVE_BASE_DIR 
```

## Step 4: Data Filtering via Automatic Evaluation

Finally we run automatic evaluation metrics (VBench) to give scores to each generated video and filter the data.

Please refer to [VBench Repo](https://github.com/Vchitect/VBench) for evaluation scripts.

We provide our filtering scripts after getting evaluation results, check [here](./vbench_filtering.ipynb).





