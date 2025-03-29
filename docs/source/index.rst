.. tfilters documentation master file, created by
   sphinx-quickstart on Sun Jan 12 00:32:16 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
.. image:: _static/tfilters-logo.jpeg
   :alt: tfilters logo
   :width: 500px
   :align: center


Welcome to tfilterspy documentation – where we say "Sawubona, Molo, Hallo, Dumela, Ndaa, Xewani, and a Dinstang in Sipitori style!" and filter data like true South African rockstars!
-----------------------------------------


TFiltersPy is your new favorite Python library for implementing state-of-the-art Bayesian filtering techniques like Kalman Filters and Particle Filters. 
Whether you're working on noisy linear systems, nonlinear dynamics, or want to sound cool at a party when you say "I coded my own Kalman Filter," this is the library for you!

Features
--------
- **Kalman Filtering:** Robust state estimation with uncertainty quantification.
- **Particle Filtering:** Non-linear and non-Gaussian filtering methods.
- **Distributed Computation:** Leveraging Dask for scalability.
- **Uncertainty Quantification:** Built-in methods for assessing estimation confidence [TODO]

Installation
============

Getting started with **tfilterspy** is as easy as Pi ! 🍰

No need for complicated rituals or secret handshakes—just open your terminal and run:

.. code-block:: bash

    pip install tfilterspy

That’s it! In a flash, you’re all set to start filtering out the noise from your data.

Prefer to tinker under the hood? If you’re feeling adventurous, clone the repo and install it in editable mode:

.. code-block:: bash

    git clone https://github.com/LeparaLaMapara/tfilterspy.git
    cd tfilterspy
    pip install -e .

Now, let the magic of Bayesian filtering begin! Enjoy the fun of transforming noisy data into clear insights with **tfilterspy**.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api_usage
   examples_index

Examples
--------
See the `examples <https://github.com/LeparaLaMapara/tfilterspy/tree/main/examples>`_ directory for real-world use cases and Jupyter notebooks.

Additional Resources
--------------------
- `API Reference <genindex.html>`_
- `Module Index <modulues.html>`_
- `Search <search.html>`_

