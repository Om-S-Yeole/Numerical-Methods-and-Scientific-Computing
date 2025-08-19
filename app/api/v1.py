from typing import Callable
from fastapi import APIRouter, HTTPException
from nmsc._utils._helpers import _methods_dict
from nmsc._utils._helpers import _str_to_sympy_convertor
from app.utils import IntegrationInputs, RombergIntegrationInputs

router = APIRouter()


@router.post("/integrate")
def integrate(body: IntegrationInputs | RombergIntegrationInputs):
    body: dict = body.model_dump()
    method = _methods_dict[body.pop("method")]

    try:
        func: Callable[[float], float] = _str_to_sympy_convertor(body.get("f"))
    except (TypeError, ValueError) as e:
        raise HTTPException(status_code=400, detail=f"{e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")

    body["f"] = func
    req_time = body.pop("req_time")

    try:
        results: dict = method(**body)._asdict()
    except (TypeError, ValueError) as e:
        raise HTTPException(status_code=400, detail=f"{e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")

    if req_time:
        return results
    else:
        _ = results.pop("req_time")
        return results
