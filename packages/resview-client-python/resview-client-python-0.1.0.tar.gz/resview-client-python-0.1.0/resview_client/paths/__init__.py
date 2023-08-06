# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from resview_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_RESERVATIONS_ = "/api/reservations/"
    API_RESERVATIONS_ID_ = "/api/reservations/{id}/"
    API_RESERVATIONSGET_BATCH_ = "/api/reservations:getBatch/"
