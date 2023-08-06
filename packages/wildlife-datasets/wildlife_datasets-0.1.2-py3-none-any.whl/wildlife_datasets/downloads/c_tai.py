import os
import argparse
import shutil
if __name__ == '__main__':
    import utils
else:
    from . import utils

def get_data(root):
    utils.print_start(root)
    with utils.data_directory(root):
        url = 'https://github.com/cvjena/chimpanzee_faces/archive/refs/heads/master.zip'
        archive = 'master.zip'
        utils.download_url(url, archive)
        utils.extract_archive(archive, delete=True)

        # Cleanup
        shutil.rmtree('chimpanzee_faces-master/datasets_cropped_chimpanzee_faces/data_CZoo')
    utils.print_finish(root)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=str, default='data',  help="Output folder")
    parser.add_argument("--name", type=str, default='CTai',  help="Dataset name")
    args = parser.parse_args()
    get_data(os.path.join(args.output, args.name))