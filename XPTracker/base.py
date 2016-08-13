PROJECT_TITLE = 'title'
PROJECT_DESCR = 'description'
PROJECT_RELEASE_DATE = 'release_date'
PROJECT_ID = 'identifier'


PROJECT_IDS = ['id_title', 'id_description', 'id_release_date', 'id_identifier']

US_FIELDS_IDS = {'title': 'id_title', 'estimate_time': 'id_estimate_time'}

class BaseModel(object):

    def set_fields_html_ids(self, ids):
        assert len(self.fields) == len(ids)
        fields_ids = {}
        for i, field in enumerate(self.fields):
            fields_ids[field] = ids[i]
        return fields_ids



class BaseProjectModel(BaseModel):

    def __init__(self):
        self.fields = [PROJECT_TITLE, PROJECT_DESCR, PROJECT_RELEASE_DATE, PROJECT_ID]
        self.fields_html_ids = self.set_fields_html_ids(PROJECT_IDS)
