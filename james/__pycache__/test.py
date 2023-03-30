import zipfile
import os
from concurrent.futures import ThreadPoolExecutor

def unzip_chunk(zip_file, chunk_size, output_dir):
    """
    Unzips a chunk of a zip file to the specified output directory.
    """
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for name in zip_ref.namelist():
            if name.endswith('/'):
                continue
            dest_path = os.path.join(output_dir, name)
            with zip_ref.open(name) as src, open(dest_path, 'wb') as dest:
                dest.write(src.read())

def parallel_unzip(zip_file, chunk_size, output_dir, num_threads):
    """
    Unzips a large zip file in parallel by chunking it and using multiple threads.
    """
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        chunks = [file_list[i:i+chunk_size] for i in range(0, len(file_list), chunk_size)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i, chunk in enumerate(chunks):
            chunk_file = f"{zip_file}.chunk{i}"
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                with zipfile.ZipFile(chunk_file, 'w') as chunk_zip:
                    for name in chunk:
                        chunk_zip.writestr(name, zip_ref.read(name))
            executor.submit(unzip_chunk, chunk_file,
