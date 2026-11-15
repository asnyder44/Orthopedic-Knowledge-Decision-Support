"""Made-up (synthetic) rehabilitation records that follow the rehab model, so the whole flow can be shown
without any real patient data. Nothing here describes a real person; values are random within plausible ranges
and are NOT clinical evidence."""

from __future__ import annotations

import random
from typing import Any

# (condition KO, procedure KO or "", protocol KO, intervention Treatment KOs, outcome measure KO or "", joint, label)
PATHWAYS = [
    ("KO-HAND-COND-001", "KO-HAND-PROC-001", "KO-HAND-REHAB-001", ["KO-HAND-TRT-003", "KO-HAND-TRT-001"],
     "KO-HAND-OUT-001", "wrist", "Carpal tunnel release rehab"),
    ("KO-HAND-COND-002", "", "KO-HAND-TRT-004", ["KO-HAND-TRT-004", "KO-HAND-TRT-003"], "", "elbow",
     "Cubital tunnel conservative care"),
    ("KO-SPORT-COND-001", "KO-SPORT-PROC-001", "KO-JOINT-TRT-001", ["KO-JOINT-TRT-001"], "", "knee",
     "ACL reconstruction rehab"),
    ("KO-JOINT-COND-001", "KO-JOINT-PROC-001", "KO-JOINT-TRT-001", ["KO-JOINT-TRT-001"], "", "knee",
     "Knee replacement rehab"),
    ("KO-TRAUMA-COND-002", "", "KO-TRAUMA-TRT-001", ["KO-TRAUMA-TRT-001", "KO-HAND-TRT-003"], "", "wrist",
     "Wrist fracture after casting"),
    ("KO-SPINE-COND-001", "", "KO-SPINE-TRT-001", ["KO-SPINE-TRT-001"], "", "spine", "Spinal stenosis therapy"),
]
EXERCISES = {"wrist": ["tendon gliding", "nerve gliding", "wrist range of motion", "grip strengthening"],
             "elbow": ["nerve gliding", "elbow range of motion", "activity modification practice"],
             "knee": ["quad sets", "heel slides", "straight leg raises", "mini squats", "stationary bike"],
             "spine": ["walking program", "core stabilization", "flexion stretches"]}
MOVES = {"wrist": ["flexion", "extension"], "elbow": ["flexion", "extension"], "knee": ["flexion", "extension"],
         "spine": ["flexion", "rotation"]}
ROM_TARGET = {("wrist", "flexion"): 75, ("wrist", "extension"): 65, ("elbow", "flexion"): 140,
              ("elbow", "extension"): 0, ("knee", "flexion"): 125, ("knee", "extension"): 0,
              ("spine", "flexion"): 60, ("spine", "rotation"): 40}
ADL = {"wrist": ["writing", "cooking", "dressing"], "elbow": ["dressing", "lifting", "work tasks"],
       "knee": ["walking", "stairs", "driving"], "spine": ["walking", "lifting", "bathing"]}
EXERCISE_KOS = ("KO-HAND-TRT-003", "KO-JOINT-TRT", "KO-SPINE-TRT")  # Treatment KOs that are exercise programs
AGE_BANDS = ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89"]


