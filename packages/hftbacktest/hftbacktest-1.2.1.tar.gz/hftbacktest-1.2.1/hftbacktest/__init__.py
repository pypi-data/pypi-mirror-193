import numpy as np
import pandas as pd

from .latencies import ConstantLatency, FeedLatency
from .assettype import Linear, Inverse
from .queue import RiskAverseQueueModel, LogProbQueueModel, IdentityProbQueueModel, SquareProbQueueModel
from .backtest import COL_EVENT, COL_EXCH_TIMESTAMP, COL_LOCAL_TIMESTAMP, COL_SIDE, COL_PRICE, COL_QTY, \
    DEPTH_EVENT, DEPTH_CLEAR_EVENT, DEPTH_SNAPSHOT_EVENT, TRADE_EVENT, BUY, SELL, NONE, NEW, EXPIRED, FILLED, CANCELED, \
    GTC, GTX, Order, \
    HftBacktest as _HftBacktest, hbt_cls_spec, DataReader, DataBinder
from .stat import Stat
from .data import validate_data, correct_local_timestamp, correct_exch_timestamp, correct
from numba.experimental import jitclass

__all__ = ('COL_EVENT', 'COL_EXCH_TIMESTAMP', 'COL_LOCAL_TIMESTAMP', 'COL_SIDE', 'COL_PRICE', 'COL_QTY',
           'DEPTH_EVENT', 'TRADE_EVENT', 'DEPTH_CLEAR_EVENT', 'DEPTH_SNAPSHOT_EVENT', 'BUY', 'SELL',
           'NONE', 'NEW', 'EXPIRED', 'FILLED', 'CANCELED', 'GTC', 'GTX',
           'Order', 'HftBacktest',
           'FeedLatency', 'ConstantLatency',
           'Linear', 'Inverse',
           'RiskAverseQueueModel', 'LogProbQueueModel', 'IdentityProbQueueModel', 'SquareProbQueueModel',
           'Stat',
           'validate_data', 'correct_local_timestamp', 'correct_exch_timestamp', 'correct')

__version__ = '1.2.1'


def HftBacktest(data, tick_size, lot_size, maker_fee, taker_fee, order_latency, asset_type, queue_model=None,
                snapshot=None, start_row=0, start_position=0, start_balance=0, start_fee=0, trade_list_size=0):
    if isinstance(data, pd.DataFrame):
        assert (data.columns[:6] == ['event', 'exch_timestamp', 'local_timestamp', 'side', 'price', 'qty']).all()
        reader = DataBinder(data.to_numpy())
    elif isinstance(data, np.ndarray):
        assert data.shape[1] >= 6
        reader = DataBinder(data)
    elif isinstance(data, list):
        reader = DataReader()
        for filepath in data:
            assert isinstance(filepath, str)
            reader.add_file(filepath)
    else:
        raise ValueError('Unsupported data type')
    if queue_model is None:
        queue_model = RiskAverseQueueModel()
    spec = hbt_cls_spec + [
        ('order_latency', order_latency._numba_type_),
        ('asset_type', asset_type._numba_type_),
        ('queue_model', queue_model._numba_type_),
        ('data_reader', reader._numba_type_),
    ]
    hbt = jitclass(spec=spec)(_HftBacktest)
    # hbt = _HftBacktest

    return hbt(reader, tick_size, lot_size, maker_fee, taker_fee, order_latency, asset_type, queue_model,
               snapshot.values if snapshot is not None else None,
               start_row, start_position, start_balance, start_fee, trade_list_size)
