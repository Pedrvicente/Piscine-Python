from pydantic import BaseModel, ValidationError, Field, model_validator
import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime.datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith('AC'):
            raise ValueError('contact_id must start with AC')
        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                raise ValueError('Physical contact reports must be verified')
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    'Telepathic contact requires at least 3 witnesses'
                )
        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError(
                    'Strong signals (> 7.0) should include received messages'
                )
        return self


def main() -> None:

    print('Alien Contact Log Validation')
    print('======================================')

    print('Valid contact report:')
    alien = AlienContact(contact_id='AC_2024_001',
                         timestamp=datetime.datetime.fromisoformat(
                             '2024-01-15T10:30:00'),
                         location='Area 51, Nevada',
                         contact_type=ContactType.RADIO,
                         signal_strength=8.5,
                         duration_minutes=45,
                         witness_count=5,
                         message_received='olaaaaaa',
                         is_verified=True)

    print(f'ID: {alien.contact_id}')
    print(f'Type: {alien.contact_type.value}')
    print(f'Location: {alien.location}')
    print(f'Signal: {alien.signal_strength}/10')
    print(f'Duration: {alien.duration_minutes} minutes')
    print(f'Witnesses: {alien.witness_count}')
    print(f'Message: {alien.message_received}')

    print()

    print('======================================')
    try:
        print('Expected validation error:')
        AlienContact(contact_id='AC_2024_001',
                     timestamp=datetime.datetime.fromisoformat(
                         '2024-01-15T10:30:00'),
                     location='Area 51, Nevada',
                     contact_type=ContactType.TELEPATHIC,
                     signal_strength=8.5,
                     duration_minutes=45,
                     witness_count=2,
                     is_verified=True)
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == '__main__':
    main()
