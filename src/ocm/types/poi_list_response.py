# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .country import Country
from .._models import BaseModel

__all__ = [
    "PoiListResponse",
    "PoiListResponseItem",
    "PoiListResponseItemAddressInfo",
    "PoiListResponseItemConnection",
    "PoiListResponseItemConnectionConnectionType",
    "PoiListResponseItemConnectionCurrentType",
    "PoiListResponseItemConnectionLevel",
    "PoiListResponseItemConnectionStatusType",
    "PoiListResponseItemDataProvider",
    "PoiListResponseItemDataProviderDataProviderStatusType",
    "PoiListResponseItemMediaItem",
    "PoiListResponseItemMediaItemUser",
    "PoiListResponseItemOperatorInfo",
    "PoiListResponseItemOperatorInfoAddressInfo",
    "PoiListResponseItemStatusType",
    "PoiListResponseItemSubmissionStatus",
    "PoiListResponseItemUsageType",
    "PoiListResponseItemUserComment",
    "PoiListResponseItemUserCommentCheckinStatusType",
    "PoiListResponseItemUserCommentCommentType",
    "PoiListResponseItemUserCommentUser",
]


class PoiListResponseItemAddressInfo(BaseModel):
    """Geographic position for site and (nearest) address component information."""

    country_id: int = FieldInfo(alias="CountryID")
    """The reference ID for the Country"""

    id: int = FieldInfo(alias="ID")
    """ID"""

    latitude: float = FieldInfo(alias="Latitude")
    """Site latitude coordinate in decimal degrees"""

    longitude: float = FieldInfo(alias="Longitude")
    """Site longitude coordinate in decimal degrees"""

    access_comments: Optional[str] = FieldInfo(alias="AccessComments", default=None)
    """Guidance for users to use or find the equipment"""

    address_line1: Optional[str] = FieldInfo(alias="AddressLine1", default=None)
    """First line of nearby street address"""

    address_line2: Optional[str] = FieldInfo(alias="AddressLine2", default=None)
    """Second line of nearby street address"""

    contact_email: Optional[str] = FieldInfo(alias="ContactEmail", default=None)
    """Primary contact email"""

    contact_telephone1: Optional[str] = FieldInfo(alias="ContactTelephone1", default=None)
    """Primary contact number"""

    contact_telephone2: Optional[str] = FieldInfo(alias="ContactTelephone2", default=None)
    """Secondary contact number"""

    country: Optional[Country] = FieldInfo(alias="Country", default=None)
    """Country details"""

    distance: Optional[float] = FieldInfo(alias="Distance", default=None)
    """Distance from search location, if search is around a point"""

    distance_unit: Optional[int] = FieldInfo(alias="DistanceUnit", default=None)
    """Unit used for distance, 1= Miles, 2 = KM"""

    postcode: Optional[str] = FieldInfo(alias="Postcode", default=None)
    """Postal code or Zipcode"""

    related_url: Optional[str] = FieldInfo(alias="RelatedURL", default=None)
    """Optional website for more information"""

    state_or_province: Optional[str] = FieldInfo(alias="StateOrProvince", default=None)
    """State or Province"""

    title: Optional[str] = FieldInfo(alias="Title", default=None)
    """General title for this location to aid user"""

    town: Optional[str] = FieldInfo(alias="Town", default=None)
    """Town or City"""


