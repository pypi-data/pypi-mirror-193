from typing import Union
import json
from zipfile import ZipFile
from pathlib import Path
import pandas as pd
import os
from glob import glob

package_dir = Path(__file__).parent.parent


def bundles_query(path: str) -> pd.DataFrame:
    """
    Takes in a path pointing to .zip, .feather, or directory of FHIR bundles
    adds concept of bundle_index (i.e. where was it in the list) for PMI
    ensures / overwrites 'total'
    Returns Bundles in a DataFrame.
    """
    if "synthea_sample" in path:
        path = f"{package_dir}/data/synthetic/synthea_10.zip"

    filetype = path.split(".")[-1]
    if filetype == "zip":
        zf = ZipFile(path)
        bundles = [json.load(zf.open(f)) for f in zf.namelist()[1::]]
        bundles = pd.DataFrame(bundles)
    elif os.path.isdir(path):

        def _open(bundle_path):
            # handle gz
            with open(bundle_path, "r") as f:
                data = json.loads(f.read())
            if pd.isna(data):
                # handle a null bundle better
                return {}
            else:
                return data

        bundle_paths = glob(f"{path}/*.json")
        bundles = pd.DataFrame([_open(p) for p in bundle_paths])
        bundles = bundles.dropna(subset=["resourceType"])
        # todo # handle a null bundle better

    bundles = bundles.reset_index().rename(columns={"index": "bundle_index"})
    bundles["total"] = bundles["entry"].apply(lambda x: len(x))
    assert "bundle_index" in bundles.columns
    return bundles


def valueset_query(oid: str) -> pd.DataFrame:
    """
    Query OID from package data
    """

    def _get_vs(oid: str) -> dict:
        vs_path = f"{package_dir}/data/valuesets/{oid}.json"
        with open(vs_path, "r") as f:
            vs = json.load(f)
        return vs

    return pd.DataFrame([_get_vs(oid)])


def context_path_query(context_key: str) -> pd.DataFrame:
    with open(f"{package_dir}/data/contexts.json", "r") as f:
        contexts = json.load(f)
    return pd.DataFrame(dict(path=contexts[context_key]["path"]))


def context_code_query(context_key: str) -> pd.DataFrame:
    with open(f"{package_dir}/data/contexts.json", "r") as f:
        contexts = json.load(f)
    return pd.DataFrame(dict(code=contexts[context_key]["code"]))


def ig_struct_query(
    resource_types: list = [],
    must_support=False,
) -> pd.DataFrame:
    """
    Point at a directory of fhir struct defitition directory
    And the relavent resource_types
    Returns the path, datatypes
    """

    def _struct_element_snapshot_query(struct_path: str) -> pd.DataFrame:
        with open(struct_path, "r") as f:
            data = json.load(f)
        df = pd.DataFrame(data["snapshot"]["element"])
        df["_file"] = struct_path
        return df

    structs_dir = (f"{package_dir}/data/structs",)
    struct_paths = glob(f"{structs_dir}/*")[1::]
    df = pd.concat(
        _struct_element_snapshot_query(p) for p in struct_paths
    ).reset_index()
    cols = ["path", "min", "max", "type", "mustSupport"]
    if must_support == True:
        df = df[df["mustSupport"] == True]
    df = df[cols]
    df["resourceType"] = df["path"].apply(lambda x: x.split(".")[0])
    if len(resource_types) > 0:
        df = df[df["resourceType"].isin(resource_types)]
    return df.reset_index(drop=True)
