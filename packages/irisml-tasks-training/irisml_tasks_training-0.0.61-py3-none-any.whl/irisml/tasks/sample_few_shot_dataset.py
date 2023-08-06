import collections
import dataclasses
import logging
import random
from typing import Optional
import torch.utils.data
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Few-shot sampling of a IC/OD dataset.

    For n-shot, do random sampling until each category exists in at least n images or all images are sampled.
    """
    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Config:
        n_shot: int
        random_seed: Optional[int] = None

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        few_shot_dataset = FewShotDataset(inputs.dataset, self.config.n_shot, self.config.random_seed)
        return self.Outputs(few_shot_dataset)

    def dry_run(self, inputs):
        return self.execute(inputs)


def _get_class_id_set(targets):
    if not targets.shape:
        return {int(targets)}
    elif len(targets.shape) == 1:
        return set(int(t) for t in targets)
    elif len(targets.shape) == 2:
        return set(int(t[0]) for t in targets)
    raise ValueError(f"Unsupported target type is detected: {targets}")


class FewShotDataset(torch.utils.data.Dataset):
    def __init__(self, dataset, n_shots, random_seed):
        self._dataset = dataset

        if hasattr(dataset, 'get_targets'):
            targets = [dataset.get_targets(i) for i in range(len(dataset))]
        else:
            targets = [t for _, t in dataset]

        classes_by_images = [_get_class_id_set(t) for t in targets]
        classes = set.union(*classes_by_images)
        classes_counter = collections.Counter({c: 0 for c in classes})

        # Random sample until satisfying classes_freq.
        ids = list(range(len(dataset)))
        random.Random(random_seed).shuffle(ids)

        self._id_mappings = []
        for i in ids:
            if min(classes_counter.values()) < n_shots:
                self._id_mappings.append(i)
                classes_counter.update(classes_by_images[i])
            else:
                break

        logger.info(f"Sampled {n_shots}-shot dataset with seed {random_seed}: {len(dataset)} -> {len(self._id_mappings)} samples.")

    def __len__(self):
        return len(self._id_mappings)

    def __getitem__(self, index):
        new_id = self._id_mappings[index]
        assert isinstance(new_id, int)
        return self._dataset[new_id]
