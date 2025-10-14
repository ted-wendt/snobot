# Vision Pipeline

## Dataset
- ~300 images of snow‑covered sidewalks
- Masks labeled as `sidewalk`

## Augmentations
- Brightness/contrast/gamma, light blur, noise
- Haze/fog, low‑contrast variants
- Small rotations, flips if context allows

## Training (PyTorch)
- Loss: BCEWithLogits + Dice (or Focal + Dice)
- Optim: AdamW, LR 3e‑4, 50–100 epochs
- Metric: IoU on sidewalk class

## Export
- PyTorch → ONNX → TFLite INT8 (post‑training quant)