def make_sample(patients: int = 40, seed: int = 7) -> dict[str, list[dict[str, Any]]]:
    rnd = random.Random(seed)
    t: dict[str, list[dict[str, Any]]] = {}
    counter: dict[str, int] = {}

    def add(entity: str, prefix: str, **row: Any) -> str:
        counter[entity] = counter.get(entity, 0) + 1
        rid = f"{prefix}-{counter[entity]:04d}"
        id_field = {"Patient": "patient_id", "HealthcareProvider": "provider_id", "TreatmentProtocol": "protocol_id"}
        key = id_field.get(entity) or next(k for k in ID_FIELDS[entity])
        t.setdefault(entity, []).append({key: rid, **row})
        return rid

    roles = [("physical therapist", "outpatient clinic"), ("hand therapist", "outpatient clinic"),
             ("occupational therapist", "outpatient clinic"), ("physical therapist", "home"),
             ("athletic trainer", "outpatient clinic"), ("physical therapist", "telehealth")]
    providers = [add("HealthcareProvider", "HP", role=r, setting=s) for r, s in roles]
    protocols = {p[2]: add("TreatmentProtocol", "TP", name=p[6], protocol_ko=p[2]) for p in PATHWAYS}

    for _ in range(patients):
        cond, proc, proto, treatments, measure, joint, _label = rnd.choice(PATHWAYS)
        age = rnd.choice(AGE_BANDS[2:] if cond in ("KO-JOINT-COND-001", "KO-SPINE-COND-001") else AGE_BANDS)
        pid = add("Patient", "P", age_band=age, sex=rnd.choice(["female", "male", "female", "male", "not stated"]),
                  condition_ko=cond, side=rnd.choice(["left", "right"]) if joint != "spine" else "not applicable")
        weeks = rnd.randint(4, 10)
        status = rnd.choices(["completed", "active", "stopped early"], [7, 2, 1])[0]
        rid = add("Rehabilitation", "R", patient_id=pid, procedure_ko=proc, protocol_ko=proto,
                  start_year=rnd.choice([2024, 2025, 2026]), status=status)
        plan = add("RehabilitationPlan", "PL", rehab_id=rid, protocol_id=protocols[proto])
        goals = [add("RecoveryGoal", "G", plan_id=plan, goal=g, target_day=weeks * 7)
                 for g in rnd.sample(["less pain", "full range of motion", "return to daily activities", "return to work"], 2)]
        add("TreatmentSchedule", "SC", plan_id=plan, sessions_per_week=rnd.choice([1, 2, 2, 3]), weeks=weeks)
        provider = rnd.choice(providers)
        sessions = []
        for k in range(rnd.randint(4, 10)):
            day = int((k + 1) * weeks * 7 / 11)
            sid = add("RehabSession", "S", rehab_id=rid, provider_id=provider, day=day, minutes=rnd.choice([30, 45, 45, 60]))
            sessions.append(sid)
            for name in rnd.sample(EXERCISES[joint], min(2, len(EXERCISES[joint]))):
                exercise_ko = treatments[0] if treatments[0].startswith(EXERCISE_KOS) else ""
                ex = add("RehabExercise", "EX", session_id=sid, exercise=name, treatment_ko=exercise_ko)
                add("ExercisePerformance", "EP", session_id=sid, exercise_id=ex, sets=rnd.randint(1, 3),
                    reps=rnd.choice([10, 10, 15, 20]), completed=rnd.random() > 0.15)
            add("TherapeuticIntervention", "TI", session_id=sid, treatment_ko=rnd.choice(treatments),
                minutes=rnd.choice([10, 15, 20]))
            if rnd.random() < 0.3:
                add("SessionReport", "SR", session_id=sid, summary=rnd.choice(
                    ["Tolerated exercises well.", "Reported mild soreness after exercises.", "Progressed home program.",
                     "Reviewed activity changes at work."]))
        pain0 = rnd.randint(5, 8)
        checkpoints = [0, weeks * 7 // 2, weeks * 7] if status != "stopped early" else [0, weeks * 7 // 2]
        for j, day in enumerate(checkpoints):
            progress = j / 2
            a = add("RecoveryAssessment", "A", rehab_id=rid, day=day)
            mob = add("MobilityAssessment", "M", assessment_id=a)
            for move in MOVES[joint]:
                target = ROM_TARGET[(joint, move)]
                start = target * rnd.uniform(0.45, 0.7) if target else rnd.uniform(5, 15)
                deg = start + (target - start) * progress * rnd.uniform(0.7, 1.0)
                add("RangeOfMotion", "ROM", mobility_id=mob, joint=joint, movement=move, degrees=round(deg))
            if joint in ("knee", "spine"):
                add("Balance", "B", mobility_id=mob, test="timed up and go",
                    score=round(rnd.uniform(14, 18) - 5 * progress * rnd.uniform(0.6, 1.0), 1))
            pa = add("PainAssessment", "PA", assessment_id=a)
            add("PainLocation", "PLC", pain_id=pa, body_site=joint, side="not applicable" if joint == "spine" else "both"
                if rnd.random() < 0.1 else rnd.choice(["left", "right"]))
            add("PainLevel", "PLV", pain_id=pa, scale="NRS 0-10",
                score=max(0, round(pain0 - pain0 * progress * rnd.uniform(0.5, 0.9))))
            fa = add("FunctionalAssessment", "FA", assessment_id=a, outcome_measure_ko=measure)
            if joint in ("wrist", "elbow"):
                add("PhysicalStrength", "PS", functional_id=fa, muscle_group="grip", measure="grip strength (kg)",
                    value=round(rnd.uniform(12, 20) + 12 * progress * rnd.uniform(0.6, 1.0), 1))
            else:
                add("PhysicalStrength", "PS", functional_id=fa, muscle_group="quadriceps",
                    measure="manual muscle test (0-5)", value=min(5, 3 + round(2 * progress * rnd.uniform(0.6, 1.0))))
            for act in rnd.sample(ADL[joint], 2):
                add("DailyLivingAbility", "ADL", functional_id=fa, activity=act,
                    independence=["needs some help", "needs some help", "independent"][min(2, j + rnd.randint(0, 1))])
            out = add("RecoveryOutcome", "O", assessment_id=a, outcome_measure_ko=measure,
                      score=round(3.5 - 2 * progress * rnd.uniform(0.6, 1.0), 2) if measure else round(40 + 45 * progress, 1))
            for g in goals:
                pct = min(100, round(100 * progress * rnd.uniform(0.7, 1.1)))
                add("GoalProgress", "GP", outcome_id=out, goal_id=g, percent=pct)
            if j == 1 and rnd.random() < 0.35:
                add("TreatmentAdjustment", "TA", assessment_id=a, plan_id=plan, protocol_id=protocols[proto],
                    reason=rnd.choice(["faster progress than expected", "slower progress than expected", "pain"]))
            if j == len(checkpoints) - 1 and status == "completed":
                for m in rnd.sample(["pain free", "full range of motion", "independent daily living", "return to work"], 2):
                    add("RecoveryMilestone", "MS", outcome_id=out, milestone=m, day=day)
                d = add("DischargeAssessment", "D", outcome_id=out, day=day,
                        discharged_to=rnd.choice(["home program", "home program", "no further care"]))
                add("FollowUpPlan", "F", discharge_id=d, follow_up_weeks=rnd.choice([4, 6, 12]))
        add("PatientFeedback", "FB", patient_id=pid, session_id=rnd.choice(sessions), provider_id=provider,
            day=weeks * 7, satisfaction=rnd.choice([3, 4, 4, 5, 5]), comment="")
    return t


ID_FIELDS = {
    "PatientFeedback": ["feedback_id"], "Rehabilitation": ["rehab_id"], "RehabSession": ["session_id"],
    "SessionReport": ["report_id"], "ExercisePerformance": ["performance_id"], "TherapeuticIntervention": ["intervention_id"],
    "RehabExercise": ["exercise_id"], "RecoveryAssessment": ["assessment_id"], "RecoveryOutcome": ["outcome_id"],
    "GoalProgress": ["progress_id"], "DischargeAssessment": ["discharge_id"], "FollowUpPlan": ["followup_id"],
    "RecoveryMilestone": ["milestone_id"], "MobilityAssessment": ["mobility_id"], "RangeOfMotion": ["rom_id"],
    "Balance": ["balance_id"], "FunctionalAssessment": ["functional_id"], "PhysicalStrength": ["strength_id"],
    "DailyLivingAbility": ["adl_id"], "PainAssessment": ["pain_id"], "PainLocation": ["location_id"],
    "PainLevel": ["level_id"], "TreatmentAdjustment": ["adjustment_id"], "RehabilitationPlan": ["plan_id"],
    "RecoveryGoal": ["goal_id"], "TreatmentSchedule": ["schedule_id"],
}
