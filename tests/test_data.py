import pytest
import scivision


@pytest.fixture
def dataset():
    return scivision.load_dataset("./")


def test_parakeet_4V1W_1_particle_still(dataset):

    # Sim the images
    images = dataset.parakeet_4V1W_1_particle_still.read()

    assert len(images) == 1


def test_parakeet_4V1W_100_particles_tilt_series(dataset):
    
    if os.getenv("CI"):
        pytest.skip("Take's too long for github workflow")
        return

    # Sim the images
    images = dataset.parakeet_4V1W_100_particles_tilt_series.read()

    assert len(images) == 100
