# Autonomy Plan

## Perception
- Binary semantic segmentation: **sidewalk vs non‑sidewalk**
- Model: **Fast‑SCNN / ENet / BiSeNetV2** at 384×192 or 512×256
- Export: **TFLite INT8** or **ONNX**

## Post‑Processing
- Morphological clean → largest component near bottom
- Row‑wise centroid → polynomial centerline
- Chute planner: segment‑based allowed azimuth ranges

## Mapping
- Pre‑season clear‑ground mapping: mark **no‑throw** polygons and **dump zones**
- During storm: align via odom/IMU; optional VO/LiDAR later
