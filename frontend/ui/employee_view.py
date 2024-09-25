import altair as alt
import pandas as pd
import streamlit as st

from commons.enum import level_mapping
from frontend.services.course import CourseService
from frontend.services.employee_competency import EmployeeCompetencyService
from frontend.services.feedback import FeedbackService


def employee_view():
    # Verificar si la configuración está completa
    if not st.session_state.get("config_done", False):
        st.error("First you have to configure all the data")
        st.stop()

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
    chart = alt.Chart(df).mark_circle(size=150).encode(
            x=alt.X("level_value:Q", sort="-y", axis=alt.Axis(title="Competency Level", tickCount=4), scale=alt.Scale(domain=[0, 3])),
            y=alt.Y("name:N", title="Competency"),
            color=alt.Color("current_level:N", scale=alt.Scale(domain=["basic", "intermediate", "advanced", "expert"],
                                                    range=["#f94144", "#f9c74f", "#90be6d", "#577590"])),
                tooltip=["name", "current_level"]
            ).properties(
                width=700,
                height=400
            )
    tab1, tab2, tab3 = st.tabs(["Employee Competency", "Feedback Reviews", "Course Recommender"])
    with tab1:
        st.altair_chart(chart, use_container_width=True)

    feedbacks = feedback_service.get_all_by_employee(employee_id)
    df_feedback = pd.DataFrame([d.model_dump() for d in feedbacks])
    with tab2:
        for _, row in df_feedback.iterrows():
            st.write(f"**Date**: {row["effective_date"]}")
            st.write(f"**Score**: {row["score"]}")
            st.write(f"**Comments**: {row["comments"]}")
            st.write("---")
    with tab3:
        with st.spinner("Getting course recomendations"):
            matching_courses = course_service.recommend_course(employee_id)
            courses = matching_courses.courses
            st.subheader("Competencies to improve")
            for comp in matching_courses.priority:
                st.write(f"**Name**: {comp.matching_competencies}, **Priority**: {comp.priority}, **Coming**: {comp.competency_from.value}")
            st.write("---")
        for course in courses:
            st.write(f"**Tittle**: {course.title}")
            st.write(f"**Competencies**: {course.matching_competencies}")
            st.write("**Rating**:", f"{round(course.rating, 2)}/5.0")
            st.write(f"**Number Reviews**: {course.number_of_reviews}")
            st.write(f"**Number Views**: {course.number_of_viewers}")
            st.write("**Short descrition**:")
            st.write(course.short_intro)
            st.write(f"[Click here]({course.url})")
            st.write("---")
