<p align="center">
  <img src="branding/logo/tfilters-logo.jpeg?" alt="tfilterspy logo"/>
</p>

# **TFiltersPy** 🌀

![PyPI Version](https://img.shields.io/pypi/v/tfilterspy?color=blue&label=PyPI&style=for-the-badge)
![Codecov](https://img.shields.io/codecov/c/github/ubunye-ai-ecosystems/tfilterspy?style=for-the-badge)
![Build](https://github.com/ubunye-ai-ecosystems/tfilterspy/actions/workflows/build_PYPIP.yml/badge.svg?style=for-the-badge)
![PyPI Downloads](https://img.shields.io/pypi/dm/tfilterspy?style=for-the-badge)
![Docs](https://img.shields.io/badge/docs-online-brightgreen?style=for-the-badge)
![Python Versions](https://img.shields.io/pypi/pyversions/tfilterspy?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/ubunye-ai-ecosystems/tfilterspy?style=for-the-badge&logo=github)
![License](https://img.shields.io/github/license/ubunye-ai-ecosystems/tfilterspy?color=green&style=for-the-badge)

✨ **TFiltersPy** is your new favorite Python library for implementing state-of-the-art Bayesian filtering techniques like Kalman Filters and Particle Filters. Whether you're working on noisy linear systems, nonlinear dynamics, or want to sound cool at a party when you say "I coded my own Kalman Filter," this is the library for you!

---

## **What’s Inside?** 📦

🎉 **TFiltersPy** offers:
- **Kalman Filters** 🧮 – A classic but still iconic tool for linear filtering and smoothing.
- **Particle Filters** 🎲 – Sampling-based estimators for nonlinear systems.
- **Nonlinear Filters** 🔀 – For when your system decides to be complicated.
- Extensible design for implementing more advanced filtering algorithms like Unscented Kalman Filters (UKF) and beyond.

---

## **Installation** 🚀

Getting started is as easy as pie (or Pi)! 🍰

```bash
pip install tfilterspy
```

Want to contribute or tinker with the code? Clone the repo and install the development dependencies:

```bash
git clone https://github.com/MaSHt01/tfilterspy.git
cd tfilterspy
pip install .[dev]
```
___________________________________________

## Usage 🛠️
Example 1: Using a Kalman Filter to tame noisy data 🤖

```python
from tfilterspy.state_estimation.linear_filters import DaskKalmanFilter
import numpy as np
import dask.array as da
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

# Load and split the digits dataset (limited to 50 samples as in your code)
digits = load_digits()
x = digits.data   # (50, 64)
y = digits.target # (50,)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Convert to Dask arrays (adjust chunks for smaller dataset)
x_train_dask = da.from_array(x_train, chunks=(10, 64))  # 40 samples, ~4 chunks
x_test_dask = da.from_array(x_test, chunks=(10, 64))    # 10 samples, ~1 chunk
y_train_dask = da.from_array(y_train, chunks=(10,))
y_test_dask = da.from_array(y_test, chunks=(10,))

# Add synthetic noise to the data
noise_level = 0.88  # Adjust this to control noise intensity
noisy_x_train_dask = x_train_dask + da.random.normal(0, noise_level, x_train_dask.shape, chunks=x_train_dask.chunks)
noisy_x_test_dask = x_test_dask + da.random.normal(0, noise_level, x_test_dask.shape, chunks=x_test_dask.chunks)

# Define Kalman Filter parameters
n_features = 64
n_observations = 64
F = np.eye(n_features)  # Static state transition
H = np.eye(n_observations)  # Direct observation
Q = np.eye(n_features) * 0.01  # Initial process noise
R = np.eye(n_observations) * 0.1  # Initial observation noise
x0 = np.zeros(n_features)  # Initial state
P0 = np.eye(n_features) * 1.0  # Initial covariance

# Initialize the DaskKalmanFilter
kf = DaskKalmanFilter(
    state_transition_matrix=F,
    observation_matrix=H,
    process_noise_cov=Q,
    observation_noise_cov=R,
    initial_state=x0,
    initial_covariance=P0,
    estimation_strategy="mle"
)

# Fit and estimate parameters on noisy training data
kf.fit(noisy_x_train_dask)
Q_est, R_est = kf.estimate_parameters(noisy_x_train_dask)
kf.Q, kf.R = Q_est, R_est  # Update with estimated parameters

# Denoise the data
train_states = kf.predict().compute()  # Denoised training states
kf.fit(noisy_x_test_dask)  # Refit on test data
test_states = kf.predict().compute()  # Denoised test states
```


_____________________
## Features 🌟

  - Dask Support for large-scale filtering with parallelism 🏎️
  - Modular structure for extensibility 🛠️
  - Lightweight and easy to use 👌
  - Designed for both linear and nonlinear systems 🔄

___________________________________
# Why TFiltersPy? 💡

Because Kalman deserves better branding! Instead of grappling with matrices and equations from scratch, use TFilterPy and focus on the fun part: tweaking models until they (hopefully) work. 🎉
______________________________


## Contributing 🤝

We welcome contributions of all types:

  - 🐛 Found a bug? Let us know in the Issues.
  - 🌟 Want to add a feature? Fork the repo, make your changes, and create a pull request.
  - 🧪 Testers needed! Write more test cases for improved coverage.

### Development Setup
  1. Clone the repo:
  ```bash
    git clone https://github.com/MaSHt01/tfilterspy.git
  ```
  2. Install dependencies:
  ```bash
    pip install .[dev]
  ```
  3. Run tests:
  ```bash
    pytest tests/
  ```

  
  _________________________
## Future Plans 🔮

  - Adding Unscented Kalman Filters (UKF) 🦄
  - Implementing Gaussian Process Filters 📈
  - Enhancing scalability with advanced parallelism ⚡

________________

## Documentation 📚

Detailed documentation is available at: https://ubunye-ai-ecosystems.github.io/uaie
(Yes, we made it look fancy. You're welcome. ✨)
_____________________

## Support ❤️

If this library made your life easier, consider:

    Giving it a ⭐ on GitHub.
    Telling your friends, colleagues, and cats about TFilterPy.
_________________________

## License 📜

This project is licensed under the MIT License. Feel free to use it, modify it, or use it as a coaster.

**Enjoy your filtering adventures with TFilterPy! 🎉🚀**
