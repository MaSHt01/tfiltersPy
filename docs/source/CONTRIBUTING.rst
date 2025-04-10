Contributing to TFilterPy
==========================

First off, thank you for considering contributing to **TFilterPy**! 🙌  
Your contributions help us build better, faster, and more meaningful filtering tools for the world.

We welcome all kinds of contributions:
- 🔧 Bug fixes
- 📚 Documentation improvements
- ✨ New features or filters
- 🧪 Unit tests and validation
- 💡 Suggestions and discussions

Getting Started
---------------

1. **Fork the repository**  
   Go to https://github.com/ubunye-ai-ecosystems/tfilterspy and click "Fork".

2. **Clone your fork**  
   .. code-block:: bash

       git clone https://github.com/your-username/tfilterspy.git
       cd tfilterspy

3. **Create a virtual environment**  
   .. code-block:: bash

       python -m venv venv
       source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. **Install dependencies**  
   .. code-block:: bash

       pip install -e .[dev]

   This installs the library along with development tools like `pytest`, `black`, `ruff`, and `sphinx`.

5. **Run the tests**  
   .. code-block:: bash

       pytest

Code Style
----------

We follow [PEP8](https://peps.python.org/pep-0008/).  
Before submitting, please run:

.. code-block:: bash

    black .
    ruff . --fix

This ensures your code is formatted and linted properly.

Branching Strategy
------------------

- `main`: Stable releases
- `dev`: Active development
- Feature branches: `feature/your-awesome-thing`
- Bugfix branches: `fix/some-bug-name`

Writing Documentation
---------------------

To build docs locally:

.. code-block:: bash

    cd docs
    make html
    open _build/html/index.html

Notebooks for examples should be placed in:  
`examples/notebooks/your_usecase_here.ipynb`

Pull Requests
-------------

1. Push your changes and open a pull request to `dev`.
2. Add a descriptive title and explain your motivation.
3. Link related issues, if any.

All PRs will go through:
- ✅ CI testing
- 🧪 Code review
- 📚 Docs build check

Need Help?
----------

Open an issue or join the discussion at  
https://github.com/ubunye-ai-ecosystems/tfilterspy/discussions

We’re all here to learn and build together. ❤️

License
-------

By contributing, you agree that your contributions will be licensed under the same license as this project (MIT, Apache 2.0, etc.).

