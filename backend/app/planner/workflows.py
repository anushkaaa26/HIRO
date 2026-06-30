from app.planner.registry import planner


def apply_workflow(job_description):

    context = {
        "job_description": job_description
    }

    fit = planner.run_agent("fit", context)

    return {
        "fit_analysis": fit
    }