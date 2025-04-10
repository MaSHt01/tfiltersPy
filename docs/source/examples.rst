Real World Use-Cases 🎢
=======================

Welcome to the Notebook Playground -  where your Jupyter notebooks come to life and show off their filtering magic! ✨  
This section showcases real-world applications of TFiltersPy in noisy, messy, dynamic environments where **Bayesian filtering** shines.

🚀 Whether you're smoothing topic probabilities, estimating hidden states, or tracking uncertainty across time — these notebooks will get you started.

📚 For a full list of our example notebooks, head over to our GitHub:

🔗 `Visit the Examples Directory <https://github.com/ubunye-ai-ecosystems/tfilterspy/tree/main/examples/notebooks>`_


Use-Case Templates
------------------

Each example notebook typically follows this structure:

1. **Data Loading** - Real or simulated data that represents a time-varying system.
2. **Preprocessing** - Cleaning, transformation, and feature extraction.
3. **Filter Setup** - Define system matrices (F, H), noise covariances (Q, R), and initial conditions.
4. **Fit & Predict** - Apply your filter across the dataset using `.fit()` and `.predict()` or `.run_filter()`.
5. **Visualization** - Plot raw vs filtered estimates.
6. **Interpretation** - Gain insights into dynamics, trends, and uncertainty.



---------------------------------
Topic Modeling + Kalman Filtering
---------------------------------

This notebook shows how to use TFiltersPy to smooth topic probabilities over time in a stream of disaster-related tweets. 
Smooth chaotic topic trends in disaster-related tweets to track evolving narratives over time.

path_to_disaster_tweets= r'C:\Users\thabanglukhetho\Documents\gits\tfilterPy\examples\data\train_nlp.csv'


.. code-block:: python

    import pandas as pd
    import numpy as np
    import dask.array as da
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.decomposition import LatentDirichletAllocation
    from  tfilterspy.state_estimation.particle_filters import DaskParticleFilter
    import matplotlib.pyplot as plt

1. Load Disaster Tweets

.. code-block:: python

    data_path = path_to_disaster_tweets  # Update after download
    df = pd.read_csv(data_path)
    tweets = df['text'].values  # ~7613 tweets
    print(f"Number of tweets: {len(tweets)}")

2. Preprocess and Extract Topics

.. code-block:: python

    vectorizer = CountVectorizer(max_features=5000, stop_words='english')
    X = vectorizer.fit_transform(tweets)
    n_topics = 5  # e.g., disaster, weather, casual, news, other
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=42)
    topic_dist = lda.fit_transform(X)  # Shape: (7613, 5)
    X_dask = da.from_array(topic_dist, chunks=(1000, n_topics))
    print(f"Topic distribution shape: {X_dask.shape}")

3. Kalman Filter Initiative

.. code-block:: python

    n_features = 14
    F = np.eye(n_features)  # Static transition (identity for simplicity)
    H = np.eye(n_features)  # Direct observation
    Q = np.eye(n_features) * 0.01  # Process noise
    R = np.eye(n_features) * 0.1   # Observation noise
    x0 = np.zeros(n_features)      # Initial state
    P0 = np.eye(n_features)        # Initial covariance
    kf = DaskKalmanFilter(F, H, Q, R, x0, P0, estimation_strategy="residual_analysis")

4. Fit and Predict

.. code-block:: python
    kf.fit(X_dask)
    smoothed_topics = kf.predict().compute()


5. Plot Raw vs Smoothed Topics (first 1000 tweets)

.. code-block:: python
    plt.figure(figsize=(12, 8))
    for i in range(n_topics):
        plt.subplot(n_topics, 1, i + 1)
        plt.plot(topic_dist[:1000, i], label=f"Raw Topic {i+1}", alpha=0.5)
        plt.plot(smoothed_topics[:1000, i], label=f"Smoothed Topic {i+1}", linestyle="--")
        plt.title(f"Topic {i+1}")
        plt.xlabel("Tweet Index (Time)")
        plt.ylabel("Probability")
        plt.legend()
    plt.tight_layout()
    plt.show()


6. Interpret Topics 

.. code-block:: python
    feature_names = vectorizer.get_feature_names_out()
    for i, topic in enumerate(lda.components_):
        top_words = [feature_names[j] for j in topic.argsort()[-5:]]
        print(f"Topic {i+1}: {', '.join(top_words)}")