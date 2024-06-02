import pytest

from flood_fill.main import SeedPoint, check_point_in_image


# test check point in image

test_seed_points = [
     (SeedPoint(0,1), (3,3), True),
     (SeedPoint(2,2), (3,3), True),
     (SeedPoint(2,3), (3,3), False)
]


@pytest.mark.parametrize("point, shape, expected", test_seed_points)
def test_check_point_in_image(point, shape, expected):
        assert check_point_in_image(point, shape) == expected


if __name__ == "__main__":
    test_check_point_in_image(test_seed_points)