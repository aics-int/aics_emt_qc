import os

from camera_alignment_core.align import Align
from camera_alignment_core.constants import (
    Magnification,
)
import pandas as pd

"""
PROD_DIR = "/allen/aics/microscopy/PRODUCTION/PIPELINE_8_1"

paths = pd.read_csv("/allen/aics/microscopy/Aditya/pipeline8_1_paths.csv")
paths = paths[2:]
for i, row in paths.iterrows():
    # Define Experiment directory which we are looking through
    exp_dir = row["Isilon path"][1:-4].replace("\\", "/")

    # Creates an output dir for aligned and split files if it doesn't exist already
    output_dir = f"{exp_dir}/aligned_split"
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Assigns optical control path from csv generated from confluence page with all info
    optical_control_path = row["Argolight Isilon path"][1:].replace("\\", "/")
    # if not optical_control_path.endswith('.czi'):
    #     optical_control_path = f'{optical_control_path}/.{optical_control_path.split("/")[-2]}.czi'

    # Walks through all files/dirs in exp_dir and finds all that are czi's
    # and splits and aligns them
    for dirpath, dirnames, filenames in os.walk(exp_dir):
        for filename in [f for f in filenames if f.endswith(".czi")]:
            block_num = int(
                filename[filename.find("Block") + 5 : filename.find("Block") + 6]
            )
            if block_num < 1:
                continue
            czi_path = f"{dirpath}/{filename}"
            align = Align(
                optical_control=optical_control_path,
                magnification=Magnification(63),
                out_dir=output_dir,
            )
            if block_num == 7:
                try:
                    aligned_scenes = align.align_image(
                        czi_path, channels_to_shift=[1, 2]
                    )
                    aligned_optical_control = align.align_optical_control(
                        channels_to_shift=[1, 2]
                    )
                    alignment_matrix = align.alignment_transform.matrix
                    alignment_info = align.alignment_transform.info
                except Exception as e:
                    print(e)
            else:
                try:
                    aligned_scenes = align.align_image(czi_path, channels_to_shift=[1])
                    aligned_optical_control = align.align_optical_control(
                        channels_to_shift=[1]
                    )
                    alignment_matrix = align.alignment_transform.matrix
                    alignment_info = align.alignment_transform.info
                except Exception as e:
                    print(e)
 """


def align_emt(exp_dir, optical_control_path):

    # Creates an output dir for aligned and split files if it doesn't exist already
    output_dir = f"{exp_dir}/aligned_split"
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
        print(f"Created folder: {output_dir}")
    else:
        print(f"Folder already exists: {output_dir}")

    for dirpath, _, filenames in os.walk(exp_dir):
        for filename in [f for f in filenames if f.endswith(".czi")]:
            block_num = int(
                filename[filename.find("Block") + 5 : filename.find("Block") + 6]
            )
            if block_num < 1:
                continue
            czi_path = f"{dirpath}/{filename}"
            align = Align(
                optical_control=optical_control_path,
                magnification=Magnification(63),
                out_dir=output_dir,
            )
            if block_num == 7:
                try:
                    _ = align.align_image(czi_path, channels_to_shift=[1, 2])
                    _ = align.align_optical_control(channels_to_shift=[1, 2])
                    _ = align.alignment_transform.matrix
                    _ = align.alignment_transform.info
                except Exception as e:
                    print(e)
            else:
                try:
                    _ = align.align_image(czi_path, channels_to_shift=[1])
                    _ = align.align_optical_control(channels_to_shift=[1])
                    _ = align.alignment_transform.matrix
                    _ = align.alignment_transform.info
                except Exception as e:
                    print(e)
    print(f"Completed alignments for {exp_dir}")


paths = pd.read_csv("/allen/aics/microscopy/Aditya/pipeline8_1_paths_remaining.csv")


for i, row in paths.iterrows():
    exp_dir = row["Isilon path"][1:-4].replace("\\", "/")
    optical_control_path = row["Argolight Isilon path"][1:].replace("\\", "/")
    align_emt(exp_dir, optical_control_path)
