import crm.models
from typing import List
def go(item: crm.models.Zayavki)->List[int]:
    okrug_list_ids=list(item.okrug)
    return okrug_list_ids