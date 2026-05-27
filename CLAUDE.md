# Worlds — Exoplanet Generator

## What This Project Does

Generates random but scientifically plausible exoplanets as JSON metadata. Each run produces one planet, validates its properties against basic physics rules, prints it to the terminal, and saves it to `output/generated_exoplanet.json`. Also regenerates `README.md` on every run (intentional, not a bug).

## How to Run

```bash
# One-time setup
./venv_setup.sh

# Generate a planet
python __main__.py
```

Output goes to `output/generated_exoplanet.json`.

## Project Structure

```
worlds/
├── __main__.py              # Entry point — calls generate, validate, save
├── utils/
│   └── planet_generator.py  # All generation + validation logic
├── output/                  # Generated JSON files land here
├── requirements.txt
└── venv_setup.sh / venv_activate.sh
```

## Key Files

- [\_\_main\_\_.py](__main__.py) — orchestrates the run: generate → validate → print → save → write README
- [utils/planet_generator.py](utils/planet_generator.py) — contains `generate_exoplanet()` and three validators

## Core Logic

### Generation (`generate_exoplanet`)
Randomly samples each property independently within fixed ranges:

| Property | Range |
|---|---|
| Radius | 1.0–2.5 Earth radii |
| Mass | 1.0–10.0 Earth masses |
| Orbital distance | 0.1–1.0 AU |
| Insolation | 0.5–2.0 Earth |
| Temperature | 250–350 K |
| Pressure | 0.5–2.0 atm |
| Gravity | 0.8–2.5 g |
| Atmosphere | N₂ 60–80%, O₂ 15–30%, CO₂ 0.01–5%, CH₄ 0.01–2% |

### Validation (`validate_exoplanet`)
Runs three independent checks and returns `{"valid": bool, "issues": [...]}`:

1. **Gravity** — `mass / radius²` should be within ±0.2 g of the sampled gravity
2. **Atmosphere** — composition percentages must sum to 95–105%
3. **Temperature** — must be between 200–400 K

## Known Limitations / Physics Simplifications

- Properties are sampled independently — in reality, mass, radius, and gravity are correlated
- Orbital distance and insolation are unrelated (insolation should derive from distance + star luminosity)
- Gravity formula (`M/R²`) is a simplified approximation, not full surface gravity calculation
- Atmospheric composition percentages don't sum to 100% by construction — validation is permissive (±5%)

## Dependencies

`requirements.txt` lists ~45 packages including Streamlit, Matplotlib, Pandas, Altair, and Pydeck — most are **not currently used**. The active runtime only needs the Python standard library (`random`, `json`, `os`). The unused deps suggest a web visualization UI was planned but not built.

## Potential Expansion Areas

- Web UI using the already-included Streamlit/Altair/Pydeck dependencies
- Correlated property generation (e.g., derive gravity from mass + radius rather than sampling independently)
- Multi-planet systems, star types, moons, rings
- CLI flags to control output format or number of planets generated
- Batch generation and CSV/Parquet export (Pandas is already a dependency)
