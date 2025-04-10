API Reference
=============

Welcome to the **TFiltersPy** API Reference — where filtering becomes intuitive, scalable, and just a little bit fun 🎉.

Overview
**TFiltersPy** helps you tame noisy signals and hidden states using Bayesian filtering. From the elegance of Kalman Filters to the chaotic beauty of Particle Filters, everything is built with Dask for distributed power.

🧠 Core Concepts
- :py:meth:`fit()` – Setup or train your filter. Think of this as telling your filter what kind of magic to perform. ✨  
- :py:meth:`predict()` – Perform state prediction on new data. Like fortune-telling, but backed by math. 🔮  
- :py:meth:`run_filter()` – Process an entire sequence of measurements and enjoy the full filtering ride. 🎢  
- :py:meth:`estimate_parameters()` – Let the filter estimate the best noise settings (Q and R) for you. No manual tuning necessary. 🛠️  

Quick Cheatsheet

+-----------------------------+-------------------------------------------------------------+
| Method                      | Description                                                 |
+=============================+=============================================================+
| :py:meth:`fit()`            | Train the filter on input data.                            |
+-----------------------------+-------------------------------------------------------------+
| :py:meth:`predict()`        | Predict next state based on system dynamics.               |
+-----------------------------+-------------------------------------------------------------+
| :py:meth:`run_filter()`     | Run the full filtering process over a dataset.             |
+-----------------------------+-------------------------------------------------------------+
| :py:meth:`estimate_parameters()` | Estimate Q and R via residuals, MLE, cross-validation, etc. |
+-----------------------------+-------------------------------------------------------------+

Key Classes

- :py:class:`tfilterspy.base_estimator.BaseEstimator`  
  The foundation of all filters – includes array management, validation, and useful helper functions.

- :py:class:`tfilterspy.utils.optimisation_utils.ParameterEstimator`  
  Adds noise estimation techniques like:
  - Residual Analysis
  - Maximum Likelihood Estimation (MLE)
  - Cross-Validation
  - Adaptive Filtering

- :py:class:`tfilterspy.state_estimation.linear_filters.DaskKalmanFilter`  
  A linear-Gaussian filter with full support for Dask arrays – great for streaming or large-scale state estimation.

- :py:class:`tfilterspy.state_estimation.particle_filters.DaskParticleFilter`  
  A nonlinear, non-Gaussian Bayesian filter using particles and Dask-powered parallel inference.

- **ExtendedKalmanFilter** *(Coming soon)*  
  For systems where you can linearize around the current estimate.

- **UnscentedKalmanFilter** *(Planned)*  
  For better handling of nonlinear transformations without Jacobians.

Design Philosophy
We follow a `scikit-learn` inspired design with a unified and consistent API:

- Modular and extensible filters.
- Lazy computation with Dask for scalability.
- Easy integration into real-world pipelines and Jupyter Notebooks.

Developer Tip 💡
All filters inherit from `BaseEstimator` and optionally from `ParameterEstimator` if they support dynamic Q/R tuning.


To dive deeper into class-level documentation, check the full :doc:`modules` or explore the examples in :doc:`examples`.

