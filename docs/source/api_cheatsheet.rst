API Reference
=============

Welcome to the **TFiltersPy** API Reference - where filtering becomes intuitive, scalable, and just a little bit fun 🎉.

Overview
--------
**TFiltersPy** helps you tame noisy signals and hidden states using Bayesian filtering. From the elegance of Kalman Filters to the chaotic beauty of Particle Filters, everything is built with Dask for distributed power.

🧠 Core Concepts:
-----------------
- **`fit()`** – Setup or train your filter. Think of this as telling your filter what kind of magic to perform. ✨  
- **`predict()`** – Perform state prediction on new data. Like fortune-telling, but backed by math. 🔮  
- **`run_filter()`** – Process an entire sequence of measurements and enjoy the full filtering ride. 🎢  
- **`estimate_parameters()`** – Let the filter estimate the best noise settings (Q and R) for you. No manual tuning necessary. 🛠️  

Key Classes
-----------
- **`BaseEstimator`**  
  The foundation of all filters – includes array management, validation, and useful helper functions.

- **`ParameterEstimator`**  
  Adds noise estimation techniques like:
  - Residual Analysis
  - Maximum Likelihood Estimation (MLE)
  - Cross-Validation
  - Adaptive Filtering

- **`DaskKalmanFilter`**  
  A linear-Gaussian filter with full support for Dask arrays – great for streaming or large-scale state estimation.

- **`DaskParticleFilter`**  
  A nonlinear, non-Gaussian Bayesian filter using particles and Dask-powered parallel inference.

- **`ExtendedKalmanFilter`** *(Coming soon)*  
  For systems where you can linearize around the current estimate.

- **`UnscentedKalmanFilter`** *(Planned)*  
  For better handling of nonlinear transformations without Jacobians.

Modules
-------
.. automodule:: TFiltersPy.base_estimator
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

.. automodule:: TFiltersPy.state_estimation.linear_filters
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

.. automodule:: TFiltersPy.state_estimation.nonlinear_filters
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

.. automodule:: TFiltersPy.state_estimation.particle_filters
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

.. automodule:: TFiltersPy.utils.optimisation_utils
   :members:
   :undoc-members:
   :show-inheritance:
   :inherited-members:

Developer Notes
---------------
🛠 **TFiltersPy** is:
- **Modular** – Easy to extend and override.
- **Dask-native** – Use for big data, sensor networks, or streaming applications.
- **Batteries-included** – With noise estimation and future plans for MCMC integration, UKF, and hybrid filtering.

Indices and Tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
