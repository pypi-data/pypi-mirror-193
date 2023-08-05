# encoding: utf-8



# file: __init__.py
# time: 4:05 

from .base_model import BaseTextClassificationModel
from .bigru_model import BiGRU_Model
from .bilstm_model import BiLSTM_Model
from .cnn_attention_model import CNN_Attention_Model
from .cnn_gru_model import CNN_GRU_Model
from .cnn_lstm_model import CNN_LSTM_Model
from .cnn_model import CNN_Model

ALL_MODELS = [
    BiGRU_Model,
    BiLSTM_Model,
    CNN_Attention_Model,
    CNN_GRU_Model,
    CNN_LSTM_Model,
    CNN_Model
]

if __name__ == "__main__":
    pass
