# Project Sno-bot
A modular, Raspberry-Pi–driven sidewalk snow-removal robot designed for Helena, MT conditions. This repo is organized for **clarity, reproducibility, and future contributions**.

## Highlights
- **Modular Toolhead Interface**: swap plow, brush, or blower without rewiring
- **Teleop → Autonomy Path**: same electronics, two software modes
- **Pi-first, lightweight ML**: semantic segmentation on-device; TFLite/ONNX
- **Safety-first**: E‑stop, contactor, current-based jam detection

## Repo Layout
```
project-sno-bot/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── architecture.md
│   ├── toolhead_interface.md
│   ├── autonomy_plan.md
│   ├── casting_planner.md
│   └── vision_pipeline.md
├── electronics/
│   ├── parts_list.md
│   ├── wiring.md
│   └── schematics/   (place PDFs/PNGs here)
├── firmware/
│   └── toolhead_mcu/
│       ├── README.md
│       └── examples/
│           ├── i2c_api_sketch.ino
│           ├── can_api_sketch.md
│           └── id_eeprom_schema.json
├── software/
│   ├── pi/
│   │   ├── toolhead_manager.py
│   │   ├── teleop_controller.py
│   │   ├── requirements.txt
│   │   └── examples/
│   │       └── demo_run.py
│   └── training/
│       ├── dataset_prep.md
│       ├── fastscnn_train_stub.py
│       └── export_to_tflite.md
└── mechanical/
    ├── mount_interface.md
    └── references.md
```

## Quick Start
1. **Clone** this repo and open `docs/architecture.md`.
2. **Electronics**: follow `electronics/parts_list.md` and `electronics/wiring.md`.
3. **Firmware**: flash `firmware/toolhead_mcu/examples/i2c_api_sketch.ino` to your toolhead MCU.
4. **Software (Pi)**: install `software/pi/requirements.txt` then run `examples/demo_run.py`.
5. **Vision**: see `docs/vision_pipeline.md` and `software/training/` for segmentation training.

## License
MIT — see `LICENSE`.
