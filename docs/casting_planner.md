# Casting Planner (Snow Throw Direction)

## Inputs
- Segment ID (from route)
- Wind (optional)
- No‑throw polygons
- Bank height estimate (optional, later)

## Outputs
- Chute azimuth (deg) + deflector (%)
- Safety check: if no safe azimuth, pause and re‑approach

## State Sketch
- `APPROACH` → `CAST_ALLOWED?` → `SET_AZIMUTH` → `TRACK_SEGMENT` → loop
