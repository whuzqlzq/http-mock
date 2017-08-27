import reader


def get_urls(rel_path):
    return reader.get_params(reader.get_files(rel_path), 'urls')
