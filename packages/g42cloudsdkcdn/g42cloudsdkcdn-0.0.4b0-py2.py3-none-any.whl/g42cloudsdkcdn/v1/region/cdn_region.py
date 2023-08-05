# coding: utf-8

import types
import six

from g42cloudsdkcore.region.region import Region
from g42cloudsdkcore.region.provider import RegionProviderChain

class CdnRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CDN")

    CN_NORTH_1 = Region("cn-north-1",
                        "https://cdn.myg42cloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://cdn.myg42cloud.com")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
        "ap-southeast-1": AP_SOUTHEAST_1,
    }

    @classmethod
    def value_of(cls, region_id, static_fields=None):
        if not region_id:
            raise KeyError("Unexpected empty parameter: region_id.")

        fields = static_fields if static_fields else cls.static_fields

        region = cls._PROVIDER.get_region(region_id)
        if region:
            return region

        if region_id in fields:
            return fields.get(region_id)

        raise KeyError("Unexpected region_id: " + region_id)


