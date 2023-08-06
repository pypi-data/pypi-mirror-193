# encoding: utf-8



# file: base_model.py
# time: 1:43 

import json
import os
import pathlib
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Dict, Union

import tensorflow as tf

import kolibri
from kolibri.backend.tensorflow.embeddings import BaseEmbedding
from kolibri.backend.tensorflow.layers import KConditionalRandomField
from kolibri.backend.tensorflow.logger import logger
from kolibri.indexers.base_indexer import BaseIndexer

if TYPE_CHECKING:
    from kolibri.backend.tensorflow.tasks.text.classification import BaseTextClassificationModel
    from kolibri.backend.tensorflow.tasks.text.labeling import BaseLabelingModel


class TaskBaseModel(ABC):

    def __init__(self) -> None:
        self.tf_model: tf.keras.Model = None
        self.embedding: BaseEmbedding = None
        self.hyper_parameters: Dict[str, Any]
        self.sequence_length: int
        self.text_processor: BaseIndexer
        self.label_processor: BaseIndexer

    def to_dict(self) -> Dict[str, Any]:
        model_json_str = self.tf_model.to_json()

        return {
            'tf_version': tf.__version__,  # type: ignore
            'kolibri_version': kolibri.backend.tensorflow.__version__,
            '__class_name__': self.__class__.__name__,
            '__module__': self.__class__.__module__,
            'config': {
                'hyper_parameters': self.hyper_parameters,  # type: ignore
                'sequence_length': self.sequence_length  # type: ignore
            },
            'embedding': self.embedding.to_dict(),  # type: ignore
            'text_processor': self.text_processor.to_dict(),
            'label_indexer': self.label_indexer.to_dict(),
            'tf_model': json.loads(model_json_str)
        }

    @classmethod
    def default_hyper_parameters(cls) -> Dict[str, Dict[str, Any]]:
        """
        The default hyper parameters of the model dict, **all models must implement this function.**

        You could easily change model's hyper-parameters.

        For example, change the LSTM unit in BiLSTM_Model from 128 to 32.

            >>> from kolibri.backend.tensorflow.tasks.classification import BiLSTM_Model
            >>> hyper = BiLSTM_Model.default_hyper_parameters()
            >>> print(hyper)
            {'layer_bi_lstm': {'units': 128, 'return_sequences': False}, 'layer_output': {}}
            >>> hyper['layer_bi_lstm']['units'] = 32
            >>> model = BiLSTM_Model(hyper_parameters=hyper)

        Returns:
            hyper params dict
        """
        raise NotImplementedError

    def save(self, model_path: str, encoding: str = 'utf-8') -> str:
        pathlib.Path(model_path).mkdir(exist_ok=True, parents=True)
        model_path = os.path.abspath(model_path)

        with open(os.path.join(model_path, 'model_config.json'), 'w', encoding=encoding) as f:
            f.write(json.dumps(self.to_dict(), indent=2, ensure_ascii=False))
            f.close()

        self.embedding.embed_model.save_weights(os.path.join(model_path, 'embed_model_weights.h5'))
        self.tf_model.save_weights(os.path.join(model_path, 'model_weights.h5'))  # type: ignore
        logger.info('model saved to {}'.format(os.path.abspath(model_path)))
        return model_path

    @classmethod
    def load_model(cls, model_path: str,
                   custom_objects: Dict = None,
                   encoding: str = 'utf-8') -> Union["BaseLabelingModel", "BaseTextClassificationModel"]:
        from kolibri.backend.tensorflow.utils import load_data_object
        if custom_objects is None:
            custom_objects = {}

        if cls.__name__ not in custom_objects:
            custom_objects[cls.__name__] = cls

        model_config_path = os.path.join(model_path, 'model_config.json')
        model_config = json.loads(open(model_config_path, 'r', encoding=encoding).read())
        model = load_data_object(model_config, custom_objects)

        model.embedding = load_data_object(model_config['embedding'], custom_objects)
        model.text_processor = load_data_object(model_config['text_processor'], custom_objects)
        model.label_indexer = load_data_object(model_config['label_indexer'], custom_objects)

        tf_model_str = json.dumps(model_config['tf_model'])

        model.tf_model = tf.keras.models.model_from_json(tf_model_str,
                                                         custom_objects=kolibri.backend.tensorflow.custom_objects)

        if isinstance(model.tf_model.layers[-1], KConditionalRandomField):
            model.crf_layer = model.tf_model.layers[-1]

        model.tf_model.load_weights(os.path.join(model_path, 'model_weights.h5'))
        model.embedding.embed_model.load_weights(os.path.join(model_path, 'embed_model_weights.h5'))
        return model

    @abstractmethod
    def build_model(self,
                    x_data: Any,
                    y_data: Any) -> None:
        raise NotImplementedError
