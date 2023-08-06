import yaml


__all__ = ["EventMunetLoadingOptions"]


class EventMunetLoadingOptions(yaml.YAMLObject):
    """Options for loading an event_munet.csv file or alike.

    Parameters
    ----------
    mode_before : {'pass', 'theoretical', 'system'}
        Mode for selecting before images. Value 'pass' means fields 'before_image_id' must exist
        and will be used as-is. Value 'theoretical' means field 'theoretical_before_image_id' must
        exist and will be used. Value 'system' means both fields 'system_before_image_id' and
        'theoretical_before_image_id' must exist and they will be combined with higher priority on
        the system images to fill in field 'before_image_id'. Field 'before_image_valid' will be
        treated similarly in any mode, if it and its variants exist.
    mode_after : {'pass', 'theoretical', 'system', 'system_only'}
        Mode for selecting after images. Value 'pass' means fields 'after_image_id' must exist and
        will be used as-is. Value 'theoretical' means field 'theoretical_after_image_id' must exist
        and will be used. Value 'system' means both fields 'system_after_image_id' and
        'theoretical_after_image_id' must exist and they will be combined with higher priority on
        the system images to fill in field 'after_image_id'. Value 'system_only' means only field
        'system_after_image_id' is used.
    """

    yaml_tag = "!EventMunetLoadingOptions"

    def __init__(
        self,
        mode_before: str = "pass",
        mode_after: str = "pass",
    ):
        self.mode_before = mode_before
        self.mode_after = mode_after

    def __repr__(self):

        return "%s(mode_before=%r, mode_after=%r)" % (
            self.__class__.__name__,
            self.mode_before,
            self.mode_after,
        )
