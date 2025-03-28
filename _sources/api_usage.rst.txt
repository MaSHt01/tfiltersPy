API Reference
=============

Welcome to the **TFiltersPy** API Reference – where filtering gets fun! 🎉 Just like scikit‑learn, we've kept our API intuitive, so you can focus on crunching numbers and filtering noise without all the boring bits. 😎

Overview
--------
**TFiltersPy** is here to help you tame unruly data with a range of filtering algorithms. Whether you’re a wizard of linear systems 🧙‍♂️ or a champion of nonlinear chaos 🤹‍♀️, our filters are designed to be as straightforward (and fun) as possible.

Key Concepts:
- **fit()**: Initialize or train your filter – think of it as setting up your filtering magic ✨.
- **predict()**: Wave your wand and generate state estimates from new measurements 🪄.
- **run_filter()**: Process a sequence of measurements for a full filtering extravaganza 🎢.
- **estimate_parameters()**: Let the filter automatically figure out optimal settings (because who wants to do that manually? 🤷‍♂️).

Key Classes
-----------
- **BaseEstimator**  
  The foundation of our filtering magic. It handles parameter management, validation, and even some neat utility tricks like converting NumPy arrays to Dask arrays. 🔧

- **ParameterEstimator**  
  A bit more advanced – it adds methods for Bayesian parameter estimation using fun strategies like residual analysis, maximum likelihood, cross-validation, and adaptive filtering. 🎯

- **DaskKalmanFilter**  
  Our distributed wizard for linear state estimation, leveraging Dask to handle massive data sets with ease. It’s as efficient as it is elegant. 🚀

- **ParticleFilter**  
  For when your system is too wild for a Kalman filter, our Particle Filter uses a swarm of particles to track nonlinear, non-Gaussian systems. It’s like herding cats – but with probabilities! 🐱🎲




Detailed Documentation
----------------------
For the nitty-gritty details of each class and method, check out the module docs below:

.. automodule:: TFiltersPy.base_estimator
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: TFiltersPy.state_estimation.linear_filters
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: TFiltersPy.state_estimation.nonlinear_filters
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: TFiltersPy.state_estimation.particle_filters
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: TFiltersPy.utils.optimisation_utils
   :members:
   :undoc-members:
   :show-inheritance:

TFiltersPy Classes
=========

.. toctree::
   :maxdepth: 4

   TFiltersPy

Additional Notes
----------------
We designed **TFiltersPy** to be:
- **Simple & Intuitive:** No need to get bogged down in boilerplate—get filtering done with minimal fuss. 👍
- **Extensible:** Customize and extend the filters to suit your unique data adventures. 🔄
- **Distributed:** Built to work with Dask, so even your largest datasets can be tamed. 🌐


Indices and Tables
------------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
