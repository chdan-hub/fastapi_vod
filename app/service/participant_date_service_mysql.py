from app.tortoise_models.participant_date import ParticipantDateModel


async def service_turn_on_participant_date_mysql(participant_date_id: int) -> None:
    # enabled=True
    await ParticipantDateModel.filter(id=participant_date_id).update(enabled=True)


async def service_turn_off_participant_date_mysql(participant_date_id: int) -> None:
    # enabled=False
    await ParticipantDateModel.filter(id=participant_date_id).update(enabled=False)


async def service_star_participant_date_mysql(participant_date_id: int) -> None:
    # starred=True + enabled=True (테스트 기대 로직)
    await ParticipantDateModel.filter(id=participant_date_id).update(starred=True, enabled=True)


async def service_unstar_participant_date_mysql(participant_date_id: int) -> None:
    # starred=False (enabled는 변경하지 않음)
    await ParticipantDateModel.filter(id=participant_date_id).update(starred=False)
