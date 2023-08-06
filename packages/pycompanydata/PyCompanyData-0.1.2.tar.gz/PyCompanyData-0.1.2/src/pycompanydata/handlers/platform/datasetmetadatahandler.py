from pycompanydata.data_types.platform.datasetmetadata import (
    DataSetMetadata,
    DataSetMetaDataPaginatedResponse,
)
from pycompanydata.handlers.base import BaseHandler


class DataSetHandler(BaseHandler):

    path = "companies/"

    def get_all_data_sets(
        self, company_id: str, **kwargs
    ) -> DataSetMetaDataPaginatedResponse:
        result = self.client.get(self.path + company_id + "/data/history", **kwargs)
        return DataSetMetaDataPaginatedResponse(**result)

    def get_single_data_set(self, company_id: str, data_set_id: str) -> DataSetMetadata:
        result = self.client.get(
            self.path + company_id + "/data/history/" + data_set_id
        )
        return DataSetMetadata(**result)
