 Mathematics Behind the Kalman Filter
====================================

Think of the Kalman Filter like a smart guesser 🤖.

At each step, it:
1. Predicts what will happen next.
2. Checks what *actually* happened (the measurement).
3. Adjusts its guess based on how wrong it was.

We do this using a bit of matrix magic — here's how it works:

Step 1: Predict (What do we *think* will happen?)

.. math::

    \hat{x}_{k|k-1} = F \cdot \hat{x}_{k-1|k-1}

    P_{k|k-1} = F \cdot P_{k-1|k-1} \cdot F^\top + Q

- :math:`\hat{x}_{k|k-1}` is our predicted state at time `k`.
- :math:`F` is the state transition matrix.
- :math:`P_{k|k-1}` is the predicted uncertainty (covariance).
- :math:`Q` is the process noise — how much we think the system can change randomly.

Step 2: Update (What did we *actually* see?)

.. math::

    y_k = z_k - H \cdot \hat{x}_{k|k-1}

    S_k = H \cdot P_{k|k-1} \cdot H^\top + R

    K_k = P_{k|k-1} \cdot H^\top \cdot S_k^{-1}

- :math:`y_k` is the "innovation" — the difference between what we saw (`z_k`) and what we predicted.
- :math:`H` maps our state to what we *can* observe.
- :math:`S_k` is the uncertainty in the measurement prediction.
- :math:`R` is the observation noise — how noisy our measurements are.
- :math:`K_k` is the Kalman Gain — it decides how much to trust the measurement vs the prediction.

Step 3: Correct (Update our guess based on new info)

.. math::

    \hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k \cdot y_k

    P_{k|k} = (I - K_k \cdot H) \cdot P_{k|k-1}

- We update our estimate of the state and its uncertainty.

Intuition:

- If the measurement is very noisy (big :math:`R`), we trust our prediction more.
- If the prediction is uncertain (big :math:`P`), we trust the measurement more.

This beautiful balance between **what we expect** and **what we observe** is what makes the Kalman Filter such a powerful tool for filtering out noise and estimating the hidden truth. ✨

understanding  Particle Filters
======================================

The Particle Filter is like a swarm of guesses (particles) trying to chase the truth. 🐝  
Each particle represents a hypothesis of where the system could be. As time moves on, we adjust how much we trust each guess based on what we observe.

It's filtering—but with friends.

Step 1: Initialization 🐣

Start with `N` particles, each one initialized at the same known state (or sampled if you want variation):

.. math::

    x_i^{(0)} = x_0, \quad w_i^{(0)} = \frac{1}{N}

Where:
- :math:`x_i^{(0)}` is the initial state of the *i*-th particle
- :math:`w_i^{(0)}` is its weight (uniform initially)

Step 2: Prediction 🔮

Let each particle evolve through the state transition model and some random noise:

.. math::

    x_i^{(k)} = f(x_i^{(k-1)}) + \epsilon_i^{(k)}

Where:
- :math:`f(x)` is the state transition function
- :math:`\epsilon_i^{(k)} \sim \mathcal{N}(0, Q)` is process noise

Step 3: Measurement Update 🔍

Compare each particle’s prediction to the actual observation:

.. math::

    w_i^{(k)} \propto w_i^{(k-1)} \cdot p(y^{(k)} \mid x_i^{(k)})

Typically, this likelihood is Gaussian:

.. math::

    p(y^{(k)} \mid x_i^{(k)}) = \mathcal{N}(y^{(k)} \mid h(x_i^{(k)}), R)

Where:
- :math:`h(x)` is the observation function
- :math:`R` is the observation noise covariance

Normalize weights so they sum to 1:

.. math::

    \sum_{i=1}^{N} w_i^{(k)} = 1

Step 4: Resampling ♻️

If most particles have near-zero weights, we resample to keep only good particles:

Draw `N` new particles **with replacement**, favoring high-weight ones.

