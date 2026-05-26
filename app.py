"""
app.py — The main Streamlit application for SkinGenie.

Run with: streamlit run app.py
"""

import streamlit as st
from src.llm import generate_routine
from src.routine import display_routine
from src.validator import validate_inputs, parse_products

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SkinGenie 🧴",
    page_icon="🧴",
    layout="centered"
)

# ── Header ───────────────────────────────────────────────────────────────────
st.title("🧴 SkinGenie")
st.markdown("*Your AI-powered skincare routine generator*")
st.divider()

# ── Sidebar: How to use ───────────────────────────────────────────────────────
with st.sidebar:
    st.header("How to use")
    st.markdown("""
    1. **List your products** — one per line
    2. **Select your skin type**
    3. **Pick your concerns**
    4. Hit **Generate Routine** ✨
    """)
    st.divider()
    st.caption("Built with Claude AI · Streamlit · Python")

# ── Input Form ────────────────────────────────────────────────────────────────
st.subheader("Step 1: Your Products")
products_raw = st.text_area(
    label="Enter your skincare products (one per line)",
    placeholder="CeraVe Hydrating Cleanser\nThe Ordinary Niacinamide 10%\nCetaphil Moisturizer\nLa Roche-Posay SPF 50",
    height=160,
    help="List every product you own, even if you don't use them all daily."
)

st.subheader("Step 2: Your Skin Profile")
col1, col2 = st.columns(2)

with col1:
    skin_type = st.selectbox(
        "Skin type",
        options=["", "Normal", "Dry", "Oily", "Combination", "Sensitive"],
        index=0,
        help="Select the option that best describes your skin."
    )

with col2:
    concerns = st.multiselect(
        "Skin concerns (select all that apply)",
        options=[
            "Acne / Breakouts",
            "Dark spots / Hyperpigmentation",
            "Dryness / Dehydration",
            "Redness / Sensitivity",
            "Anti-aging / Fine lines",
            "Oiliness / Large pores",
            "Uneven texture",
            "Dark circles",
        ],
        help="Pick everything that applies — more context = better routine."
    )

st.divider()

# ── Generate Button ───────────────────────────────────────────────────────────
generate_btn = st.button("✨ Generate My Routine", type="primary", use_container_width=True)

if generate_btn:
    # Validate inputs
    is_valid, error_msg = validate_inputs(products_raw, skin_type, concerns)

    if not is_valid:
        st.error(error_msg)
    else:
        products = parse_products(products_raw)

        # Show a spinner while Claude works
        with st.spinner("SkinGenie is building your personalized routine... ✨"):
            try:
                routine_data = generate_routine(
                    products=products,
                    skin_type=skin_type,
                    concerns=concerns
                )

                st.success(f"Your routine is ready! Based on {len(products)} products.")
                st.divider()

                # Display the routine
                display_routine(routine_data)

            except ValueError as e:
                st.error(f"Configuration error: {e}")
                st.info("Make sure you've added your ANTHROPIC_API_KEY to your .env file.")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
                st.info("Check your API key and internet connection, then try again.")
