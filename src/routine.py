"""
routine.py — Handles formatting and displaying the routine in Streamlit.

Separates display logic from AI logic — a good software engineering habit.
"""

import streamlit as st

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EMOJIS = {
    "monday": "🌅", "tuesday": "🌤️", "wednesday": "⛅",
    "thursday": "🌦️", "friday": "✨", "saturday": "🌸", "sunday": "🛁"
}


def display_routine(routine_data: dict):
    """Render the full weekly routine in a clean Streamlit layout."""

    routine = routine_data.get("routine", {})
    tips = routine_data.get("tips", [])
    warnings = routine_data.get("warnings", [])

    # Show warnings at the top if any exist
    if warnings:
        st.subheader("⚠️ Ingredient Warnings")
        for warning in warnings:
            st.warning(warning)

    st.subheader("📅 Your Weekly Routine")

    # Display each day in two columns (AM | PM)
    for day in DAYS:
        if day not in routine:
            continue

        emoji = DAY_EMOJIS.get(day, "📆")
        st.markdown(f"### {emoji} {day.capitalize()}")

        col_am, col_pm = st.columns(2)

        with col_am:
            st.markdown("**☀️ Morning (AM)**")
            am_steps = routine[day].get("am", [])
            for i, step in enumerate(am_steps, 1):
                st.markdown(f"{i}. {step}")

        with col_pm:
            st.markdown("**🌙 Evening (PM)**")
            pm_steps = routine[day].get("pm", [])
            for i, step in enumerate(pm_steps, 1):
                st.markdown(f"{i}. {step}")

        st.divider()

    # Show pro tips
    if tips:
        st.subheader("💡 Pro Tips")
        for tip in tips:
            st.info(tip)
