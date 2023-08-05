import concurrent.futures
from tqdm import tqdm
from brevettiai.io import AnyPath


def _download_file(source, callback):
    if type(source) == str:
        source = AnyPath(source)
    content = source.read_bytes()
    if callback is not None:
        return callback(source, content)
    else:
        return content


def load_files(paths, callback=None, monitor=True, tqdm_args=None, max_workers=16):
    """Download multiple files at once"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(_download_file, src, callback=callback) for src in paths]

        if monitor:
            futures = tqdm(futures, **(tqdm_args or {}))

        for f in futures:
            yield f.result()
