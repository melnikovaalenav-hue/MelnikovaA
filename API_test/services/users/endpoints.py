from API_test.config.stages import get_stage

class Endpoints:

    STAGES = get_stage()

    create_user = f"{STAGES}/v2/pet"