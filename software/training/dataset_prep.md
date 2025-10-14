# Dataset Preparation
- Use CVAT/LabelMe to annotate sidewalks → binary masks.
- Split 70/15/15 train/val/test by scene (avoid leakage).
- Resize to 384×192 or 512×256; save RGB + mask pairs.
