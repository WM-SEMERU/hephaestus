# Hephaestus
> Using neural machine translation for buggy code repair


## Overview

Recent approaches to automatic code repair have seen the use of neural machine translation (NMT) models to translate buggy code into fixed code. These models are trained with the buggy and fixed abstracted code token sequences directly, as in [this paper](https://arxiv.org/pdf/1812.08693.pdf) by Tufano et al. Hephaestus aims to use similar models, but train them with [Edit Operations](/hephaestus/EditOperations.html) instead of the traditional approach mentioned above. Thus, we train the models with the "difference" between the buggy and fixed code.

Hephaestus provides a modular framework from which researchers can reproduce or extend this work.

## Installation

Hephaestus requires the following Python dependencies:

- OpenNMT-py (version == 2.0.1)

    ```
    pip install OpenNMT-py==2.0.1
    ```

    If the above command fails because dependencies were not able to be installed, then use:

    ```
    pip install OpenNMT-py==2.0.1 --no-deps
    ```

- PyTorch (version >= 1.6.0)

    ```
    pip install torch>=1.6.0+cu111
    ```

    If the above command fails, then install PyTorch from source as given by the PyTorch
    [website](https://pytorch.org/get-started/locally/):

    ```
    pip3 install torch==1.8.1+cu111 torchvision==0.9.1+cu111 torchaudio===0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
    ```

- Pandas

    ```
    pip install pandas
    ```

- Matplotlib

    ```
    pip install matplotlib
    ```

Once the dependencies have been installed, clone the repository with:

```
git clone https://github.com/WM-SEMERU/hephaestus.git
```

From there, feel free to run the Jupyter notebooks in the `nbs` directory to your heart's content!

This project was built using [nbdev](https://nbdev.fast.ai/). If you would like to modify the Hephaestus library for research purposes, then you must install nbdev according to the instructions in the link above.

## Documentation

Find our documentation [here](https://wm-semeru.github.io/hephaestus/).