class PoiListResponseItemConnectionConnectionType(BaseModel):
    """The type of end-user connection an EVSE supports."""

    formal_name: Optional[str] = FieldInfo(alias="FormalName", default=None)
    """Formal (standard) name for this connection type"""

    id: Optional[int] = FieldInfo(alias="ID", default=None)

    is_discontinued: Optional[bool] = FieldInfo(alias="IsDiscontinued", default=None)
    """If true, this is an discontinued but used connection type"""

    is_obsolete: Optional[bool] = FieldInfo(alias="IsObsolete", default=None)
    """
    If true, this is an obsolete connection type and is unlikely top be present in
    modern infrastructure
    """

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class PoiListResponseItemConnectionCurrentType(BaseModel):
    """Indicates the EVSE power supply type e.g.

    DC (Direct Current), AC (Single Phase), AC (3 Phase).
    """

    id: int = FieldInfo(alias="ID")

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class PoiListResponseItemConnectionLevel(BaseModel):
    """A general category for equipment power capability.

    Deprecated for general use. Currently computed automatically based on equipment power.
    """

    comments: str = FieldInfo(alias="Comments")

    id: int = FieldInfo(alias="ID")

    is_fast_charge_capable: bool = FieldInfo(alias="IsFastChargeCapable")
    """If true, this level is considered 'fast' charging, relative to other levels."""

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class PoiListResponseItemConnectionStatusType(BaseModel):
    """
    The Status Type of a site or equipment item indicates whether it is generally operational.
    """

    id: int = FieldInfo(alias="ID")

    is_operational: bool = FieldInfo(alias="IsOperational")

    is_user_selectable: bool = FieldInfo(alias="IsUserSelectable")

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class PoiListResponseItemConnection(BaseModel):
    """Details on the equipment type and power capability.

    If calling the API in verbose mode related models are also included in the result (e.g. ConnectionType, Level, StatusType, CurrentType)
    """

    amps: Optional[int] = FieldInfo(alias="Amps", default=None)
    """EVSE supply max current in Amps"""

    comments: Optional[str] = FieldInfo(alias="Comments", default=None)

    connection_type: Optional[PoiListResponseItemConnectionConnectionType] = FieldInfo(
        alias="ConnectionType", default=None
    )
    """The type of end-user connection an EVSE supports."""

    connection_type_id: Optional[int] = FieldInfo(alias="ConnectionTypeID", default=None)

    current_type: Optional[PoiListResponseItemConnectionCurrentType] = FieldInfo(alias="CurrentType", default=None)
    """Indicates the EVSE power supply type e.g.

    DC (Direct Current), AC (Single Phase), AC (3 Phase).
    """

    current_type_id: Optional[int] = FieldInfo(alias="CurrentTypeID", default=None)
    """The supply type reference ID (e.g. DC etc)"""

    id: Optional[int] = FieldInfo(alias="ID", default=None)

    level: Optional[PoiListResponseItemConnectionLevel] = FieldInfo(alias="Level", default=None)
    """A general category for equipment power capability.

    Deprecated for general use. Currently computed automatically based on equipment
    power.
    """

    level_id: Optional[int] = FieldInfo(alias="LevelID", default=None)
    """A general category for power capability.

    Depreceated in favour of documenting specific equipment power in kW.
    """

    power_kw: Optional[float] = FieldInfo(alias="PowerKW", default=None)
    """Peak available power in kW"""

    quantity: Optional[int] = FieldInfo(alias="Quantity", default=None)
    """Optional summary number of equipment items available with this specification"""

    reference: Optional[str] = FieldInfo(alias="Reference", default=None)
    """Optional operators reference for this connection/port"""

    status_type: Optional[PoiListResponseItemConnectionStatusType] = FieldInfo(alias="StatusType", default=None)
    """
    The Status Type of a site or equipment item indicates whether it is generally
    operational.
    """

    status_type_id: Optional[int] = FieldInfo(alias="StatusTypeID", default=None)
    """Status Type reference ID. 0 = Unknown"""

    voltage: Optional[float] = FieldInfo(alias="Voltage", default=None)
    """EVSE supply voltage"""


class PoiListResponseItemDataProviderDataProviderStatusType(BaseModel):
    """
    Status object describing whether this data provider is currently enabled and the type of source (manual entry, imported etc)
    """

    id: int = FieldInfo(alias="ID")
    """The reference ID for this provider status type"""

    is_provider_enabled: bool = FieldInfo(alias="IsProviderEnabled")
    """If false, results from this data provider are not currently enabled"""

    description: Optional[str] = None
    """The Title of this status type"""


