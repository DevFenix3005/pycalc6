# -*- mode: python ; coding: utf-8 -*-
import shutil
import os

distribution_home = "./dist"
app_name = "PyCalc6"
assets_folder = "assets"
dist_assets_path = f"{distribution_home}/{app_name}/{assets_folder}"
files_to_copy = ["styles.qss"]

if not os.path.exists(dist_assets_path):
    os.makedirs(dist_assets_path)


[
    shutil.copyfile(f"./{assets_folder}/{file}", f"{dist_assets_path}/{file}")
    for file in files_to_copy
]
