from .constants import COMMENT_TEXT_LABEL, TARGET_LABELS


def get_data_and_targets(data):
    return data[COMMENT_TEXT_LABEL], data[TARGET_LABELS].values