class PoiListResponseItemDataProvider(BaseModel):
    """
    A Data Provider is the controller of the source data set used to construct the details for this POI. Data has been transformed and interpreted from it's original form. Each Data Provider provides data either by an explicit license or agreement.
    """

    id: int = FieldInfo(alias="ID")
    """The reference ID for this Data Provider"""

    is_restricted_edit: bool = FieldInfo(alias="IsRestrictedEdit")
    """Currently not implemented. Indicates a potential editing restriction."""

    comments: Optional[str] = FieldInfo(alias="Comments", default=None)
    """General public comments with information about this Data Provider."""

    data_provider_status_type: Optional[PoiListResponseItemDataProviderDataProviderStatusType] = FieldInfo(
        alias="DataProviderStatusType", default=None
    )
    """
    Status object describing whether this data provider is currently enabled and the
    type of source (manual entry, imported etc)
    """

    date_last_imported: Optional[datetime] = FieldInfo(alias="DateLastImported", default=None)
    """
    Date and time (UTC) the last import was performed for this data provider (if an
    import).
    """

    is_approved_import: Optional[bool] = FieldInfo(alias="IsApprovedImport", default=None)
    """If false, data may not be imported for this provider."""

    is_open_data_licensed: Optional[bool] = FieldInfo(alias="IsOpenDataLicensed", default=None)
    """If true, data provider uses an Open Data license"""

    license: Optional[str] = FieldInfo(alias="License", default=None)
    """Summary of the licensing which applies for this Data Provider.

    Each Data Provider has one specific license or agreement. Usage of the data
    requires acceptance of the given license.
    """

    title: Optional[str] = FieldInfo(alias="Title", default=None)
    """The Title for this Data Provider"""

    website_url: Optional[str] = FieldInfo(alias="WebsiteURL", default=None)
    """Website URL for this data provider"""


class PoiListResponseItemMediaItemUser(BaseModel):
    """Short public summary profile for a specific Open Charge Map user"""

    id: Optional[int] = FieldInfo(alias="ID", default=None)

    profile_image_url: Optional[str] = FieldInfo(alias="ProfileImageURL", default=None)

    reputation_points: Optional[int] = FieldInfo(alias="ReputationPoints", default=None)

    username: Optional[str] = FieldInfo(alias="Username", default=None)


class PoiListResponseItemMediaItem(BaseModel):
    """A user submitted media item related to a specific charge point or site.

    Currently always an image.
    """

    charge_point_id: Optional[str] = FieldInfo(alias="ChargePointID", default=None)

    comment: Optional[str] = FieldInfo(alias="Comment", default=None)

    date_created: Optional[str] = FieldInfo(alias="DateCreated", default=None)

    id: Optional[str] = FieldInfo(alias="ID", default=None)

    is_enabled: Optional[bool] = FieldInfo(alias="IsEnabled", default=None)

    is_external_resource: Optional[bool] = FieldInfo(alias="IsExternalResource", default=None)

    is_featured_item: Optional[bool] = FieldInfo(alias="IsFeaturedItem", default=None)

    is_video: Optional[bool] = FieldInfo(alias="IsVideo", default=None)

    item_thumbnail_url: Optional[str] = FieldInfo(alias="ItemThumbnailURL", default=None)

    item_url: Optional[str] = FieldInfo(alias="ItemURL", default=None)

    user: Optional[PoiListResponseItemMediaItemUser] = FieldInfo(alias="User", default=None)
    """Short public summary profile for a specific Open Charge Map user"""


class PoiListResponseItemOperatorInfoAddressInfo(BaseModel):
    """Geographic position for site and (nearest) address component information."""

    country_id: int = FieldInfo(alias="CountryID")
    """The reference ID for the Country"""

    id: int = FieldInfo(alias="ID")
    """ID"""

    latitude: float = FieldInfo(alias="Latitude")
    """Site latitude coordinate in decimal degrees"""

    longitude: float = FieldInfo(alias="Longitude")
    """Site longitude coordinate in decimal degrees"""

    access_comments: Optional[str] = FieldInfo(alias="AccessComments", default=None)
    """Guidance for users to use or find the equipment"""

    address_line1: Optional[str] = FieldInfo(alias="AddressLine1", default=None)
    """First line of nearby street address"""

    address_line2: Optional[str] = FieldInfo(alias="AddressLine2", default=None)
    """Second line of nearby street address"""

    contact_email: Optional[str] = FieldInfo(alias="ContactEmail", default=None)
    """Primary contact email"""

    contact_telephone1: Optional[str] = FieldInfo(alias="ContactTelephone1", default=None)
    """Primary contact number"""

    contact_telephone2: Optional[str] = FieldInfo(alias="ContactTelephone2", default=None)
    """Secondary contact number"""

    country: Optional[Country] = FieldInfo(alias="Country", default=None)
    """Country details"""

    distance: Optional[float] = FieldInfo(alias="Distance", default=None)
    """Distance from search location, if search is around a point"""

    distance_unit: Optional[int] = FieldInfo(alias="DistanceUnit", default=None)
    """Unit used for distance, 1= Miles, 2 = KM"""

    postcode: Optional[str] = FieldInfo(alias="Postcode", default=None)
    """Postal code or Zipcode"""

    related_url: Optional[str] = FieldInfo(alias="RelatedURL", default=None)
    """Optional website for more information"""

    state_or_province: Optional[str] = FieldInfo(alias="StateOrProvince", default=None)
    """State or Province"""

    title: Optional[str] = FieldInfo(alias="Title", default=None)
    """General title for this location to aid user"""

    town: Optional[str] = FieldInfo(alias="Town", default=None)
    """Town or City"""


