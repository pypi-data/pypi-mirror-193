from autoai_libs.transformers.exportable import NumpyColumnSelector
from autoai_libs.transformers.exportable import CompressStrings
from autoai_libs.transformers.exportable import NumpyReplaceMissingValues
from autoai_libs.transformers.exportable import NumpyReplaceUnknownValues
from autoai_libs.transformers.exportable import boolean2float
from autoai_libs.transformers.exportable import CatImputer
from autoai_libs.transformers.exportable import CatEncoder
import numpy as np
from autoai_libs.transformers.exportable import float32_transform
from autoai_libs.transformers.exportable import FloatStr2Float
from autoai_libs.transformers.exportable import NumImputer
from autoai_libs.transformers.exportable import OptStandardScaler
from lale.lib.lale import ConcatFeatures
from autoai_libs.transformers.exportable import NumpyPermuteArray
from xgboost import XGBRegressor
import lale

lale.wrap_imported_operators()
numpy_column_selector_0 = NumpyColumnSelector(columns=[0, 1, 3, 4, 5])
compress_strings = CompressStrings(
    compress_type="hash",
    dtypes_list=["int_num", "char_str", "int_num", "char_str", "char_str"],
    missing_values_reference_list=["", "-", "?", float("nan")],
    misslist_list=[[], [], [], [], []],
)
numpy_replace_missing_values_0 = NumpyReplaceMissingValues(
    missing_values=[], filling_values=float("nan")
)
numpy_replace_unknown_values = NumpyReplaceUnknownValues(
    filling_values=float("nan"),
    filling_values_list=[
        float("nan"), float("nan"), float("nan"), float("nan"), float("nan"),
    ],
    missing_values_reference_list=["", "-", "?", float("nan")],
)
cat_imputer = CatImputer(
    strategy="most_frequent",
    missing_values=float("nan"),
    sklearn_version_family="23",
)
cat_encoder = CatEncoder(
    encoding="ordinal",
    categories="auto",
    dtype=np.float64,
    handle_unknown="error",
    sklearn_version_family="23",
)
numpy_column_selector_1 = NumpyColumnSelector(columns=[2])
float_str2_float = FloatStr2Float(
    dtypes_list=["float_num"], missing_values_reference_list=[]
)
numpy_replace_missing_values_1 = NumpyReplaceMissingValues(
    missing_values=[], filling_values=float("nan")
)
num_imputer = NumImputer(strategy="median", missing_values=float("nan"))
opt_standard_scaler = OptStandardScaler(
    num_scaler_copy=None,
    num_scaler_with_mean=None,
    num_scaler_with_std=None,
    use_scaler_flag=False,
)
numpy_permute_array = NumpyPermuteArray(
    axis=0, permutation_indices=[0, 1, 3, 4, 5, 2]
)
xgb_regressor = XGBRegressor(
    base_score=0.5,
    booster="gbtree",
    colsample_bylevel=1,
    colsample_bynode=1,
    colsample_bytree=1,
    gamma=0,
    gpu_id=-1,
    interaction_constraints="",
    learning_rate=0.300000012,
    max_delta_step=0,
    max_depth=3,
    min_child_weight=1,
    missing=float("nan"),
    monotone_constraints="()",
    n_estimators=100,
    num_parallel_tree=1,
    random_state=33,
    reg_alpha=0,
    reg_lambda=1,
    scale_pos_weight=1,
    subsample=1,
    tree_method="exact",
    validate_parameters=1,
    verbosity=0,
    silent=False,
    nthread=1,
    seed=33,
)
pipeline = (
    (
        (
            numpy_column_selector_0
            >> compress_strings
            >> numpy_replace_missing_values_0
            >> numpy_replace_unknown_values
            >> boolean2float()
            >> cat_imputer
            >> cat_encoder
            >> float32_transform()
        )
        & (
            numpy_column_selector_1
            >> float_str2_float
            >> numpy_replace_missing_values_1
            >> num_imputer
            >> opt_standard_scaler
            >> float32_transform()
        )
    )
    >> ConcatFeatures()
    >> numpy_permute_array
    >> xgb_regressor
)