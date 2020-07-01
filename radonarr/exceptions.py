"""Exceptions for Radonarr."""


class RadonarrError(Exception):
    """Generic Radonarr Exception."""

    pass


class RadonarrConnectionError(RadonarrError):
    """Radonarr connection exception."""

    pass


class RadonarrAccessRestricted(RadonarrError):
    """Radonarr access restricted exception."""

    pass


class RadonarrResourceNotFound(RadonarrError):
    """Radonarr resource not found exception."""

    pass


"""Exceptions for Sonarr."""


class SonarrError(Exception):
    """Generic Sonarr Exception."""

    pass


class SonarrConnectionError(SonarrError):
    """Sonarr connection exception."""

    pass


class SonarrAccessRestricted(SonarrError):
    """Sonarr access restricted exception."""

    pass


class SonarrResourceNotFound(SonarrError):
    """Sonarr resource not found exception."""

    pass


"""Exceptions for Radarr."""


class RadarrError(Exception):
    """Generic Radarr Exception."""

    pass


class RadarrConnectionError(RadarrError):
    """Radarr connection exception."""

    pass


class RadarrAccessRestricted(RadarrError):
    """Radarr access restricted exception."""

    pass


class RadarrResourceNotFound(RadarrError):
    """Radarr resource not found exception."""

    pass
