import altair as alt
import pandas as pd
import streamlit as st

from commons.enum import level_mapping
from frontend.services.course import CourseService
from frontend.services.employee_competency import EmployeeCompetencyService
from frontend.services.feedback import FeedbackService


def employee_view():
    # Verificar si la configuración está completa

    if not st.session_state.get("employee", False):
        st.error("Select the employee before continue")
        st.stop()
    else:
        employee_id = st.session_state.employee.id
        employee_name = st.session_state.employee.name
    st.title(f"{employee_name}")
    st.write(f"{st.session_state.department.name}")

    feedback_service = FeedbackService()
    employee_competency_service = EmployeeCompetencyService()
    course_service = CourseService()
    employee_competencies = employee_competency_service.get_all_by_employee(employee_id)
    df = pd.DataFrame([d.model_dump() for d in employee_competencies])
    df["level_value"] = df["current_level"].map(level_mapping)
    chart = (
        alt.Chart(df)
        .mark_circle(size=150)
        .encode(
            x=alt.X("level_value:Q", sort="-y", axis=alt.Axis(title="", tickCount=4), scale=alt.Scale(domain=[0, 3])),
            y=alt.Y("name:N", title=""),
            color=alt.Color(
                "current_level:N",
                scale=alt.Scale(
                    domain=["basic", "intermediate", "advanced", "expert"],
                    range=["#f94144", "#f9c74f", "#90be6d", "#577590"],
                ),
            ),
            tooltip=["name", "current_level"],
        )
        .properties(width=600, height=300)
    )

    feedbacks = feedback_service.get_all_by_employee(employee_id)
    df_feedback = pd.DataFrame([d.model_dump() for d in feedbacks])
    if "priority_data" not in st.session_state:
        st.session_state["priority_data"] = []
    tab1, tab2 = st.tabs(["Employee View", "Course Recommender"])
    with tab1:
        cols = st.columns(2)
        with cols[0].container(height=400):
            st.subheader("Competencies")
            st.altair_chart(chart, use_container_width=True)

        with cols[1].container(height=400):
            for _, row in df_feedback.iterrows():
                st.markdown(f"**Date**: {row["effective_date"]}")
                st.markdown(f"**Score**: {row["score"]}")
                st.markdown(f"{row["comments"]}")
                st.write("---")

    with tab2:

        with st.spinner("Getting course recomendations"):
            matching_courses = course_service.recommend_course(employee_id)
            courses = matching_courses.courses
        with st.container(height=200):
            st.markdown("**Competencies needed to improve**")
            for priority in matching_courses.priority:
                st.markdown(f"**{priority.matching_competencies}** priority {priority.priority}")
        with st.container(height=1000):
            for course in courses:
                st.markdown(f"## {course.title}")
                st.markdown(f"{round(course.rating, 2)}★     {course.number_of_viewers}👁")
                st.markdown(f"{course.matching_competencies.replace(","," | ")}")
                st.markdown(course.short_intro)
                st.markdown(f"[URL]({course.url})")
                st.write("---")
