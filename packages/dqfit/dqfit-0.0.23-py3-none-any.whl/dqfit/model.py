# import mapply
import pandas as pd
import numpy as np
import plotly.express as px
from IPython.display import display

from dqfit.services import Query
from dqfit.preprocessing import BundleFramer
from dqfit.categories import Complete, Conformant, Plausible, Timely

# mapply.init(n_workers=-1)


class DQIModel:
    def __init__(
        self,
        srcdir: str,
        outdir=False,
        context=[],
        categories=["conformant", "complete", "plausible"],
    ):
        self.srcdir: str = srcdir
        self.outdir: str = outdir
        self.context: list = context
        self.categories: list = categories
        self.context_path: pd.Series = self._load_context_path()
        self.results: pd.DataFrame = self.fit()
        self.index = self._get_index()
        self.features = self.results[[]]
        self.fhir_path_summary = self._fhir_path_summary()
        if outdir:
            self._handle_out()

    def visualize(self):
        print(f"Index: {self.index}")
        display(self.results)
        display(self.fhir_path_summary)
        self._visualize_fhir_path_summary().show()  # renderer='notebook' fickle

    def fit(self) -> pd.DataFrame:
        bundles = Query.bundles_query(self.srcdir)
        # add tdqm?
        bundles["fhir_path"] = bundles.apply(
            self._score_bundle, axis=1
        )  # ok this is the bottleneck
        bundles["conformant"] = bundles["fhir_path"].apply(
            lambda x: x["conformant"].mean()
        )
        bundles["complete"] = bundles["fhir_path"].apply(lambda x: x["complete"].mean())
        bundles["plausible"] = bundles["fhir_path"].apply(
            lambda x: x["plausible"].mean()
        )
        bundles["timely"] = bundles["fhir_path"].apply(lambda x: x["timely"].max())
        print(f"Processed {len(bundles)} bundles")
        return bundles

    def _get_index(self):
        index = int(self.results["patient_level_score"].sum().sum())
        return index

    def _load_context_path(self) -> pd.Series:
        # WIP
        context = Query.ig_struct_query(
            resource_types=["Coverage","Patient", "Condition", "Procedure", "Observation"],
            must_support=True,
        )
        return context["path"]

    def _score_bundle(self, bundle: pd.Series) -> pd.DataFrame:
        """
        A FHIR Path is...
        Patient.birthDate
        Patient.telecom
        Observation.status

        For each Path in the Bundle and in the Context,
        assign score per category
        """
        fhir_path = BundleFramer.fhir_path_frame(bundle)
        fhir_path = fhir_path[fhir_path["path"].isin(self.context_path)].reset_index(
            drop=True
        )
        fhir_path["conformant"] = fhir_path.apply(Conformant.score, axis=1)
        fhir_path["complete"] = fhir_path.apply(Complete.score, axis=1)
        fhir_path["plausible"] = fhir_path.apply(Plausible.score, axis=1)
        fhir_path = Timely.score(fhir_path)  # merges dates back
        return fhir_path

    def _handle_out(self):
        result_vectors = ["bundle_index", "fhir_path", *self.categories]
        df = self.results[result_vectors].reset_index(drop=True)
        df["fhir_path"] = df["fhir_path"].apply(lambda x: x.to_dict(orient="records"))
        df.to_json(f"{self.outdir}/results.json", orient="records")
        fig = self._visualize_fhir_path_summary()
        fig.write_html(f"{self.outdir}/fhir_path_summary.html")
        print(f"Results saved to {self.outdir}")

    # @staticmethod
    # def _score_patient_level(fhir_path: pd.Series) -> np.array:
    #     return np.array(
    #         [
    #             fhir_path["conformant"].mean(),
    #             fhir_path["complete"].mean(),
    #             fhir_path["plausible"].mean(),
    #             # fhir_path["timely"].mean(), # WIP
    #         ]
    #     )

    # def _patient_level_matrix(self):
    #     df = pd.DataFrame(list(self.results['patient_level_score']))
    #     df = df.rename(columns={0:'conformant',1:'complete',2:'plausible'})
    #     df['count'] = self.results['total']
    #     df['timely'] = self.results['timely']
    #     return df

    def cohort_fhir_path(self):
        return pd.concat(list(self.results["fhir_path"]))

    def _fhir_path_summary(self):
        cohort_fhir_path = self.cohort_fhir_path()
        fhir_path_summary = cohort_fhir_path.groupby(["resourceType", "path"]).agg(
            document_count=("bundle_index", "nunique"),
            term_count=("path", "count"),
            conformant=("conformant", "mean"),
            complete=("complete", "mean"),
            plausible=("plausible", "mean"),
            timely=("timely", "max"),
        )
        # fhir_path_summary

        return fhir_path_summary.reset_index()

    def _visualize_fhir_path_summary(self):
        df = self.fhir_path_summary.melt(
            id_vars=["resourceType", "path", "document_count", "term_count"]
        )
        fig = px.scatter(
            df,
            y="path",
            x="value",
            facet_col="variable",
            title=f"Index: {self.index} | n={len(self.results)} | Context {self.context}",
            hover_data=["document_count", "term_count"],
            color="resourceType",
            height=600,
        )
        return fig
