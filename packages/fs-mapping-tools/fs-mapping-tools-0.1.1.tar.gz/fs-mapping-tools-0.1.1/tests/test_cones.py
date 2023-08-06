"""Testing suites for the cones module.

Author:
    Paulo Sanchez (@erlete)
"""

import pytest
from bidimensional import Coordinate

from fs_mapping_tools import Cone, ConeArray


class TestCone:
    """Testing suite for the Cone class."""

    ZERO = Coordinate(0, 0)

    def test_instance(self) -> None:
        """Test class instantiation."""
        with pytest.raises(TypeError):
            # Incorrect `position` data type:
            Cone(1, "yellow")
            # Incorrect `type` data type:
            Cone(self.ZERO, ["yellow"])

        with pytest.raises(ValueError):
            # Incorrect `type` value:
            Cone(self.ZERO, "yellowish")

        # Valid `position` and `type` values:
        Cone(self.ZERO, "yellow")
        Cone(self.ZERO, "blue")
        Cone(self.ZERO, "orange")
        Cone(self.ZERO, "orange-big")

    def test_access(self) -> None:
        """Test class attributes."""
        c1 = Cone(self.ZERO, "yellow")
        c2 = Cone(self.ZERO, "blue")
        c3 = Cone(self.ZERO, "orange")
        c4 = Cone(self.ZERO, "orange-big")

        # Test `x` and `y` attributes:
        assert c1.x == c2.x == c3.x == c4.x == 0
        assert c1.y == c2.y == c3.y == c4.y == 0

        # Test `position` attribute:
        assert c1.position == c2.position == c3.position == c4.position \
            == self.ZERO

        # Test `type` attribute:
        assert c1.type == "yellow"
        assert c2.type == "blue"
        assert c3.type == "orange"
        assert c4.type == "orange-big"

    def test_properties(self) -> None:
        """Test class properties."""
        c = Cone(self.ZERO, "yellow")

        with pytest.raises(TypeError):
            c.position = 1
            c.position = "Coordinate(1, 2)"

        with pytest.raises(TypeError):
            c.type = 1
            c.type = ["yellow"]

        with pytest.raises(ValueError):
            c.type = "yellowish"
            c.type = "blueish"

    def test_eq(self) -> None:
        """Test class equality."""
        c1 = Cone(self.ZERO, "yellow")
        c2 = Cone(self.ZERO, "blue")
        c3 = Cone(self.ZERO, "orange")
        c4 = Cone(self.ZERO, "orange-big")

        assert c1 == c1
        assert c2 == c2
        assert c3 == c3
        assert c4 == c4

        with pytest.raises(TypeError):
            c1 == 1
            c1 == "str"
            c1 == [1, 2]
            c1 == [c1, c2]

    def test_ne(self) -> None:
        """Test class inequality."""
        c1 = Cone(self.ZERO, "yellow")
        c2 = Cone(self.ZERO, "blue")
        c3 = Cone(self.ZERO, "orange")
        c4 = Cone(self.ZERO, "orange-big")

        assert c1 != c2
        assert c1 != c3
        assert c1 != c4
        assert c2 != c3
        assert c2 != c4
        assert c3 != c4

        with pytest.raises(TypeError):
            c1 != 1
            c1 != "str"
            c1 != [1, 2]
            c1 != [c1, c2]

    def test_plot(self) -> None:
        """Test plot method."""
        c1 = Cone(self.ZERO, "yellow")
        c2 = Cone(self.ZERO, "blue")
        c3 = Cone(self.ZERO, "orange")
        c4 = Cone(self.ZERO, "orange-big")

        # Detail off:
        c1.plot(detail=False)
        c2.plot(detail=False)
        c3.plot(detail=False)
        c4.plot(detail=False)

        # Detail on:
        c1.plot(detail=True)
        c2.plot(detail=True)
        c3.plot(detail=True)
        c4.plot(detail=True)

    def test_repr(self) -> None:
        """Test raw representation method."""
        c1 = Cone(self.ZERO, "yellow")
        c2 = Cone(self.ZERO, "blue")
        c3 = Cone(self.ZERO, "orange")
        c4 = Cone(self.ZERO, "orange-big")

        assert repr(c1) == "Cone(0.0, 0.0, yellow)"
        assert repr(c2) == "Cone(0.0, 0.0, blue)"
        assert repr(c3) == "Cone(0.0, 0.0, orange)"
        assert repr(c4) == "Cone(0.0, 0.0, orange-big)"

    def test_str(self) -> None:
        """Test string representation method."""
        c1 = Cone(self.ZERO, "yellow")
        c2 = Cone(self.ZERO, "blue")
        c3 = Cone(self.ZERO, "orange")
        c4 = Cone(self.ZERO, "orange-big")

        assert str(c1) == "Cone(0.0, 0.0, yellow)"
        assert str(c2) == "Cone(0.0, 0.0, blue)"
        assert str(c3) == "Cone(0.0, 0.0, orange)"
        assert str(c4) == "Cone(0.0, 0.0, orange-big)"


