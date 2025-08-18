import requests
import json
import streamlit as st
from _utils import _load_config

ui_cfg: dict = _load_config("ui/configs/ui_config.yaml")
home_cfg: dict = ui_cfg.get("home_page", {})

st.title(home_cfg.get("title", "Numerical Methods and Scientific Computing"))
st.divider()
st.subheader(
    "Calculate the numerical integration of various functions using different methods"
)

with st.form("integration_computation_form"):
    method_str = st.selectbox(label="Method", options=home_cfg.get("methods"))
    function = st.text_input(
        label="Function",
    )
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input(label="a", value=0.0)
    with col2:
        b = st.number_input(label="b", value=1.0)
    grid_pts = st.number_input(label="Grid points", value=50, min_value=2, step=1)
    req_time = st.checkbox("Display required time")

    submitted = st.form_submit_button("Submit", width="stretch")

    if submitted:
        with st.spinner(text="Calculating...", show_time=True):
            body = {
                "method": method_str,
                "f": function,
                "a": a,
                "b": b,
                "grid_pts": grid_pts,
                "req_time": req_time,
            }
            json_body = json.dumps(body)
            response = requests.post(
                url=home_cfg.get("integration_calc_backend_url"), data=json_body
            )

        if response.ok:
            res = response.json()
            st.text(f"Integration value:   {res.get("integral")}")
            if req_time:
                st.text(f"Computation time:  {res.get("req_time")}")
        else:
            try:
                # If backend sends structured error JSON
                error_msg = response.json().get("detail", response.text)
            except Exception:
                # Fallback if it's just plain text
                error_msg = response.text

            st.error(f"Integration failed: {error_msg}")
