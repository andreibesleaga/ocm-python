# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .country import Country
from .._models import BaseModel

__all__ = [
    "ReferencedataRetrieveResponse",
    "ChargerType",
    "CheckinStatusType",
    "ConnectionType",
    "CurrentType",
    "DataProvider",
    "DataProviderDataProviderStatusType",
    "Operator",
    "OperatorAddressInfo",
    "StatusType",
    "SubmissionStatusType",
    "UsageType",
    "UserCommentType",
]


class ChargerType(BaseModel):
    """A general category for equipment power capability.

    Deprecated for general use. Currently computed automatically based on equipment power.
    """

    comments: str = FieldInfo(alias="Comments")

    id: int = FieldInfo(alias="ID")

    is_fast_charge_capable: bool = FieldInfo(alias="IsFastChargeCapable")
    """If true, this level is considered 'fast' charging, relative to other levels."""

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class CheckinStatusType(BaseModel):
    """
    Classification for the users comment or experience using a specific charging location.
    """

    id: int = FieldInfo(alias="ID")

    is_automated_checkin: bool = FieldInfo(alias="IsAutomatedCheckin")
    """If true, checkin or comment was provided by an automated system."""

    is_positive: Optional[bool] = FieldInfo(alias="IsPositive", default=None)
    """If true, this type of checkin/comment is considered positive."""

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class ConnectionType(BaseModel):
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


class CurrentType(BaseModel):
    """Indicates the EVSE power supply type e.g.

    DC (Direct Current), AC (Single Phase), AC (3 Phase).
    """

    id: int = FieldInfo(alias="ID")

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class DataProviderDataProviderStatusType(BaseModel):
    """
    Status object describing whether this data provider is currently enabled and the type of source (manual entry, imported etc)
    """

    id: int = FieldInfo(alias="ID")
    """The reference ID for this provider status type"""

    is_provider_enabled: bool = FieldInfo(alias="IsProviderEnabled")
    """If false, results from this data provider are not currently enabled"""

    description: Optional[str] = None
    """The Title of this status type"""


class DataProvider(BaseModel):
    """
    A Data Provider is the controller of the source data set used to construct the details for this POI. Data has been transformed and interpreted from it's original form. Each Data Provider provides data either by an explicit license or agreement.
    """

    id: int = FieldInfo(alias="ID")
    """The reference ID for this Data Provider"""

    is_restricted_edit: bool = FieldInfo(alias="IsRestrictedEdit")
    """Currently not implemented. Indicates a potential editing restriction."""

    comments: Optional[str] = FieldInfo(alias="Comments", default=None)
    """General public comments with information about this Data Provider."""

    data_provider_status_type: Optional[DataProviderDataProviderStatusType] = FieldInfo(
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


class OperatorAddressInfo(BaseModel):
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


class Operator(BaseModel):
    """
    An Operator is the public organisation which controls a network of charging points.
    """

    id: int = FieldInfo(alias="ID")
    """Id"""

    address_info: Optional[OperatorAddressInfo] = FieldInfo(alias="AddressInfo", default=None)
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


class StatusType(BaseModel):
    """
    The Status Type of a site or equipment item indicates whether it is generally operational.
    """

    id: int = FieldInfo(alias="ID")

    is_operational: bool = FieldInfo(alias="IsOperational")

    is_user_selectable: bool = FieldInfo(alias="IsUserSelectable")

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class SubmissionStatusType(BaseModel):
    """Submission Status object, detailing the POI listing status"""

    id: int = FieldInfo(alias="ID")
    """Submission Status Type reference ID"""

    is_live: bool = FieldInfo(alias="IsLive")
    """If true, POI listing is live (not draft or de-listed)"""

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class UsageType(BaseModel):
    """The Usage Type of a site indicates the general restrictions on usage."""

    id: int = FieldInfo(alias="ID")

    is_access_key_required: bool = FieldInfo(alias="IsAccessKeyRequired")
    """If true this usage required a physical access key"""

    is_membership_required: bool = FieldInfo(alias="IsMembershipRequired")
    """If true, this usage type requires registration or membership with a service."""

    is_pay_at_location: bool = FieldInfo(alias="IsPayAtLocation")
    """If true, usage requires paying at location"""

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class UserCommentType(BaseModel):
    """Category for a user comment, e.g.

    General Comment, Fault Report (Notice To Users And Operator)
    """

    id: Optional[int] = FieldInfo(alias="ID", default=None)

    title: Optional[str] = FieldInfo(alias="Title", default=None)


class ReferencedataRetrieveResponse(BaseModel):
    """Set of core reference data used for other API results and UI"""

    charger_types: Optional[List[ChargerType]] = FieldInfo(alias="ChargerTypes", default=None)

    checkin_status_types: Optional[List[CheckinStatusType]] = FieldInfo(alias="CheckinStatusTypes", default=None)

    connection_types: Optional[List[ConnectionType]] = FieldInfo(alias="ConnectionTypes", default=None)

    countries: Optional[List[Country]] = FieldInfo(alias="Countries", default=None)

    current_types: Optional[List[CurrentType]] = FieldInfo(alias="CurrentTypes", default=None)

    data_providers: Optional[List[DataProvider]] = FieldInfo(alias="DataProviders", default=None)

    data_types: Optional[object] = FieldInfo(alias="DataTypes", default=None)

    metadata_groups: Optional[str] = FieldInfo(alias="MetadataGroups", default=None)

    operators: Optional[List[Operator]] = FieldInfo(alias="Operators", default=None)

    status_types: Optional[List[StatusType]] = FieldInfo(alias="StatusTypes", default=None)

    submission_status_types: Optional[List[SubmissionStatusType]] = FieldInfo(
        alias="SubmissionStatusTypes", default=None
    )

    usage_types: Optional[List[UsageType]] = FieldInfo(alias="UsageTypes", default=None)

    user_comment_types: Optional[List[UserCommentType]] = FieldInfo(alias="UserCommentTypes", default=None)
