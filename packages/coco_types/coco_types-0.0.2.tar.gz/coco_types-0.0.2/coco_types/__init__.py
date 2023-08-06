__version__ = "0.0.2"

import coco_types.coco_dict_types as dict_types  # pyright: ignore[reportUnusedImport]

from .coco_keypoints import AnnotationKP, CategoryKP, DatasetKP
from .coco_object_detection import (Annotation, BaseModel, Category, Dataset, EncodedRLE, Image, Info, Licence, RLE,
                                    TPolygon_segmentation)

__all__ = ["Annotation", "Licence", "BaseModel", "Category", "Dataset", "EncodedRLE", "Image", "RLE", "Info",
           "TPolygon_segmentation",
           "AnnotationKP", "CategoryKP", "DatasetKP"]
