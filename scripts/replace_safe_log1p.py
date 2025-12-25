#!/usr/bin/env python3
"""Replace any FunctionTransformer.func named 'safe_log1p' with numpy.log1p

Usage: python scripts/replace_safe_log1p.py
"""
from pathlib import Path
import joblib
import numpy as np
import types


def replace_func(obj):
    # If object has attribute 'func', check and replace
    if hasattr(obj, "func"):
        func = getattr(obj, "func")
        if isinstance(func, types.FunctionType) and func.__name__ == "safe_log1p":
            print("Replacing safe_log1p on", obj)
            obj.func = np.log1p
    # Recurse into common containers
    if hasattr(obj, "steps"):
        for name, step in obj.steps:
            replace_func(step)
    if hasattr(obj, "transformers"):
        # ColumnTransformer stores list of (name, transformer, cols)
        for t in obj.transformers:
            if len(t) >= 2:
                replace_func(t[1])
    if hasattr(obj, "estimator"):
        replace_func(obj.estimator)


def main():
    p = Path("outputs/models/preprocess_pipeline.joblib")
    if not p.exists():
        print("preprocess pipeline not found at", p)
        return
    # Ensure safe_log1p is available in __main__ so unpickling can resolve it
    import __main__ as _main
    try:
        import utils
        if not hasattr(_main, "safe_log1p"):
            _main.safe_log1p = utils.safe_log1p
    except Exception:
        pass

    pipeline = joblib.load(p)
    replace_func(pipeline)
    joblib.dump(pipeline, p)
    print("Patched and saved:", p)


if __name__ == "__main__":
    main()
