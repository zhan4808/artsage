import torch
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog

def load_model():
    cfg = get_cfg()
    cfg.merge_from_file("path/to/your/config.yaml")
    cfg.MODEL.WEIGHTS = "path/to/your/model.pth"
    predictor = DefaultPredictor(cfg)
    return predictor

def recognize_painting(image_path, predictor):
    from detectron2.utils.visualizer import Visualizer
    from PIL import Image

    image = cv2.imread(image_path)
    outputs = predictor(image)
    return outputs