class PoiListResponseItemOperatorInfo(BaseModel):
    """
    An Operator is the public organisation which controls a network of charging points.
    """

    id: int = FieldInfo(alias="ID")
    """Id"""

    address_info: Optional[PoiListResponseItemOperatorInfoAddressInfo] = FieldInfo(alias="AddressInfo", default=None)
    """Geographic position for site and (nearest) address component information."""

    booking_url: Optional[str] = FieldInfo(alias="BookingURL", default=None)

    comments: Optional[str] = FieldInfo(alias="Comments", default=None)

    contact_email: Optional[str] = FieldInfo(alias="ContactEmail", default=None)

    fault_report_email: Optional[str] = FieldInfo(alias="FaultReportEmail", default=None)
    """
    Used to send automated notification to network operator if a user submits a
    fault report comment/check-in
    """

    is_private_individual: Optional[bool] = FieldInfo(alias="IsPrivateIndividual", default=None)
    """If true, this operator represents a private individual"""

    is_restricted_edit: Optional[bool] = FieldInfo(alias="IsRestrictedEdit", default=None)
    """If true, this network restricts community edits for OCM data"""

    phone_primary_contact: Optional[str] = FieldInfo(alias="PhonePrimaryContact", default=None)
    """Primary contact number for network users"""

    phone_secondary_contact: Optional[str] = FieldInfo(alias="PhoneSecondaryContact", default=None)
    """Secondary contact number"""

    title: Optional[str] = FieldInfo(alias="Title", default=None)
    """Title"""

    website_url: Optional[str] = FieldInfo(alias="WebsiteURL", default=None)
    """Website for more information about this network"""


class PoiListResponseItemStatusType(BaseModel):
    """
    The Status Type of a site or equipment item indicates whether it is generally operational.
    """

    id: int = FieldInfo(alias="ID")

    is_operational: bool = FieldInfo(alias="IsOperational")

    is_user_selectable: bool = FieldInfo(alias="IsUserSelectable")

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class PoiListResponseItemSubmissionStatus(BaseModel):
    """Submission Status object, detailing the POI listing status"""

    id: int = FieldInfo(alias="ID")
    """Submission Status Type reference ID"""

    is_live: bool = FieldInfo(alias="IsLive")
    """If true, POI listing is live (not draft or de-listed)"""

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class PoiListResponseItemUsageType(BaseModel):
    """The Usage Type of a site indicates the general restrictions on usage."""

    id: int = FieldInfo(alias="ID")

    is_access_key_required: bool = FieldInfo(alias="IsAccessKeyRequired")
    """If true this usage required a physical access key"""

    is_membership_required: bool = FieldInfo(alias="IsMembershipRequired")
    """If true, this usage type requires registration or membership with a service."""

    is_pay_at_location: bool = FieldInfo(alias="IsPayAtLocation")
    """If true, usage requires paying at location"""

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class PoiListResponseItemUserCommentCheckinStatusType(BaseModel):
    """
    Classification for the users comment or experience using a specific charging location.
    """

    id: int = FieldInfo(alias="ID")

    is_automated_checkin: bool = FieldInfo(alias="IsAutomatedCheckin")
    """If true, checkin or comment was provided by an automated system."""

    is_positive: Optional[bool] = FieldInfo(alias="IsPositive", default=None)
    """If true, this type of checkin/comment is considered positive."""

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class PoiListResponseItemUserCommentCommentType(BaseModel):
    """Category for a user comment, e.g.

    General Comment, Fault Report (Notice To Users And Operator)
    """

    id: Optional[int] = FieldInfo(alias="ID", default=None)

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class PoiListResponseItemUserCommentUser(BaseModel):
    """Short public summary profile for a specific Open Charge Map user"""

    id: Optional[int] = FieldInfo(alias="ID", default=None)

    profile_image_url: Optional[str] = FieldInfo(alias="ProfileImageURL", default=None)

    reputation_points: Optional[int] = FieldInfo(alias="ReputationPoints", default=None)

    username: Optional[str] = FieldInfo(alias="Username", default=None)


