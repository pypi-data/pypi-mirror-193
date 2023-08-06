from gandai.datastore import Cloudstore
from gandai.models import Event
from gandai.services import Query
# from gandai.adapters import Grata

ds = Cloudstore()

from time import time
def load_search(search_key: str, actor_key: str = "") -> dict:

    def _get_comments(domain: str) -> list:
        if len(comments) == 0:
            return []
        return comments.query("domain == @domain").to_dict(orient="records")

    def _get_events(domain: str) -> list:
        if len(events) == 0:
            return []
        return events.query("domain == @domain").to_dict(orient="records")
        
    def _companies_by_state(last_event_type: str) -> list:
        df = companies.query("last_event_type == @last_event_type")
        return df.fillna("").to_dict(orient="records")


    t0 = time()
    companies = Query.companies_query(search_key)
    events = Query.events_query(search_key)
    comments = Query.comments_query(search_key)
    conflicts = Query.conflicts_query()
    # import pdb; pdb.set_trace()
    print("queries:", (time()-t0))
    companies["comments"] = companies["domain"].apply(_get_comments)
    companies["events"] = companies["domain"].apply(_get_events)
    companies["last_event_type"] = companies["events"].apply(
        lambda x: x[-1]["type"] if len(x) > 0 else "created"
    )

    companies = companies.merge(conflicts, how='left', left_on='domain', right_on='domain')
    companies['dealcloud_id'] = companies['dealcloud_id'].fillna("")

    
    inbox = _companies_by_state("created")
    review = _companies_by_state("advance")
    qualified = _companies_by_state("qualify")
    rejected = _companies_by_state("reject")
    conflict = _companies_by_state("conflict")

    search_data = ds[f"searches/{search_key}/search"]

    resp = {
        "key": search_key,
        "actor_key": actor_key,
        "meta": search_data['meta'],
        "keywords": search_data['keywords'],
        "filters": search_data['filters'],
        "companies": {
            "inbox": inbox,
            "review": review,
            "outbox": [], # TODO
            "qualified": qualified,
            "rejected": rejected,
            "conflict": conflict

        },
    }
    return resp



# def fetch_similiar(id: str) -> None:
#     Grata.







# def build_targets(search_key: str, actor_key: str): 
#     def _cache_similiar(grata_id: str, page_size=50):
#         data = Grata._search_similiar([grata_id], page_size=page_size)
#         def _write_features(grata_data, search_key):
#             # rm company_features_ prefix ?
#             gs_path = f"gs://{ds.bucket_name}/searches/{search_key}/companies/company_features_{grata_id}.feather"
#             df = Grata._get_features(grata_data=grata_data, search_key=search_key)
#             print(df.shape)
#             df.to_feather(gs_path)
#         _write_features(data, search_key)

#     qualified_companies = [] #query this
#     grata_ids = [co['id'] for co in qualified_companies]
#     exisiting_tables = ds.keys("/searches/{search_key}/companies/")
#     exisiting_keys = [exisiting_tables]
#     for grata_id in grata_ids:
#         _cache_similiar(grata_id)

    