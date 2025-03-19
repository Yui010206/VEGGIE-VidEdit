# VEGGIE: Instructional Editing and Reasoning Video Concepts with Grounded Generation

Official implementation of **VEGGIE**, a unified versatile video generative model that handles various tasks for both video concept grounding and editing according to user instructions. 

[Shoubin Yu*](https://yui010206.github.io/), [Difan Liu*](https://difanliu.github.io/), [Ziqiao Ma*](https://mars-tin.github.io/), 
[Yicong Hong](https://yiconghong.me/), [Yang Zhou](https://yzhou359.github.io), [Hao Tan](https://research.adobe.com/person/hao-tan/), [Joyce Chai](https://web.eecs.umich.edu/~chaijy/), [Mohit Bansal](https://www.cs.unc.edu/~mbansal/)

Adobe Research, University of Michigan, University of North Carolina at Chapel Hill

[![Project Website](https://img.shields.io/badge/Project-Website-blue)](https://veggie-gen.github.io/)  [![arXiv](https://img.shields.io/badge/arXiv-2503.14350-b31b1b.svg)](https://arxiv.org/abs/2503.14350)   [![HuggingFace](https://img.shields.io/badge/🤗-HuggingFace%20-cyan.svg)](https://huggingface.co/datasets/Shoubin/VEGGIE-Bench)

<br>
<img width="800" src="assets/teaser.png"/>
<br>

<br>
<img width="800" src="assets/method.png"/>
<br>


# Instructional Video Editing Examples


*: Non-Instructional methods utilize paired video captions for editing.

### Instruction: Make it on the beach.

| Input Video | VEGGIE | VidToMe* | TokenFlow* | Flatten* | InstructDiff | LGVI | InsV2V |
|-------------|--------|---------|------------|----------|--------------|------|--------|
| ![Input](assets/baselines/input/cat.gif) | ![VEGGIE](assets/baselines/veggie/Env.gif) | ![VidToMe](assets/baselines/vidtome/Env.gif) | ![TokenFlow](assets/baselines/tokenflow/Env.gif) | ![Flatten](assets/baselines/flatten/Env.gif) | ![InstructDiff](assets/baselines/instructdiff/Env.gif) | ![LGVI](assets/baselines/lgvi/Env.gif) | ![InsV2V](assets/baselines/insv2v/Env.gif) |

### Instruction: Please add a ball in the given video frames.

| Input Video | VEGGIE | VidToMe* | TokenFlow* | Flatten* | InstructDiff | LGVI | InsV2V |
|-------------|--------|---------|------------|----------|--------------|------|--------|
| ![Input](assets/baselines/input/dog.gif) | ![VEGGIE](assets/baselines/veggie/Addition.gif) | ![VidToMe](assets/baselines/vidtome/Addition.gif) | ![TokenFlow](assets/baselines/tokenflow/Addition.gif) | ![Flatten](assets/baselines/flatten/Addition.gif) | ![InstructDiff](assets/baselines/instructdiff/Addition.gif) | ![LGVI](assets/baselines/lgvi/Addition.gif) | ![InsV2V](assets/baselines/insv2v/Addition.gif) |

### Instruction: Make it Chinese ink style.

| Input Video | VEGGIE | VidToMe* | TokenFlow* | Flatten* | InstructDiff | LGVI | InsV2V |
|-------------|--------|---------|------------|----------|--------------|------|--------|
| ![Input](assets/baselines/input/boat.gif) | ![VEGGIE](assets/baselines/veggie/Style.gif) | ![VidToMe](assets/baselines/vidtome/Style.gif) | ![TokenFlow](assets/baselines/tokenflow/Style.gif) | ![Flatten](assets/baselines/flatten/Style.gif) | ![InstructDiff](assets/baselines/instructdiff/Style.gif) | ![LGVI](assets/baselines/lgvi/Style.gif) | ![InsV2V](assets/baselines/insv2v/Style.gif) |

### Instruction: Could you label the bear in these video frames with red color masks?

| Input Video | VEGGIE | VidToMe* | TokenFlow* | Flatten* | InstructDiff | LGVI | InsV2V |
|-------------|--------|---------|------------|----------|--------------|------|--------|
| ![Input](assets/baselines/input/bear.gif) | ![VEGGIE](assets/baselines/veggie/Grounding.gif) | ![VidToMe](assets/baselines/vidtome/Grounding.gif) | ![TokenFlow](assets/baselines/tokenflow/Grounding.gif) | ![Flatten](assets/baselines/flatten/Grounding.gif) | ![InstructDiff](assets/baselines/instructdiff/Grounding.gif) | ![LGVI](assets/baselines/lgvi/Grounding.gif) | ![InsV2V](assets/baselines/insv2v/Grounding.gif) |

### Instruction: Replace the cup with a bottle of flower.

| Input Video | VEGGIE | VidToMe* | TokenFlow* | Flatten* | InstructDiff | LGVI | InsV2V |
|-------------|--------|---------|------------|----------|--------------|------|--------|
| ![Input](assets/baselines/input/ktE5HT0mzPY.gif) | ![VEGGIE](assets/baselines/veggie/Swap.gif) | ![VidToMe](assets/baselines/vidtome/Swap.gif) | ![TokenFlow](assets/baselines/tokenflow/Swap.gif) | ![Flatten](assets/baselines/flatten/Swap.gif) | ![InstructDiff](assets/baselines/instructdiff/Swap.gif) | ![LGVI](assets/baselines/lgvi/Swap.gif) | ![InsV2V](assets/baselines/insv2v/Swap.gif) |

### Instruction: Please remove the man in black in given video frames.

| Input Video | VEGGIE | VidToMe* | TokenFlow* | Flatten* | InstructDiff | LGVI | InsV2V |
|-------------|--------|---------|------------|----------|--------------|------|--------|
| ![Input](assets/baselines/input/running.gif) | ![VEGGIE](assets/baselines/veggie/Removal.gif) | ![VidToMe](assets/baselines/vidtome/Removal.gif) | ![TokenFlow](assets/baselines/tokenflow/Removal.gif) | ![Flatten](assets/baselines/flatten/Removal.gif) | ![InstructDiff](assets/baselines/instructdiff/Removal.gif) | ![LGVI](assets/baselines/lgvi/Removal.gif) | ![InsV2V](assets/baselines/insv2v/Removal.gif) |

### Instruction: Make the swan white.

| Input Video | VEGGIE | VidToMe* | TokenFlow* | Flatten* | InstructDiff | LGVI | InsV2V |
|-------------|--------|---------|------------|----------|--------------|------|--------|
| ![Input](assets/baselines/input/blackswan.gif) | ![VEGGIE](assets/baselines/veggie/Color.gif) | ![VidToMe](assets/baselines/vidtome/Color.gif) | ![TokenFlow](assets/baselines/tokenflow/Color.gif) | ![Flatten](assets/baselines/flatten/Color.gif) | ![InstructDiff](assets/baselines/instructdiff/Color.gif) | ![LGVI](assets/baselines/lgvi/Color.gif) | ![InsV2V](assets/baselines/insv2v/Color.gif) |

### Instruction: What can be used for heating food? Highlight your answer with red masks.

| Input Video | VEGGIE | VidToMe* | TokenFlow* | Flatten* | InstructDiff | LGVI | InsV2V |
|-------------|--------|---------|------------|----------|--------------|------|--------|
| ![Input](assets/baselines/input/BBQ-plate.gif) | ![VEGGIE](assets/baselines/veggie/Reasoning.gif) | ![VidToMe](assets/baselines/R.png) | ![TokenFlow](assets/baselines/R.png) | ![Flatten](assets/baselines/R.png) | ![InstructDiff](assets/baselines/instructdiff/Reasoning.gif) | ![LGVI](assets/baselines/lgvi/Reasoning.gif) | ![InsV2V](assets/baselines/insv2v/Reasoning.gif) |



# Instructional Video Editing Examples


# Reference
Please cite our paper if you use our models in your works:

```bibtex
@article{yu2025veggie,
        title={VEGGIE: Instructional Editing and Reasoning Video Concepts with Grounded Generation}, 
        author={Shoubin Yu and Difan Liu and Ziqiao Ma and Yicong Hong and Yang Zhou and Hao Tan and Joyce Chai and Mohit Bansal},
        year={2025},
        journal={arXiv:2503.14350},
}
