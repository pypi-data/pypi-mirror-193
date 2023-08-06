# Copyright 2022- Autonomi AI, Inc. All rights reserved.
import os

AUTONOMI_API_URL = "api.autonomi.ai"
AUTONOMI_API_ENDPOINT = os.getenv(
    "AUTONOMI_API_ENDPOINT", f"https://{AUTONOMI_API_URL}/v1"
)

SUPPORTED_VIDEO_FORMATS = (".mp4", ".avi", ".mov")


class StoreMetadata:
    """Column names for the store dataframe."""

    FILE_URL = "file_url"
    """Remote file URL."""
    FILE_ID = "file_id"
    """Unique file identifier."""
    FRAME_ID = "frame_id"
    """Unique video frame identifier."""


class SearchMetadata:
    SCORES = "search_scores"
    """Search relevance score."""
    FEATURES = "search_features"
    """Extracted instance features."""


class DeepTagMetadata:
    """Column names for the deeptag dataframe."""

    LABELS = "pred_labels"
    """Predicted class label."""
    SCORES = "pred_scores"
    """Predicted class score. """
    BOXES = "pred_boxes"
    """Predicted bounding box coords in [0, 1]."""
    BOX_ID = "box_id"
    """Unique bounding box identifier."""
