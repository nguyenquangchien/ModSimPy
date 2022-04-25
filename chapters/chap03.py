from modsim import *

def step(state, p1, p2):
    """Mô phỏng 1 bước thời gian.
    
    state: đối tượng State chỉ trạng thái dùng chung xe
    p1: xác suất có xe theo hướng Olin->Wellesley
    p2: xác suất có xe theo hướng Wellesley->Olin
    """
    if flip(p1):
        bike_to_wellesley(state)
    
    if flip(p2):
        bike_to_olin(state)

from modsim import *

def bike_to_olin(state):
    """Di chuyển một xe từ Wellesley đến Olin.
    
    state: đối tượng State chỉ trạng thái dùng chung xe
    """
    if state.wellesley == 0:
        state.wellesley_empty += 1
        return
    state.wellesley -= 1
    state.olin += 1

from modsim import *

# Lời giải

def bike_to_wellesley(state):
    """Di chuyển một xe từ Olin đến Wellesley.
    
    state: đối tượng State chỉ trạng thái dùng chung xe
    """
    if state.olin == 0:
        state.olin_empty += 1
        return
    state.olin -= 1
    state.wellesley += 1

