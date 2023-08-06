import sys
import json
import pandas as pd

from dqfit.categories import Complete, Conformant, Plausible, Timely
from dqfit.preprocessing import BundleFramer
from dqfit.services import Query, ContextManager

def fit_bundle(bundle, context_key) -> pd.DataFrame:
    assert(context_key in ContextManager.CONTEXTS.keys())
    fhir_path = BundleFramer.fhir_path_frame(bundle)
    fhir_path['Context'] = context_key
    fhir_path = Conformant.fit(fhir_path, context_key)
    fhir_path = Complete.fit(fhir_path, context_key) 
    fhir_path = Plausible.fit(fhir_path, context_key)
    # fhir_path = Timely.score(fhir_path, context)
    return fhir_path

def fhir_path_summary(fhir_path: pd.DataFrame, conformance_threshold = 0) -> pd.DataFrame:
    df = fhir_path[fhir_path['Conformant'] > conformance_threshold].reset_index(drop=True)
    return df.groupby(["resourceType", "path"]).agg(
            document_count=("bundle_index", "nunique"),
            term_count=("path", "count"),
            Conformant=("Conformant", "mean"),
            Complete=("Complete", "mean"),
            Plausible=("Plausible", "mean"),
            # timely=("timely", "max"),
        ).reset_index()

def score_bundles(bundles: pd.DataFrame, context_key: str) -> pd.DataFrame:
    df = bundles.copy()
    df['fhir_path'] = df.apply(fit_bundle, args=[context_key], axis=1)
    df['Context'] = context_key
    df['Conformant'] = df['fhir_path'].apply(lambda x: x['Conformant'].mean())
    df['Complete'] = df['fhir_path'].apply(lambda x: x['Complete'].mean())
    df['Plausible'] = df['fhir_path'].apply(lambda x: x['Plausible'].mean())
    return df

def main(srcdir: str, outdir: str, context_key: str) -> None:
    print("This package is currently in a research review phase")
    bundles = Query.bundles_query(srcdir)
    print(f"Found {len(bundles)} bundles.")
    cohort_level = score_bundles(bundles, context_key)
    cohort_fhir_path = pd.concat(list(cohort_level['fhir_path']))
    fhir_path_summary = fhir_path_summary(cohort_fhir_path)
    fhir_path_summary.to_csv(f"{outdir}/fhir_path_summary.csv", index=False)
    index = dict(cohort_level[['Conformant','Complete','Plausible']].mean())
    with open(f"{outdir}/index.json") as f:
        json.dump(index, f)
    print(index)
    

if __name__ == "__main__":
    print("Useage: python -m main.py [srcdir] [outdir] [context]")
    srcdir = sys.argv[1]
    outdir = sys.argv[2]
    context = sys.argv[3]
    main(srcdir, outdir,[context])