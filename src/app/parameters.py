from enum import Enum
from tensorflow.python.keras.layers import LSTM, GRU, CuDNNLSTM, CuDNNGRU
from tensorflow.python.client import device_lib

class Dataset (Enum):
    CRYPTO = "CRYPTO"
    WEATHER = "WEATHER"

class Symbol (Enum):
    BTC_USDT = "BTC-USDT"
    BCH_BTC = "BCH-BTC"
    ETH_BTC = "ETH-BTC"
    LTC_BTC = "LTC-BTC"
    DASH_BTC = "DASH-BTC"
    DOGE_BTC = "DOGE-BTC"
    XRP_BTC = "XRP-BTC" # Ripple
    XMR_BTC = "XMR-BTC" # Monero


## CuDNNN / GPU versions are applied automatically
class Model (Enum):
    LSTM = LSTM
    GRU = GRU


### SEQ INFO
DATASET = Dataset.WEATHER.value
MAX_DATASET_SIZE = 100000 # Dataset has over 1 mil values, so we limit to last x values
SYMBOL_TO_PREDICT = Symbol.BTC_USDT.value # The current symbol to train the model to base predictions on
FUTURE_PERIOD = 25 # The look forward period for the future column, used to train the neural network to predict future price
SEQUENCE_LEN = 120 # The look back period aka the sequence length. e.g if this is 100, the last 100 prices will be used to predict future price

EPOCHS = 100 # Epochs per training fold (we are doing 10 fold cross validation)
BATCH_SIZE = 2048

## MODEL INFO
HIDDEN_LAYERS = 4
NEURONS_PER_LAYER = 64
MODEL = Model.GRU.value
DROPOUT = 0.0


## Utilise GPU if GPU is available
local_devices = device_lib.list_local_devices()
gpus = [x.name for x in local_devices if x.device_type == 'GPU']
if len(gpus) != 0:
    if MODEL == GRU:
        MODEL = CuDNNGRU
    elif MODEL == LSTM:
        MODEL = CuDNNLSTM