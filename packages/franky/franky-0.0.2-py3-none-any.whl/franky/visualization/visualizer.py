import os.path as osp
import warnings
from typing import Dict, List, Optional, Sequence, Union

import numpy as np
import torch

from franky.config import Config
from franky.dist import master_only
from franky.registry import VISBACKENDS, VISUALIZERS
from franky.structures import BaseDataElement
from franky.utils import ManagerMixin
from franky.visualization.vis_backend import BaseVisBackend


@VISUALIZERS.register_module()
class Visualizer(ManagerMixin):
    def __init__(
            self,
            name='visualizer',
            vis_backends: Optional[List[Dict]] = None,
            save_dir: Optional[str] = None
    ) -> None:
        super().__init__(name)
        self._dataset_meta: Optional[dict] = None
        self._vis_backends: Union[Dict, Dict[str, 'BaseVisBackend']] = dict()

        if save_dir is None:
            warnings.warn('`Visualizer` backend is not initialized '
                          'because save_dir is None.')
        elif vis_backends is not None:
            assert len(vis_backends) > 0, 'empty list'
            names = [
                vis_backend.get('name', None) for vis_backend in vis_backends
            ]
            if None in names:
                if len(set(names)) > 1:
                    raise RuntimeError(
                        'If one of them has a name attribute, '
                        'all backends must use the name attribute')
                else:
                    type_names = [
                        vis_backend['type'] for vis_backend in vis_backends
                    ]
                    if len(set(type_names)) != len(type_names):
                        raise RuntimeError(
                            'The same vis backend cannot exist in '
                            '`vis_backend` config. '
                            'Please specify the name field.')

            if None not in names and len(set(names)) != len(names):
                raise RuntimeError('The name fields cannot be the same')

            save_dir = osp.join(save_dir, 'vis_data')

            for vis_backend in vis_backends:
                name = vis_backend.pop('name', vis_backend['type'])
                vis_backend.setdefault('save_dir', save_dir)
                self._vis_backends[name] = VISBACKENDS.build(vis_backend)

    @property  # type: ignore
    @master_only
    def dataset_meta(self) -> Optional[dict]:
        """Optional[dict]: Meta info of the dataset."""
        return self._dataset_meta

    @dataset_meta.setter  # type: ignore
    @master_only
    def dataset_meta(self, dataset_meta: dict) -> None:
        """Set the dataset meta info to the Visualizer."""
        self._dataset_meta = dataset_meta

    @master_only
    def get_backend(self, name) -> 'BaseVisBackend':
        """get vis backend by name.

        Args:
            name (str): The name of vis backend

        Returns:
             BaseVisBackend: The vis backend.
        """
        return self._vis_backends.get(name)  # type: ignore

    @master_only
    def add_config(self, config: Config, **kwargs):
        """Record the config.

        Args:
            config (Config): The Config object.
        """
        for vis_backend in self._vis_backends.values():
            vis_backend.add_config(config, **kwargs)

    @master_only
    def add_graph(self, model: torch.nn.Module, data_batch: Sequence[dict],
                  **kwargs) -> None:
        """Record the model graph.

        Args:
            model (torch.nn.Module): Model to draw.
            data_batch (Sequence[dict]): Batch of data from dataloader.
        """
        for vis_backend in self._vis_backends.values():
            vis_backend.add_graph(model, data_batch, **kwargs)

    @master_only
    def add_image(self, name: str, image: np.ndarray, step: int = 0) -> None:
        """Record the image.

        Args:
            name (str): The image identifier.
            image (np.ndarray, optional): The image to be saved. The format
                should be RGB. Defaults to None.
            step (int): Global step value to record. Defaults to 0.
        """
        for vis_backend in self._vis_backends.values():
            vis_backend.add_image(name, image, step)  # type: ignore

    @master_only
    def add_scalar(self,
                   name: str,
                   value: Union[int, float],
                   step: int = 0,
                   **kwargs) -> None:
        """Record the scalar data.

        Args:
            name (str): The scalar identifier.
            value (float, int): Value to save.
            step (int): Global step value to record. Defaults to 0.
        """
        for vis_backend in self._vis_backends.values():
            vis_backend.add_scalar(name, value, step, **kwargs)  # type: ignore

    @master_only
    def add_scalars(self,
                    scalar_dict: dict,
                    step: int = 0,
                    file_path: Optional[str] = None,
                    **kwargs) -> None:
        """Record the scalars' data.

        Args:
            scalar_dict (dict): Key-value pair storing the tag and
                corresponding values.
            step (int): Global step value to record. Defaults to 0.
            file_path (str, optional): The scalar's data will be
                saved to the `file_path` file at the same time
                if the `file_path` parameter is specified.
                Defaults to None.
        """
        for vis_backend in self._vis_backends.values():
            vis_backend.add_scalars(scalar_dict, step, file_path, **kwargs)

    @master_only
    def add_datasample(self,
                       name,
                       image: np.ndarray,
                       data_sample: Optional['BaseDataElement'] = None,
                       draw_gt: bool = True,
                       draw_pred: bool = True,
                       show: bool = False,
                       wait_time: int = 0,
                       step: int = 0) -> None:
        """Draw datasample."""
        pass

    def close(self) -> None:
        """close an opened object."""
        for vis_backend in self._vis_backends.values():
            vis_backend.close()

    @classmethod
    def get_instance(cls, name: str, **kwargs) -> 'Visualizer':
        """Make subclass can get latest created instance by
        ``Visualizer.get_current_instance()``.

        Downstream codebase may need to get the latest created instance
        without knowing the specific Visualizer type. For example, mmdetection
        builds visualizer in runner and some component which cannot access
        runner wants to get latest created visualizer. In this case,
        the component does not know which type of visualizer has been built
        and cannot get target instance. Therefore, :class:`Visualizer`
        overrides the :meth:`get_instance` and its subclass will register
        the created instance to :attr:`_instance_dict` additionally.
        :meth:`get_current_instance` will return the latest created subclass
        instance.

        Examples:
            >>> class DetLocalVisualizer(Visualizer):
            >>>     def __init__(self, name):
            >>>         super().__init__(name)
            >>>
            >>> visualizer1 = DetLocalVisualizer.get_instance('name1')
            >>> visualizer2 = Visualizer.get_current_instance()
            >>> visualizer3 = DetLocalVisualizer.get_current_instance()
            >>> assert id(visualizer1) == id(visualizer2) == id(visualizer3)

        Args:
            name (str): Name of instance.

        Returns:
            object: Corresponding name instance.
        """
        instance = super().get_instance(name, **kwargs)
        Visualizer._instance_dict[name] = instance
        return instance
