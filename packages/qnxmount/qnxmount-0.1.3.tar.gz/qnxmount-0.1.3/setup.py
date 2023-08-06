# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qnxmount', 'qnxmount.efs', 'qnxmount.etfs', 'qnxmount.qnx6']

package_data = \
{'': ['*']}

install_requires = \
['crcmod>=1.7,<2.0', 'fusepy>=3.0.1,<4.0.0', 'kaitaistruct>=0.10,<0.11']

setup_kwargs = {
    'name': 'qnxmount',
    'version': '0.1.3',
    'description': 'read only mounters for qnx filesystems',
    'long_description': '# QNX Filesystems Mounter\n\n## Project Discription\n\nThis project contains code to parse and mount (read only) QNX filesystems in non-standard images (HDD / SSD / eMMC).\n\nExisting tools were not able to handle the exotic configurations of some of the filesystems that we encountered in vehicle forensics, for instance on blocksizes greater than 4K on qnx6 filesystems, or non-standard allignment on qnx efs filesystems.\n\nThe description of the binary data structure of these filesystems is done with [kaitai](https://kaitai.io/) and this description can be found in the `.ksy` files in the folders for each respective qnx filesystem ([qnx6](qnxmount/qnx6/parser.ksy), [etfs](qnxmount/etfs/parser.ksy), and [efs](qnxmount/efs/parser.ksy)). With Kaitai, a Python based parser was generated. Mounting with these parsers is based on fuse.\n\nThis project is only tested on Linux machines. \n\n\n## Getting started\n\nSet up your Python virtual environment and activate the environment:\n```commandline\npython3 -m venv venv\nsource ./venv/bin/activate\n```\nInstall qnxmount and fuse in the virtual environment:\n```commandline\npip install qnxmount\nsudo apt install fuse\n```\n\n<!-- Or clone this repo and install.\n```commandline\npip install .\n``` -->\n\n\n## Usage\n\nGeneral use of the module is as follows:\n```shell\npython3 -m qnxmount {fs_type} [options] /image /mountpoint\n```\nwhere `fs_type` is the filesystem type (qnx6, etfs, or efs) and options are the options for that filesystem type.\n\nThe options are different for each filesystem type. An overview is given below. For more information use the help option. \n```shell\npython3 -m qnxmount qnx6 [-o OFFSET] /image /mountpoint\npython3 -m qnxmount etfs [-o OFFSET] [-s PAGE_SIZE] /image /mountpoint\npython3 -m efs /image /mountpoint\n```\n\nNote that the offset and page size can be entered in decimal, octal, binary, or hexadecimal format. For example, we can mount an image with a qnx6 filesystem at offset 0x1000 with:\n```shell\npython3 -m qnxmount qnx6 -o 0x1000 /image /mountpoint \n```\nUsing the option `-o 4096` would give the same result.\n\nIf mounting succeeds you will see the log message `"Mounting image /image on mount point /mountpoint"` appear and the process will hang. Navigate to the given mount point with another terminal session or a file browser to access the file system.\n\nUnmounting can be done from the terminal with:\n```shell\nsudo umount /mountpoint\n```\nThe logs will show show that the image was successfully unmounted and qnxmount will exit.\n\n## Contributing and Testing\n\nIf you want develop the tool and run tests, first fork the repository. Contributions can be submitted as a merge request. \n\nTo get started clone the forked repository and create a virtual environment. Install the test dependencies and fuse into the environment.\n```commandline\npip install .[test]\nsudo apt install fuse\n```\n\nThe folder **tests** contains functional tests to test the different parsers.\nTo run these tests you need a file system image and an accompanying tar archive.\nThe tests run are functional tests that check whether the parsed data from the test image is equal to the data stored in the archive.\nDefault test_images are located in the folders **test_data**.\nIf you want to test your own image replace the files **test_image.bin** and **test_image.tar.gz** with your own.\n\nA test image can be created by running the script `make_test_fs.sh` inside a QNX Virtual Machine.\nUpdate the script with the (edge) cases you want to check and run the command below.\nThis should create an _image.bin_ and _image.tar.gz_ into the specified directory.\nThese can be used as test files.\n```shell\nmake_test_fs.sh /path/to/output/directory\n```\n\nTo run the tests in this repo navigate to the main directory of the repo and run:\n```shell\npytest\n```\n\n[//]: # (Usually, tests can be run by directly calling `pytest tests --image ... --tar ...`, however this method fails here.)\n[//]: # (The reason is that the tests are located in a separate subfolder from the **qnx6_file_system.py**. )\n[//]: # (The qnx6_file_system module cannot be imported because it is not located in the tests directory.)\n[//]: # (When python3 is called it adds \'.\' to the PATH and since the qnx6_file_system module is located in the working directory they can be found.)\n',
    'author': 'Francis Hoogendijk',
    'author_email': 'f.hoogendijk@nfi.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NetherlandsForensicInstitute/qnxmount',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
