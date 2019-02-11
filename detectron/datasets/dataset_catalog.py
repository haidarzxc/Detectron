# Copyright (c) 2017-present, Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

"""Collection of available datasets."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


# Path to data dir
_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

# Required dataset entry keys
_IM_DIR = 'image_directory'
_ANN_FN = 'annotation_file'

# Optional dataset entry keys
_IM_PREFIX = 'image_prefix'
_DEVKIT_DIR = 'devkit_directory'
_RAW_DIR = 'raw_dir'

# Available datasets
_DATASETS = {
    'storms_2017_train': {
        _IM_DIR:
            _DATA_DIR + '/storms/storms_train2017',
        _ANN_FN:
            _DATA_DIR + '/storms/annotations/instances_train2017.json'
    },
    'storms_2017_val': {
        _IM_DIR:
            _DATA_DIR + '/storms/storms_val2017',
        _ANN_FN:
            _DATA_DIR + '/storms/annotations/instances_val2017.json'
    },
    # 'coco_2014_train': {
    #     _IM_DIR:
    #         _DATA_DIR + '/coco/coco_train2014',
    #     _ANN_FN:
    #         _DATA_DIR + '/coco/annotations/instances_train2014.json'
    # },
    # 'coco_2014_val': {
    #     _IM_DIR:
    #         _DATA_DIR + '/coco/coco_val2014',
    #     _ANN_FN:
    #         _DATA_DIR + '/coco/annotations/instances_val2014.json'
    # },
    # 'coco_2014_minival': {
    #     _IM_DIR:
    #         _DATA_DIR + '/coco/coco_val2014',
    #     _ANN_FN:
    #         _DATA_DIR + '/coco/annotations/instances_minival2014.json'
    # },
    # 'coco_2014_valminusminival': {
    #     _IM_DIR:
    #         _DATA_DIR + '/coco/coco_val2014',
    #     _ANN_FN:
    #         _DATA_DIR + '/coco/annotations/instances_valminusminival2014.json'
    # },
    # 'keypoints_coco_2014_train': {
    #     _IM_DIR:
    #         _DATA_DIR + '/coco/coco_train2014',
    #     _ANN_FN:
    #         _DATA_DIR + '/coco/annotations/person_keypoints_train2014.json'
    # },
    # 'keypoints_coco_2014_val': {
    #     _IM_DIR:
    #         _DATA_DIR + '/coco/coco_val2014',
    #     _ANN_FN:
    #         _DATA_DIR + '/coco/annotations/person_keypoints_val2014.json'
    # },
    # 'keypoints_coco_2014_minival': {
    #     _IM_DIR:
    #         _DATA_DIR + '/coco/coco_val2014',
    #     _ANN_FN:
    #         _DATA_DIR + '/coco/annotations/person_keypoints_minival2014.json'
    # },
    # 'keypoints_coco_2014_valminusminival': {
    #     _IM_DIR:
    #         _DATA_DIR + '/coco/coco_val2014',
    #     _ANN_FN:
    #         _DATA_DIR + '/coco/annotations/person_keypoints_valminusminival2014.json'
    # },
}


def datasets():
    """Retrieve the list of available dataset names."""
    return _DATASETS.keys()


def contains(name):
    """Determine if the dataset is in the catalog."""
    return name in _DATASETS.keys()


def get_im_dir(name):
    """Retrieve the image directory for the dataset."""
    return _DATASETS[name][_IM_DIR]


def get_ann_fn(name):
    """Retrieve the annotation file for the dataset."""
    print("---------------------------------> ",_DATASETS[name][_ANN_FN])
    return _DATASETS[name][_ANN_FN]


def get_im_prefix(name):
    """Retrieve the image prefix for the dataset."""
    return _DATASETS[name][_IM_PREFIX] if _IM_PREFIX in _DATASETS[name] else ''


def get_devkit_dir(name):
    """Retrieve the devkit dir for the dataset."""
    return _DATASETS[name][_DEVKIT_DIR]


def get_raw_dir(name):
    """Retrieve the raw dir for the dataset."""
    return _DATASETS[name][_RAW_DIR]
