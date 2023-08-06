import pandas as pd

from concurrent.futures import ThreadPoolExecutor
from gandai.datastore import Cloudstore

ds = Cloudstore()


def companies_query(search_key: str) -> pd.DataFrame:
    keys = ds.keys(f"searches/{search_key}/companies")
    if len(keys) == 0:
        return pd.DataFrame(dict(domain=[]))
    # wait a minuteeee...what if there are those obj{} companies
    gs_paths = [f"gs://{ds.bucket_name}/{k}" for k in keys]
    with ThreadPoolExecutor(max_workers=20) as exec:
        futures = exec.map(pd.read_feather, gs_paths)
    df = pd.concat(list(futures))
    df = df.dropna(subset=['domain']) # 
    df = df.drop_duplicates(subset=['domain']).reset_index(drop=True)
    return df

def events_query(search_key: str) -> pd.DataFrame:
    keys = ds.keys(f"searches/{search_key}/events")
    return pd.DataFrame(ds.load_async(keys))

def comments_query(search_key: str) -> pd.DataFrame:
    keys = ds.keys(f"searches/{search_key}/comments")
    return pd.DataFrame(ds.load_async(keys))

def searches_query() -> pd.DataFrame:
    keys = ds.keys(f"searches/")
    keys = [k for k in keys if k.endswith('search')]
    return pd.DataFrame(ds.load_async(keys))
    
def conflicts_query() -> pd.DataFrame:
    df = pd.read_feather(f"gs://{ds.bucket_name}/global/dealcloud_conflict_domain.feather")
    return df