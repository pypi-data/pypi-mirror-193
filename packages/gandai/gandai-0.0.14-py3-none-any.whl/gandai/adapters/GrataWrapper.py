import pandas as pd
import requests
from gandai.datastore import Cloudstore
from gandai.adapters import filters

ds = Cloudstore()


class GrataWrapper:
    def __init__(self) -> None:
        self.token = self._authenticate()

    def build_similiar_targets_from_id(self, search_key: str, id: str, k=25):
        """Gets + Caches Feature Table"""

        json_data = {
            "filters": {
                "similar_companies": self._get_similiars_filter([id]),
                "tolerance": 100,
            },
            "page": 1,
            "page_size": k,
            "paging": True,
            "query": "",
        }

        response = requests.post(
            "https://search.grata.com/api/search/",
            headers={"authorization": self.token},
            json=json_data,
        )

        if response.status_code != 200:
            print(response)  # .code, response.content)
            return data

        data = response.json()
        print(data.keys(), "todo handle suggested keywords")
        features: pd.DataFrame = self._get_features(data)
        gs_url = f"gs://{ds.bucket_name}/searches/{search_key}/companies/{id}.feather"
        features.to_feather(gs_url)
        print(features.shape, gs_url)

    def _get_targets_from_keyword(self, keyword: str, k=25) -> dict:
        json_data = {
            "filters": {
                "keywords": self._get_keywords_filter([keyword]),
                "locations": filters.CORE_LOCATION_FILTER,
            },
            "page": 1,
            "page_size": k,
            "query": "",
        }
        response = requests.post(
            "https://search.grata.com/api/search/",
            headers={"authorization": self.token},
            json=json_data,
        )
        data = response.json()
        return data

    def build_targets_from_keyword(self, search_key: str, keyword: str, k=25) -> None:
        """Gets + Caches Feature Table"""
        data = self._get_targets_from_keyword(keyword, k)
        features: pd.DataFrame = self._get_features(data)
        gs_url = f"gs://{ds.bucket_name}/searches/{search_key}/companies/{str(keyword)}.feather"
        features.to_feather(gs_url)

    @staticmethod
    def _authenticate():
        def _set_token(token: str) -> None:
            ds["env/GRATA_TOKEN"] = token

        json_data = {
            "email": "parker@genzassociates.com",  # todo: env/GRATA_USER
            "password": ds["env/GRATA_PASSWORD"],
        }

        response = requests.post(
            "https://login.grata.com/api/authenticate/", json=json_data
        )
        data = response.json()
        token = data["user"]["token"]
        _set_token(f"Token {token}")
        return f"Token {token}"

    @staticmethod
    def _get_keywords_filter(keywords: list) -> dict:
        return {
            "op": "and",
            "conditions": [
                {
                    "include": keywords,
                    "exclude": [],
                    "op": "any",
                    "match": "core",
                    "weight": 3,
                    "type": "filter",
                },
            ],
        }

    @staticmethod
    def _get_similiars_filter(ids: list) -> dict:
        # NB filters also takes a tolerance, e.g. 100
        return {
            "op": "and",
            "conditions": [
                {
                    "include": ids,
                    "exclude": [],
                    "op": "any",
                },
            ],
        }

    @staticmethod
    def _get_features(data: dict) -> pd.DataFrame:
        COUNTRIES = ["USA", "CAN", "GBR", "MEX"]
        OWNERSHIP_EXCLUDE = [
            "Public",
            "Private Equity Add-On",
            "Private Subsidiary",
            "Public Subsidiary",
        ]

        df = pd.DataFrame(data["companies"])
        # add features
        df["employee_count"] = df["employees"].apply(lambda x: x.get("value"))
        df["country"] = (
            df["headquarters"].dropna().apply(lambda x: x.get("country_iso"))
        )
        df['web_hit_count'] = df['hits'].apply(lambda x: x['web']['hit_count'])

        # filter
        df = df.query("employee_count > 10")
        df = df.query("ownership not in @OWNERSHIP_EXCLUDE")
        df = df.query("country in @COUNTRIES")
        df = df.dropna(subset=["employee_count"])

        # select columns, errr should I bother?
        # consider the size difference, or maybe handling typing is annoying,
        # tbd
        df = df[
            [
                # "search_key",
                "name",
                "domain",
                "description",
                "employee_count",
                "ownership",
                "web_hit_count",
                "primary_business_model_name",
                "country",
                "id",
            ]
        ]

        # sort
        # df['ownership'] = df['ownership'].astype('category')
        # df['ownership'] = df['ownership'].cat.set_categories(['Bootstrapped','Investor Backed'])
        # df = df.sort_values(["ownership","employee_count"], ascending=[True, False]).reset_index(drop=True)
        # df = df.sort_values("employee_count", ascending=False).reset_index(drop=True)
        df = df.reset_index(drop=True)
        return df
