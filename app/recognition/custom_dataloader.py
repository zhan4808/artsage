import os
import requests
import hashlib
from PIL import Image
from torch.utils.data import Dataset

class MetDataset(Dataset):
    def __init__(self, annotations, cache_dir="image_cache"):
        self.annotations = annotations
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        row = self.annotations.iloc[idx]
        img_path = self._fetch_image(row["primaryImage"])
        # Include other annotations like bounding boxes, categories if available
        return {
            "image": img_path,
            "label": row.get("objectName", "unknown"),
            "metadata": row.to_dict(),
        }

    def _fetch_image(self, url):
        hash_name = hashlib.md5(url.encode()).hexdigest()
        file_path = os.path.join(self.cache_dir, hash_name + ".jpg")
        if not os.path.exists(file_path):
            response = requests.get(url)
            if response.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(response.content)
        return file_path