class PoiListResponseItemUserComment(BaseModel):
    """A user comment or check-in for a specific charging point (POI/Site)"""

    charge_point_id: Optional[int] = FieldInfo(alias="ChargePointID", default=None)

    checkin_status_type: Optional[PoiListResponseItemUserCommentCheckinStatusType] = FieldInfo(
        alias="CheckinStatusType", default=None
    )
    """
    Classification for the users comment or experience using a specific charging
    location.
    """

    checkin_status_type_id: Optional[int] = FieldInfo(alias="CheckinStatusTypeID", default=None)

    comment: Optional[str] = FieldInfo(alias="Comment", default=None)

    comment_type: Optional[PoiListResponseItemUserCommentCommentType] = FieldInfo(alias="CommentType", default=None)
    """Category for a user comment, e.g.

    General Comment, Fault Report (Notice To Users And Operator)
    """

    comment_type_id: Optional[int] = FieldInfo(alias="CommentTypeID", default=None)

    date_created: Optional[datetime] = FieldInfo(alias="DateCreated", default=None)

    id: Optional[str] = FieldInfo(alias="ID", default=None)

    related_url: Optional[str] = FieldInfo(alias="RelatedURL", default=None)

    user: Optional[PoiListResponseItemUserCommentUser] = FieldInfo(alias="User", default=None)
    """Short public summary profile for a specific Open Charge Map user"""

    user_name: Optional[str] = FieldInfo(alias="UserName", default=None)


