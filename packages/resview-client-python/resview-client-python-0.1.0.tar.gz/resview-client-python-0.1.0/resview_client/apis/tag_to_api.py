import typing_extensions

from resview_client.apis.tags import TagValues
from resview_client.apis.tags.reservations_api import ReservationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.RESERVATIONS: ReservationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.RESERVATIONS: ReservationsApi,
    }
)
