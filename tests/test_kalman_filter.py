import numpy as np
import pytest
import dask.array as da

from tfilterspy.state_estimation.linear_filters import DaskKalmanFilter

from tfilterspy.state_estimation.particle_filters import DaskParticleFilter


def test_kalman_filter_initialization():
    # Create simple test parameters
    F = np.eye(2)
    H = np.eye(2)
    Q = np.eye(2)
    R = np.eye(2)
    x0 = np.zeros(2)
    P0 = np.eye(2)
    
    # Should initialize without error
    kf = DaskKalmanFilter(F, H, Q, R, x0, P0)
    assert kf.F.shape == (2, 2)

    # Test that a non-square F matrix raises an error
    with pytest.raises(ValueError):
        DaskKalmanFilter(np.array([[1, 0]]), H, Q, R, x0, P0)


def test_kalman_predict():
    # Test prediction functionality for Kalman Filter
    F = np.eye(2)
    H = np.eye(2)
    Q = np.eye(2) * 0.1
    R = np.eye(2) * 0.5
    x0 = np.zeros(2)
    P0 = np.eye(2)
    measurements = np.random.randn(100, 2)  # 100 time steps

    kf = DaskKalmanFilter(F, H, Q, R, x0, P0)
    kf.fit(measurements)
    state_estimates = kf.predict().compute()

    assert state_estimates.shape == (100, 2)


def test_particle_filter_initialization():
    # Define a simple 2D state model (position and velocity)
    F = np.array([[1, 1],
                  [0, 1]])
    H = np.array([[1, 0]])  # Only position is measured

    # Define noise covariances
    Q = np.eye(2) * 0.01
    R = np.eye(1) * 0.1

    initial_state = np.array([0, 1])


    # Initialize the particle filter; adjust expected behavior if needed
     # Create the particle filter instance with Dask enabled
    pf = DaskParticleFilter(F, H, Q, R, initial_state, num_particles=1000, use_dask=True, estimation_strategy="residual_analysis")
    assert pf.F.shape == (2, 2)

    # Test that an invalid F matrix raises an error
    with pytest.raises(ValueError):
        DaskParticleFilter(np.array([[1, 0]]), H, Q, R, initial_state, num_particles=1000, use_dask=True, estimation_strategy="residual_analysis")

def test_particle_filter_predict():
  # Define a simple 2D state model (position and velocity)
    F = np.array([[1, 1],
                  [0, 1]])
    H = np.array([[1, 0]])  # Only position is measured

    # Define noise covariances
    Q = np.eye(2) * 0.01
    R = np.eye(1) * 0.1

    initial_state = np.array([0, 1])

    measurements = np.random.randn(100, 2)  # 100 time steps

    pf = DaskParticleFilter(F,H, Q, R, initial_state, num_particles=1000, use_dask=True, estimation_strategy="residual_analysis")
    pf.run_filter(measurements)
    state_estimates = pf.predict().compute()

    assert state_estimates.shape == (100, 2)


# Optional: If you want to test Dask compatibility specifically,
# uncomment and adjust this test.
# def test_particle_filter_dask_compatibility():
#     F = np.eye(2)
#     H = np.eye(2)
#     Q = np.eye(2)
#     R = np.eye(2)
#     x0 = np.zeros(2)
#     P0 = np.eye(2)
#     # Create a Dask array for measurements with appropriate chunking.
#     measurements = da.random.random((100, 2), chunks=(50, 2))
#
#     pf = DaskParticleFilter(F, H, Q, R, x0, P0)
#     pf.fit(measurements)
#     state_estimates = pf.predict()
#
#     # Ensure that state_estimates is a Dask array and compute its shape.
#     assert isinstance(state_estimates, da.Array)
#     assert state_estimates.compute().shape == (100, 2)
