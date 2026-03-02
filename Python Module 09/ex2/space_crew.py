from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
import datetime


class CrewRanks(Enum):
    CADET = 'cadet'
    OFFICER = 'officer'
    LIEUTENANT = 'lieutenant'
    CAPTAIN = 'captain'
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime.datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')
        has_leader = False
        for member in self.crew:
            if member.rank in (CrewRanks.COMMANDER, CrewRanks.CAPTAIN):
                has_leader = True
        if not has_leader:
            raise ValueError('Must have at least one Commander or Captain')
        experts = []
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience >= 5:
                    experts.append(member)
            if len(experts) < len(self.crew) / 2:
                raise ValueError(
                    'Long missions (> 365 days) need 50% '
                    'experienced crew (5+ years)'
                )
        for member in self.crew:
            if not member.is_active:
                raise ValueError('All crew members must be active')
        return self


def main() -> None:

    print('Space Mission Crew Validation')
    print('=========================================')

    print('Valid mission created:')
    pedro = CrewMember(member_id='001',
                       name='Pedro',
                       rank=CrewRanks.COMMANDER,
                       age=20,
                       specialization='Mission Command',
                       years_experience=20,
                       is_active=True)

    joao = CrewMember(member_id='002',
                      name='Joao',
                      rank=CrewRanks.CADET,
                      age=20,
                      specialization='Navigation',
                      years_experience=20,
                      is_active=True)

    paula = CrewMember(member_id='002',
                       name='Paula',
                       rank=CrewRanks.CADET,
                       age=20,
                       specialization='Engineering',
                       years_experience=20,
                       is_active=True)

    mission = SpaceMission(mission_id='M2024_MARS',
                           mission_name='Mars Colony Establishment',
                           destination='Mars',
                           launch_date='2024-01-15T10:30:00',
                           duration_days=900,
                           crew=[pedro, joao, paula],
                           mission_status='planned',
                           budget_millions=2500.0)

    print(f'Mission: {mission.mission_name}')
    print(f'ID: {mission.mission_id}')
    print(f'Destination: {mission.destination}')
    print(f'Duration: {mission.duration_days} days')
    print(f'Budget: {mission.budget_millions}')
    print(f'Crew size: {len(mission.crew)}')
    print('Crew members:')
    for member in mission.crew:
        print(
            f'- {member.name} ({member.rank.value}) - {member.specialization}'
        )

    print()

    print('=========================================')

    try:
        pedro = CrewMember(
            member_id='001',
            name='Pedro',
            rank=CrewRanks.OFFICER,
            age=20,
            specialization='ouvir',
            years_experience=20,
            is_active=True)

        joao = CrewMember(
            member_id='002',
            name='Joao',
            rank=CrewRanks.CADET,
            age=20,
            specialization='chorar',
            years_experience=20,
            is_active=True)

        paula = CrewMember(
            member_id='002',
            name='Paula',
            rank=CrewRanks.CADET,
            age=20,
            specialization='chorar',
            years_experience=20,
            is_active=True)

        mission = SpaceMission(
            mission_id='M2024_MARS',
            mission_name='Mars Colony Establishment',
            destination='Mars',
            launch_date='2024-01-15T10:30:00',
            duration_days=900,
            crew=[pedro, joao, paula],
            mission_status='planned',
            budget_millions=2500.0)
    except ValidationError as e:
        print('Expected validation error:')
        for error in e.errors():
            print(error['msg'])


if __name__ == '__main__':
    main()
