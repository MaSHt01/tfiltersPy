Installation
============

Getting started with **TFiltersPy** is as easy as Pi 🥧!  
No complicated rituals or secret handshakes—just open your terminal and run:

.. code-block:: bash
    pip install tfilterspy
---

✅ That’s it! You're all set to start filtering out the noise and revealing the hidden states in your data.


Installing from Source
----------------------

Prefer to tinker under the hood or contribute to the project? Clone the repo and install it in **editable mode**:

.. code-block:: bash
    git clone https://github.com/ubunye-ai-ecosystems/tfilterspy.git
    cd tfilterspy
    pip install -e .
---

This lets you edit the code and immediately test your changes without needing to reinstall. Great for hacking, debugging, or extending the library!


Requirements
------------

TFiltersPy is built on top of:

- `Dask <https://www.dask.org/>`_ for parallel and scalable computation.
- `NumPy <https://numpy.org/>`_ and `SciPy <https://scipy.org/>`_ for linear algebra and probability.
- `Matplotlib` and `Seaborn` (optional) for visualizing filter outputs.

You can install optional dev dependencies like this:

.. code-block:: bash
    pip install -r requirements-dev.txt
---

🎉 Now let the magic of Bayesian filtering begin! Enjoy turning noisy chaos into smooth, interpretable insights with **TFiltersPy**.
