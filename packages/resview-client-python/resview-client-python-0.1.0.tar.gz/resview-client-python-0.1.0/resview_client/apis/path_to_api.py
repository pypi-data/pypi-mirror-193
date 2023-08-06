import typing_extensions

from resview_client.paths import PathValues
from resview_client.apis.paths.api_reservations_ import ApiReservations
from resview_client.apis.paths.api_reservations_id_ import ApiReservationsId
from resview_client.apis.paths.api_reservationsget_batch_ import ApiReservationsgetBatch

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_RESERVATIONS_: ApiReservations,
        PathValues.API_RESERVATIONS_ID_: ApiReservationsId,
        PathValues.API_RESERVATIONSGET_BATCH_: ApiReservationsgetBatch,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_RESERVATIONS_: ApiReservations,
        PathValues.API_RESERVATIONS_ID_: ApiReservationsId,
        PathValues.API_RESERVATIONSGET_BATCH_: ApiReservationsgetBatch,
    }
)
