"""Test the move utility."""

from copy import deepcopy
from pathlib import Path
from shutil import rmtree

from pytest import fixture

from chime_frb_api.utils import copy, move
from chime_frb_api.workflow import Work

TEST_WORK = Work(
    pipeline="test-move-util",
    plots=["move_test/some_plot.png"],
    products=["move_test/some_product.dat"],
    site="chime",
    creation=1676399549.2184331,
    id="4r4nd0mlyg3n3r4t3dstr1ngb33pb00p",
)


@fixture()
def directory():
    """Directory fixture."""
    directory = Path("move_test")
    directory.mkdir(exist_ok=True)
    (directory / "some_plot.png").touch()
    (directory / "some_product.dat").touch()
    yield directory
    rmtree(directory.as_posix())


def test_copy_work_products(directory):
    """Test for copy.work_products."""
    assert Path("move_test/some_product.dat").exists()
    assert Path("move_test/some_plot.png").exists()
    work = deepcopy(TEST_WORK)
    copy.work_products(work, test_mode=True)
    assert Path("move_test/some_product.dat").exists()
    assert Path("move_test/some_plot.png").exists()
    assert Path(
        "move_test/data/chime/baseband/processed/workflow/20230214/test-move-util/4r4nd0mlyg3n3r4t3dstr1ngb33pb00p/some_plot.png"  # noqa: E501
    ).exists()
    assert Path(
        "move_test/data/chime/baseband/processed/workflow/20230214/test-move-util/4r4nd0mlyg3n3r4t3dstr1ngb33pb00p/some_product.dat"  # noqa: E501
    ).exists()
    assert work.plots == [
        "move_test/data/chime/baseband/processed/workflow/20230214/test-move-util/4r4nd0mlyg3n3r4t3dstr1ngb33pb00p/some_plot.png"  # noqa: E501
    ]
    assert work.products == [
        "move_test/data/chime/baseband/processed/workflow/20230214/test-move-util/4r4nd0mlyg3n3r4t3dstr1ngb33pb00p/some_product.dat"  # noqa: E501
    ]


def test_move_work_products(directory):
    """Test for move.work_products."""
    assert Path("move_test/some_product.dat").exists()
    assert Path("move_test/some_plot.png").exists()
    work = deepcopy(TEST_WORK)
    move.work_products(work, test_mode=True)
    assert not Path("move_test/some_product.dat").exists()
    assert not Path("move_test/some_plot.png").exists()
    assert Path(
        "move_test/data/chime/baseband/processed/workflow/20230214/test-move-util/4r4nd0mlyg3n3r4t3dstr1ngb33pb00p/some_plot.png"  # noqa: E501
    ).exists()
    assert Path(
        "move_test/data/chime/baseband/processed/workflow/20230214/test-move-util/4r4nd0mlyg3n3r4t3dstr1ngb33pb00p/some_product.dat"  # noqa: E501
    ).exists()
    assert work.plots == [
        "move_test/data/chime/baseband/processed/workflow/20230214/test-move-util/4r4nd0mlyg3n3r4t3dstr1ngb33pb00p/some_plot.png"  # noqa: E501
    ]
    assert work.products == [
        "move_test/data/chime/baseband/processed/workflow/20230214/test-move-util/4r4nd0mlyg3n3r4t3dstr1ngb33pb00p/some_product.dat"  # noqa: E501
    ]
