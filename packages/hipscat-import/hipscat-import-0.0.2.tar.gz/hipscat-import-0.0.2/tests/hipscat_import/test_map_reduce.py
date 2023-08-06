"""Tests of map reduce operations"""

import os
import tempfile

import file_testing as ft
import hipscat.pixel_math as hist
import numpy.testing as npt
import pyarrow as pa
import pytest

import hipscat_import.map_reduce as mr
from hipscat_import.file_readers import get_file_reader


def test_read_empty_filename():
    """Empty file name"""
    with pytest.raises(FileNotFoundError):
        mr.map_to_pixels(
            input_file="",
            file_reader=get_file_reader("parquet"),
            shard_suffix=0,
            highest_order=10,
            ra_column="ra",
            dec_column="dec",
        )


def test_read_wrong_fileformat(small_sky_file0):
    """CSV file attempting to be read as parquet"""
    with pytest.raises(pa.lib.ArrowInvalid):
        mr.map_to_pixels(
            input_file=small_sky_file0,
            file_reader=get_file_reader("parquet"),
            highest_order=0,
            ra_column="ra_mean",
            dec_column="dec_mean",
            shard_suffix=0,
        )


def test_read_directory(test_data_dir):
    """Provide directory, not file"""
    with pytest.raises(FileNotFoundError):
        mr.map_to_pixels(
            input_file=test_data_dir,
            file_reader=get_file_reader("parquet"),
            shard_suffix=0,
            highest_order=0,
            ra_column="ra",
            dec_column="dec",
        )


def test_read_bad_fileformat(blank_data_file):
    """Unsupported file format"""
    with pytest.raises(NotImplementedError):
        mr.map_to_pixels(
            input_file=blank_data_file,
            file_reader=None,
            shard_suffix=0,
            highest_order=0,
            ra_column="ra",
            dec_column="dec",
        )


def test_read_single_fits(formats_fits):
    """Success case - fits file that exists being read as fits"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        result = mr.map_to_pixels(
            input_file=formats_fits,
            file_reader=get_file_reader("fits"),
            highest_order=0,
            shard_suffix=0,
            cache_path=tmp_dir,
            ra_column="ra",
            dec_column="dec",
        )
        assert len(result) == 12
        expected = hist.empty_histogram(0)
        expected[11] = 131
        npt.assert_array_equal(result, expected)


def test_map_headers_wrong(formats_headers_csv):
    """Test loading the a file with non-default headers (without specifying right headers)"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        with pytest.raises(ValueError):
            mr.map_to_pixels(
                input_file=formats_headers_csv,
                file_reader=get_file_reader("csv"),
                shard_suffix=0,
                cache_path=tmp_dir,
                highest_order=0,
                ra_column="ra",
                dec_column="dec",
            )


def test_map_headers(formats_headers_csv):
    """Test loading the a file with non-default headers"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        result = mr.map_to_pixels(
            input_file=formats_headers_csv,
            file_reader=get_file_reader("csv"),
            highest_order=0,
            ra_column="ra_mean",
            dec_column="dec_mean",
            shard_suffix=0,
            cache_path=tmp_dir,
        )

        assert len(result) == 12

        expected = hist.empty_histogram(0)
        expected[11] = 8
        npt.assert_array_equal(result, expected)
        assert (result == expected).all()

        file_name = os.path.join(tmp_dir, "pixel_11", "shard_0_0.parquet")
        expected_ids = [*range(700, 708)]
        ft.assert_parquet_file_ids(file_name, "object_id", expected_ids)

        file_name = os.path.join(tmp_dir, "pixel_1", "shard_0_0.parquet")
        assert not os.path.exists(file_name)


def test_map_small_sky_order0(small_sky_single_file):
    """Test loading the small sky catalog and partitioning each object into the same large bucket"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        result = mr.map_to_pixels(
            input_file=small_sky_single_file,
            file_reader=get_file_reader("csv"),
            highest_order=0,
            ra_column="ra",
            dec_column="dec",
            shard_suffix=0,
            cache_path=tmp_dir,
        )

        assert len(result) == 12

        expected = hist.empty_histogram(0)
        expected[11] = 131
        npt.assert_array_equal(result, expected)
        assert (result == expected).all()

        file_name = os.path.join(tmp_dir, "pixel_11", "shard_0_0.parquet")
        expected_ids = [*range(700, 831)]
        ft.assert_parquet_file_ids(file_name, "id", expected_ids)


def test_map_small_sky_part_order1(small_sky_file0):
    """
    Test loading a small portion of the small sky catalog and
    partitioning objects into four smaller buckets
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        result = mr.map_to_pixels(
            input_file=small_sky_file0,
            file_reader=get_file_reader("csv"),
            highest_order=1,
            ra_column="ra",
            dec_column="dec",
            shard_suffix=0,
            cache_path=tmp_dir,
        )

        assert len(result) == 48

        expected = hist.empty_histogram(1)
        filled_pixels = [5, 7, 11, 2]
        expected[44:] = filled_pixels[:]
        npt.assert_array_equal(result, expected)
        assert (result == expected).all()

        # Pixel 44 - contains 5 objects
        file_name = os.path.join(tmp_dir, "pixel_44", "shard_0_0.parquet")
        expected_ids = [703, 707, 716, 718, 723]
        ft.assert_parquet_file_ids(file_name, "id", expected_ids)

        # Pixel 45 - contains 7 objects
        file_name = os.path.join(tmp_dir, "pixel_45", "shard_0_0.parquet")
        expected_ids = [704, 705, 710, 719, 720, 722, 724]
        ft.assert_parquet_file_ids(file_name, "id", expected_ids)

        # Pixel 46 - contains 11 objects
        file_name = os.path.join(tmp_dir, "pixel_46", "shard_0_0.parquet")
        expected_ids = [700, 701, 706, 708, 709, 711, 712, 713, 714, 715, 717]
        ft.assert_parquet_file_ids(file_name, "id", expected_ids)

        # Pixel 47 - contains 2 objects
        file_name = os.path.join(tmp_dir, "pixel_47", "shard_0_0.parquet")
        expected_ids = [702, 721]
        ft.assert_parquet_file_ids(file_name, "id", expected_ids)


def test_reduce_order0(parquet_shards_dir):
    """Test reducing into one large pixel"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        mr.reduce_pixel_shards(
            cache_path=parquet_shards_dir,
            origin_pixel_numbers=[44, 45, 46, 47],
            destination_pixel_order=0,
            destination_pixel_number=11,
            destination_pixel_size=131,
            output_path=tmp_dir,
            id_column="id",
        )

        output_file = os.path.join(tmp_dir, "Norder0/Npix11", "catalog.parquet")

        expected_ids = [*range(700, 831)]
        ft.assert_parquet_file_ids(output_file, "id", expected_ids)


def test_reduce_bad_expectation(parquet_shards_dir):
    """Test reducing into one large pixel"""
    with tempfile.TemporaryDirectory() as tmp_dir:
        with pytest.raises(ValueError):
            mr.reduce_pixel_shards(
                cache_path=parquet_shards_dir,
                origin_pixel_numbers=[44, 45, 46, 47],
                destination_pixel_order=0,
                destination_pixel_number=11,
                destination_pixel_size=11,  ## should be 131
                output_path=tmp_dir,
                id_column="id",
            )
