from detectron2.data.datasets import register_coco_instances

def register_met_datasets():
    """
    Register the Met dataset in COCO format.
    """
    register_coco_instances(
        "met_train", {}, "app/recognition/configs/train.json", "image_cache"
    )
    register_coco_instances(
        "met_val", {}, "app/recognition/configs/val.json", "image_cache"
    )