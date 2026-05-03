# Learn-It-All IsaacLab Quadruped

An Isaac Lab external project for a custom quadruped locomotion setup. This
repository extracts the quadruped-specific work from a local Isaac Lab workspace
into a cleaner structure that is easier to open-source, install, and reproduce.

## Highlights

- Keeps the project separate from the upstream Isaac Lab repository
- Packages custom quadruped USD assets inside the external project
- Registers custom Gym tasks for training and play
- Includes RSL-RL launch scripts and custom RSL-RL/SKRL configs
- Preserves a legacy task variant alongside the current mainline task
- 
- ## Demo Videos

Uploading 52df2518c9b6cf07706bcbec8fc3300e_raw.mp4…
https://github.com/user-attachments/assets/1b139a39-3bb8-4f09-8b10-c91d4368a620

## Prerequisites

Install Isaac Lab first by following the official setup guide:

- https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/index.html

Use the same Python environment that already has Isaac Lab installed.

## Install This Project

From the repository root:

```bash
python -m pip install -e source/learn_it_all_isaaclab_quadruped
```

## Registered Tasks

Current mainline task based on `dog2` / `my_dog_work`:

- `LearnItAll-DogM-Flat-v0`
- `LearnItAll-DogM-Flat-Play-v0`
- `LearnItAll-DogM-Rough-v0`
- `LearnItAll-DogM-Rough-Play-v0`
- `LearnItAll-DogM-Direct-v0`

Legacy task based on `dog1` / `my_dog`:

- `LearnItAll-DogMLegacy-Flat-v0`
- `LearnItAll-DogMLegacy-Flat-Play-v0`
- `LearnItAll-DogMLegacy-Rough-v0`
- `LearnItAll-DogMLegacy-Rough-Play-v0`

`LearnItAll-DogM-Direct-v0` is kept as a convenience alias for the current flat
task even though the implementation still uses Isaac Lab's manager-based RL
workflow internally.

## Training

```bash
python scripts/rsl_rl/train.py --task=LearnItAll-DogM-Direct-v0
python scripts/rsl_rl/train.py --task=LearnItAll-DogM-Rough-v0
```

## Play / Evaluation

```bash
python scripts/rsl_rl/play.py --task=LearnItAll-DogM-Direct-v0 --checkpoint /path/to/model.pt
python scripts/rsl_rl/play.py --task=LearnItAll-DogM-Flat-Play-v0 --checkpoint /path/to/model.pt
```

## Project Structure

```text
Learn-It-All-IsaacLab-Quadruped/
├── README.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── .gitignore
├── scripts/
│   └── rsl_rl/
│       ├── cli_args.py
│       ├── train.py
│       └── play.py
└── source/
    └── learn_it_all_isaaclab_quadruped/
        ├── config/
        │   └── extension.toml
        ├── setup.py
        └── learn_it_all_isaaclab_quadruped/
            ├── __init__.py
            ├── assets/
            │   └── robots/
            │       ├── my_dog.py
            │       └── data/
            │           ├── dog1/
            │           └── dog2/
            └── tasks/
                └── manager_based/
                    └── locomotion/
                        └── velocity/
                            ├── dog_m/
                            └── dog_m_legacy/
```

## License

This repository is released under the BSD-3-Clause license. Some files are
adapted from Isaac Lab examples and retain upstream BSD-3-Clause headers. See
`LICENSE` and `THIRD_PARTY_NOTICES.md` for details.

## Notes Before Publishing

- Review the asset provenance for `dog1` and `dog2` before pushing publicly
- Update the repository URL in `extension.toml`
- Add your demo media links and any benchmark results you want to show
