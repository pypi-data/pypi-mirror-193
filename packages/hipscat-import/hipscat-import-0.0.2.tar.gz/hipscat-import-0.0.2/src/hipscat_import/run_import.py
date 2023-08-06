"""Import a set of non-hipscat files using dask for parallelization"""

import hipscat.io.write_metadata as io
import numpy as np
from dask.distributed import Client, as_completed
from hipscat import pixel_math
from tqdm import tqdm

import hipscat_import.map_reduce as mr
from hipscat_import.arguments import ImportArguments


def _map_pixels(args, client):
    """Generate a raw histogram of object counts in each healpix pixel"""

    futures = []
    for i, file_path in enumerate(args.input_paths):
        futures.append(
            client.submit(
                mr.map_to_pixels,
                input_file=file_path,
                file_reader=args.file_reader,
                filter_function=args.filter_function,
                highest_order=args.highest_healpix_order,
                ra_column=args.ra_column,
                dec_column=args.dec_column,
                shard_suffix=i,
                cache_path=None if args.debug_stats_only else args.tmp_dir,
            )
        )

    raw_histogram = pixel_math.empty_histogram(args.highest_healpix_order)
    for _, result in tqdm(
        as_completed(futures, with_results=True),
        desc="Mapping  ",
        total=len(futures),
        disable=(not args.progress_bar),
    ):
        raw_histogram = np.add(raw_histogram, result)
    return raw_histogram


def _reduce_pixels(args, destination_pixel_map, client):
    """Loop over destination pixels and merge into parquet files"""

    futures = []
    for destination_pixel, source_pixels in destination_pixel_map.items():
        futures.append(
            client.submit(
                mr.reduce_pixel_shards,
                cache_path=args.tmp_dir,
                origin_pixel_numbers=source_pixels,
                destination_pixel_order=destination_pixel[0],
                destination_pixel_number=destination_pixel[1],
                destination_pixel_size=destination_pixel[2],
                output_path=args.catalog_path,
                id_column=args.id_column,
            )
        )
    for _ in tqdm(
        as_completed(futures),
        desc="Reducing ",
        total=len(futures),
        disable=(not args.progress_bar),
    ):
        pass


def _validate_args(args):
    if not args:
        raise ValueError("args is required and should be type ImportArguments")
    if not isinstance(args, ImportArguments):
        raise ValueError("args must be type ImportArguments")


def run(args):
    """Importer that creates a dask client from the arguments"""
    _validate_args(args)

    with Client(
        local_directory=args.dask_tmp,
        n_workers=args.dask_n_workers,
        threads_per_worker=args.dask_threads_per_worker,
    ) as client:
        run_with_client(args, client)


def run_with_client(args, client):
    """Importer, where the client context may out-live the runner"""
    _validate_args(args)
    raw_histogram = _map_pixels(args, client)

    step_progress = tqdm(total=2, desc="Binning  ", disable=not args.progress_bar)
    pixel_map = pixel_math.generate_alignment(
        raw_histogram, args.highest_healpix_order, args.pixel_threshold
    )
    step_progress.update(1)
    destination_pixel_map = pixel_math.generate_destination_pixel_map(
        raw_histogram, pixel_map
    )
    step_progress.update(1)
    step_progress.close()

    if not args.debug_stats_only:
        _reduce_pixels(args, destination_pixel_map, client)

    # All done - write out the metadata
    step_progress = tqdm(total=3, desc="Finishing", disable=not args.progress_bar)
    io.write_legacy_metadata(args, raw_histogram, pixel_map)
    step_progress.update(1)
    io.write_catalog_info(args, raw_histogram)
    step_progress.update(1)
    io.write_partition_info(args, destination_pixel_map)
    step_progress.update(1)
    step_progress.close()
