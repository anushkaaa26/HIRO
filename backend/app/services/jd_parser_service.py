from app.schemas.jd_schema import JDParseResponse


def parse_job_description(job_description: str) -> JDParseResponse:
    """
    Mock parser.
    Later this will call the Lemma JD Parser Pod.
    """

    return JDParseResponse(
        company="Google",
        role="Software Engineer Intern",
        skills=[
            "Python",
            "FastAPI",
            "React",
            "Machine Learning"
        ],
        experience="0-2 years",
        location="Remote",
        employment_type="Internship",
        deadline=None
    )