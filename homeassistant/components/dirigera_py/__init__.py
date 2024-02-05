"""The Ikea Dirigera Python integration."""
from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

# pylint: disable-all
# TO DO List the platforms that you want to support. # pylint: disable=W0511
# For your initial PR, limit it to 1 platform.
PLATFORMS: list[Platform] = [Platform.LIGHT]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Ikea Dirigera Python from a config entry."""

    hass.data.setdefault(DOMAIN, {})
    # TO DO 1. Create API instance # pylint: disable=W0511
    # TO DO 2. Validate the API connection (and authentication) # pylint: disable=W0511
    # TO DO 3. Store an API object for your platforms to access # pylint: disable=W0511
    # hass.data[DOMAIN][entry.entry_id] = MyApi(...)

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