.. math::

    x_i^{(k)} \sim \{ x_j^{(k)} \}_{j=1}^{N}, \quad \text{with probability } w_j^{(k)}

Step 5: Estimate State 🎯

The best guess of the state is just a weighted average of all particles:

.. math::

    \hat{x}^{(k)} = \sum_{i=1}^{N} w_i^{(k)} x_i^{(k)}

Bonus: Residuals

We can define the residual (aka innovation) at each step:

.. math::

    r^{(k)} = y^{(k)} - \hat{y}^{(k)}, \quad \text{where } \hat{y}^{(k)} = h(\hat{x}^{(k)})

Use these for parameter estimation or diagnostics!

Intuition:

- If your model is spot-on, particles stay tight and track the truth.
- If your model is wrong or noisy, particles spread out, but the filter still works by focusing on better guesses.

That's it — just a clever crowd of guesses refining themselves with every new clue! 🧠🎲

Parameter Estimation Methods
============================

When you're not sure how much noise is in your system (Q and R), these methods help your filter figure it out.

Let’s break down each method simply:

Notation:
- :math:`Q`: Process noise covariance (uncertainty in the system’s evolution).
- :math:`R`: Observation noise covariance (uncertainty in what we observe).
- :math:`y_t`: Observation at time t.
- :math:`\hat{y}_t`: Predicted observation at time t from filter.
- :math:`r_t = y_t - \hat{y}_t`: The *residual* or *innovation*.

1. Residual Analysis 📊

This method says: "Let’s look at the errors and calculate how wild they are."

We assume the residuals are due to noise. So we use their **variance** and **covariance** to estimate Q and R:

.. math::

    R \approx \mathrm{Var}(r_t) = \frac{1}{T} \sum_{t=1}^{T} r_t r_t^\top

    Q \approx \mathrm{Cov}(r_t) = \frac{1}{T} \sum_{t=1}^{T} (r_t - \bar{r})(r_t - \bar{r})^\top

Where :math:`\bar{r}` is the mean of the residuals.

2. Maximum Likelihood Estimation (MLE) 🔍

MLE says: “Let’s find the Q and R that *most likely* made our observations happen.”

We do it iteratively:
- Run the filter
- Get residuals
- Update Q and R to maximize the likelihood

Simplified:

.. math::

    Q^{(i+1)} = \mathrm{Var}(r_t^{(i)})

    R^{(i+1)} = \mathrm{Var}(r_t^{(i)})

Where :math:`i` is the iteration index. We stop after a few rounds or when it converges.

3. Cross-Validation (CV) 🔁

Let’s split the data into parts (folds), train the filter on some, and validate on the rest.

For each fold:

.. math::

    \text{Train on } X_{\text{train}}, \quad \text{Validate on } X_{\text{val}}

    Q_{\text{fold}} = \mathrm{Cov}(r_t^{\text{train}}), \quad
    R_{\text{fold}} = \mathrm{Var}(r_t^{\text{train}})

Then we compute the **validation score**:

.. math::

    \text{Score}_{\text{fold}} = \frac{1}{N} \sum_{t \in \text{val}} \left\| y_t - \hat{y}_t \right\|^2

We pick the Q and R from the fold with the **lowest score**.

4. Adaptive Filtering (Online Updating) 🔄


This method says: “Let’s keep updating Q and R as we go using a small learning rate.”

Every new innovation :math:`r_t` gives us new evidence to tweak Q and R:

.. math::

    Q_t = (1 - \alpha) Q_{t-1} + \alpha (r_t r_t^\top)

    R_t = (1 - \alpha) R_{t-1} + \alpha \cdot \mathrm{diag}(r_t r_t^\top)

Where:
- :math:`\alpha` is the learning rate (e.g. 0.01)
- :math:`r_t` is the innovation (residual)

The filter gets smarter over time, adjusting itself like a thermostat reacting to room temperature. 🌡️


These techniques are all about helping the filter "learn" how noisy the world is — so it can be confident when it needs to be, and skeptical when things look fishy. 🐠