class TestConeArray:
    """Testing suite for the ConeArray class."""

    ZERO = Coordinate(0, 0)
    C1 = Cone(Coordinate(0, 0), "yellow")
    C2 = Cone(Coordinate(0, 0), "blue")
    C3 = Cone(Coordinate(0, 0), "orange")
    C4 = Cone(Coordinate(0, 0), "orange-big")

    def test_instance(self) -> None:
        """Test class instantiation."""
        # Empty initialization:
        ConeArray()

        # Single initialization:
        ConeArray(self.C1)

        # Multiple initialization:
        ConeArray(self.C1, self.C1)

    def test_access(self) -> None:
        """Test class attributes."""
        ca1 = ConeArray(self.C1)
        ca2 = ConeArray(self.C2)
        ca3 = ConeArray(self.C3)
        ca4 = ConeArray(self.C4)

        # Test `cones` attribute:
        assert ca1.cones == [self.C1]
        assert ca2.cones == [self.C2]
        assert ca3.cones == [self.C3]
        assert ca4.cones == [self.C4]

        # Test `type` attribute:
        assert ca1.type == "yellow"
        assert ca2.type == "blue"
        assert ca3.type == "orange"
        assert ca4.type == "orange-big"

    def test_properties(self) -> None:
        """Test class properties."""
        ca = ConeArray(self.C1)

        # Test `cones` property:
        with pytest.raises(TypeError):
            ca.cones = 1
            ca.cones = "str"

        ca.cones = [self.C1]
        ca.cones = [self.C1, self.C1]
        ca.cones = (self.C1,)
        ca.cones = (self.C1, self.C1)
        ca.cones = {self.C1}
        ca.cones = {self.C1, self.C1}

        with pytest.raises(TypeError):
            ca.cones = [self.C1, 1]
            ca.cones = [1, "s"]

        with pytest.raises(ValueError):
            ca.cones = [self.C1, self.C2]
            ca.cones = [self.C1, self.C3]
            ca.cones = [self.C1, self.C4]

    def test_append(self) -> None:
        """Test appending method."""
        ca = ConeArray(self.C1)

        # Invalid `cone` data type:
        with pytest.raises(TypeError):
            ca.append(1)
            ca.append("str")
            ca.append([1, 2])
            ca.append([self.C1, self.C2])

        # Invalid `type` value:
        with pytest.raises(ValueError):
            ca.append(self.C2)
            ca.append(self.C3)
            ca.append(self.C4)

    def test_extend(self) -> None:
        """Test extending method."""
        ca = ConeArray(self.C1)

        # Invalid `cone` data type:
        with pytest.raises(TypeError):
            ca.extend(1)
            ca.extend("str")

        with pytest.raises(TypeError):
            ca.extend([1])
            ca.extend(["str"])
            ca.extend([1, 2])
            ca.extend(self.C1)

        # Invalid `type` value:
        with pytest.raises(ValueError):
            ca.extend([self.C2])
            ca.extend([self.C3])
            ca.extend([self.C4])

        with pytest.raises(ValueError):
            ca.extend([self.C1, self.C2])

        ca.extend([self.C1, self.C1])

    def test_eq(self) -> None:
        """Test class equality."""
        ca1 = ConeArray(self.C1)
        ca2 = ConeArray(self.C2)
        ca3 = ConeArray(self.C3)
        ca4 = ConeArray(self.C4)

        assert ca1 == ca1
        assert ca2 == ca2
        assert ca3 == ca3
        assert ca4 == ca4

        with pytest.raises(TypeError):
            ca1 == 1
            ca1 == "str"
            ca1 == [1, 2]
            ca1 == [ca1, ca2]

    def test_ne(self) -> None:
        """Test class inequality."""
        ca1 = ConeArray(self.C1)
        ca2 = ConeArray(self.C2)
        ca3 = ConeArray(self.C3)
        ca4 = ConeArray(self.C4)

        assert ca1 != ca2
        assert ca1 != ca3
        assert ca1 != ca4
        assert ca2 != ca3
        assert ca2 != ca4
        assert ca3 != ca4

        with pytest.raises(TypeError):
            ca1 != 1
            ca1 != "str"
            ca1 != [1, 2]
            ca1 != [ca1, ca2]

    def test_hash(self) -> None:
        """Test class hashing."""
        ca = ConeArray(self.C1)

        assert hash(ca) == hash((self.C1,))

        ca.append(self.C1)

        assert hash(ca) == hash((self.C1, self.C1))

    def test_get_item(self) -> None:
        """Test get item method."""
        ca = ConeArray(self.C1)

        assert ca[0] == ca[-1] == self.C1
        assert ca[0:][0] == ca[::][0] == self.C1

        with pytest.raises(TypeError):
            ca["1"]
            ca["key"]
            ca[1.0]
            ca[self.C1]

        with pytest.raises(IndexError):
            ca[1]

    def test_set_item(self) -> None:
        """Test set item method."""
        ca = ConeArray(self.C1)

        with pytest.raises(TypeError):
            ca["1"] = self.C1
            ca["key"] = self.C1
            ca[1.0] = self.C1
            ca[self.C1] = self.C1

        with pytest.raises(IndexError):
            ca[1] = self.C1

        with pytest.raises(TypeError):
            ca[0] = 1
            ca[0] = "str"
            ca[0] = [1, 2]
            ca[0] = [self.C1, self.C2]

        with pytest.raises(ValueError):
            ca[0] = self.C2
            ca[0] = self.C3
            ca[0] = self.C4

    def test_plot(self) -> None:
        """Test plot method."""
        # Detail off:
        ConeArray(self.C1).plot(detail=False)
        ConeArray(self.C2).plot(detail=False)
        ConeArray(self.C3).plot(detail=False)
        ConeArray(self.C4).plot(detail=False)

        # Detail on:
        ConeArray(self.C1).plot(detail=True)
        ConeArray(self.C2).plot(detail=True)
        ConeArray(self.C3).plot(detail=True)
        ConeArray(self.C4).plot(detail=True)

    def test_len(self) -> None:
        """Test length method."""
        ca1 = ConeArray(self.C1)
        ca2 = ConeArray(self.C2)
        ca3 = ConeArray(self.C3)
        ca4 = ConeArray(self.C4)

        assert len(ca1) == 1
        assert len(ca2) == 1
        assert len(ca3) == 1
        assert len(ca4) == 1

        ca1.append(self.C1)
        ca2.append(self.C2)
        ca3.append(self.C3)
        ca4.append(self.C4)

        assert len(ca1) == 2
        assert len(ca2) == 2
        assert len(ca3) == 2
        assert len(ca4) == 2

    def test_repr(self) -> None:
        """Test raw representation method."""
        ca1 = ConeArray(self.C1)
        ca2 = ConeArray(self.C2)
        ca3 = ConeArray(self.C3)
        ca4 = ConeArray(self.C4)

        assert repr(ca1) == "ConeArray(1 yellow cone)"
        assert repr(ca2) == "ConeArray(1 blue cone)"
        assert repr(ca3) == "ConeArray(1 orange cone)"
        assert repr(ca4) == "ConeArray(1 orange-big cone)"

        ca1.append(self.C1)
        ca2.append(self.C2)
        ca3.append(self.C3)
        ca4.append(self.C4)

        assert repr(ca1) == "ConeArray(2 yellow cones)"
        assert repr(ca2) == "ConeArray(2 blue cones)"
        assert repr(ca3) == "ConeArray(2 orange cones)"
        assert repr(ca4) == "ConeArray(2 orange-big cones)"

    def test_str(self) -> None:
        """Test string representation method."""
        ca1 = ConeArray(self.C1)
        ca2 = ConeArray(self.C2)
        ca3 = ConeArray(self.C3)
        ca4 = ConeArray(self.C4)

        assert str(ca1) == """ConeArray(
    Cone(0.0, 0.0, yellow)
)"""
        assert str(ca2) == """ConeArray(
    Cone(0.0, 0.0, blue)
)"""
        assert str(ca3) == """ConeArray(
    Cone(0.0, 0.0, orange)
)"""
        assert str(ca4) == """ConeArray(
    Cone(0.0, 0.0, orange-big)
)"""

        ca1.append(self.C1)
        ca2.append(self.C2)
        ca3.append(self.C3)
        ca4.append(self.C4)

        assert str(ca1) == """ConeArray(
    Cone(0.0, 0.0, yellow),
    Cone(0.0, 0.0, yellow)
)"""
        assert str(ca2) == """ConeArray(
    Cone(0.0, 0.0, blue),
    Cone(0.0, 0.0, blue)
)"""
        assert str(ca3) == """ConeArray(
    Cone(0.0, 0.0, orange),
    Cone(0.0, 0.0, orange)
)"""
        assert str(ca4) == """ConeArray(
    Cone(0.0, 0.0, orange-big),
    Cone(0.0, 0.0, orange-big)
)"""