class PoiListResponseItem(BaseModel):
    """
    A POI (Point of Interest), also referred to as a `Site` or `ChargePoint`, is the top-level set of information regarding a geographic site with one or more electric vehicle charging equipment present. The term `ChargePointID` is used to reference the unique ID for each POI, as called OCM ID. This reference appears in various UI elements in the format `OCM-12345` to distinguish the ID number as being a reference for a specific POI/site.

    Note: If the API is called in verbose mode properties expanded properties are included in the results (e.g. UsageType, StatusType, DataProvider, OperatorInfo, SubmissionStatus).  With the exception of the AddressInfo property, other object properties will not be populated in a compact result set and instead only the associated reference IDs will be set (e.g. UsageTypeID, DataProviderID etc)
    """

    address_info: Optional[PoiListResponseItemAddressInfo] = FieldInfo(alias="AddressInfo", default=None)
    """Geographic position for site and (nearest) address component information."""

    connections: Optional[List[PoiListResponseItemConnection]] = FieldInfo(alias="Connections", default=None)
    """List of equipment summary information for this site"""

    data_provider: Optional[PoiListResponseItemDataProvider] = FieldInfo(alias="DataProvider", default=None)
    """
    A Data Provider is the controller of the source data set used to construct the
    details for this POI. Data has been transformed and interpreted from it's
    original form. Each Data Provider provides data either by an explicit license or
    agreement.
    """

    data_provider_id: Optional[int] = FieldInfo(alias="DataProviderID", default=None)
    """The reference ID for the Data Provider of this POI"""

    data_providers_reference: Optional[str] = FieldInfo(alias="DataProvidersReference", default=None)
    """
    If present, this is the Data Providers own key for this POI within their source
    data set
    """

    data_quality_level: Optional[int] = FieldInfo(alias="DataQualityLevel", default=None)
    """
    A metric applied during imports to indicate a quality level based on available
    information detail (5 == best). Largely unused currently.
    """

    date_created: Optional[datetime] = FieldInfo(alias="DateCreated", default=None)
    """
    The date and time (UTC, ISO 8601) this POI was added to the Open Charge Map
    database
    """

    date_last_confirmed: Optional[datetime] = FieldInfo(alias="DateLastConfirmed", default=None)
    """
    The date and time (UTC, ISO 8601) this POI was last confirmed according to the
    data provider or a user. See DateLastVerified for a dynamically computed date
    based on multiple signals.
    """

    date_last_status_update: Optional[datetime] = FieldInfo(alias="DateLastStatusUpdate", default=None)
    """
    The date and time (UTC, ISO 8601) this POI or directly related child properties
    were updated.
    """

    date_last_verified: Optional[datetime] = FieldInfo(alias="DateLastVerified", default=None)
    """
    A dynamically computed value, the date and time (UTC, ISO 8601) this POI was
    last confirmed by a user edit or related user comment
    """

    date_planned: Optional[datetime] = FieldInfo(alias="DatePlanned", default=None)
    """The date and time (UTC, ISO 8601) this POI is or was planned for commissioning.

    In general planned POIs should not be presented to end users until confirmed
    operational.
    """

    general_comments: Optional[str] = FieldInfo(alias="GeneralComments", default=None)
    """General additional factual information for the POI.

    Users are discouraged from using this field for opinions on site quality etc.
    """

    id: Optional[int] = FieldInfo(alias="ID", default=None)
    """The OCM reference ID for this POI (Point of Interest)."""

    is_recently_verified: Optional[bool] = FieldInfo(alias="IsRecentlyVerified", default=None)
    """
    A dynamically computed value indicating of any recently confirmation activity
    has taken place for this site (positive check-ins etc)
    """

    media_items: Optional[List[PoiListResponseItemMediaItem]] = FieldInfo(alias="MediaItems", default=None)
    """A list of user submitted photos for this site"""

    metadata_values: Optional[List[object]] = FieldInfo(alias="MetadataValues", default=None)
    """Optional array of metadata values.

    Generally used to indicate data attribution but is also intended for future use
    to indicate surrounding amenties, links or foreign key values into other data
    sets.
    """

    number_of_points: Optional[int] = FieldInfo(alias="NumberOfPoints", default=None)
    """The number of bays or discreet stations available overall at this site.

    This indicates the limiting for number of simultaneous site users.
    """

    operator_id: Optional[int] = FieldInfo(alias="OperatorID", default=None)
    """The reference ID of the equipment network operator or owner"""

    operator_info: Optional[PoiListResponseItemOperatorInfo] = FieldInfo(alias="OperatorInfo", default=None)
    """
    An Operator is the public organisation which controls a network of charging
    points.
    """

    operators_reference: Optional[str] = FieldInfo(alias="OperatorsReference", default=None)
    """
    The network operators own reference for this site (may be a site reference or a
    single equipment reference)
    """

    parent_charge_point_id: Optional[int] = FieldInfo(alias="ParentChargePointID", default=None)
    """If present, this data in this POI supercedes information in another POI.

    Generally not relevant to consumers.
    """

    status_type: Optional[PoiListResponseItemStatusType] = FieldInfo(alias="StatusType", default=None)
    """
    The Status Type of a site or equipment item indicates whether it is generally
    operational.
    """

    status_type_id: Optional[int] = FieldInfo(alias="StatusTypeID", default=None)
    """The overall operational status type reference ID for this POI (i.e.

    Operational etc). 0 == Unknown
    """

    submission_status: Optional[PoiListResponseItemSubmissionStatus] = FieldInfo(alias="SubmissionStatus", default=None)
    """Submission Status object, detailing the POI listing status"""

    submission_status_type_id: Optional[int] = FieldInfo(alias="SubmissionStatusTypeID", default=None)
    """The reference ID for the submission status type which applied to this POI."""

    usage_cost: Optional[str] = FieldInfo(alias="UsageCost", default=None)
    """Free text description of likely usage costs associated with this site.

    Generally relates to parking charges whether network operates this site as Free
    """

    usage_type: Optional[PoiListResponseItemUsageType] = FieldInfo(alias="UsageType", default=None)
    """The Usage Type of a site indicates the general restrictions on usage."""

    usage_type_id: Optional[int] = FieldInfo(alias="UsageTypeID", default=None)
    """The reference ID for the site Usage Type, 0 == Unknown"""

    user_comments: Optional[List[PoiListResponseItemUserComment]] = FieldInfo(alias="UserComments", default=None)
    """A list of user comments or check-ins for this site"""

    uuid: Optional[str] = FieldInfo(alias="UUID", default=None)
    """A universally unique identifier used as surrogate key.

    ID and UUID must be preserved when submitting POI update information.
    """


PoiListResponse: TypeAlias = List[PoiListResponseItem]
