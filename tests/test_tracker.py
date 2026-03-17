import pytest
from edint_eyetracking import MPIrisArea

def test_tracker_initialization():
    tracker = MPIrisArea()
    assert tracker is not None
    assert tracker.calibrated is False
    assert tracker.avg_vector is None
