import random

from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):

    def create_creature(
        self, name_or_power: str | int | None = None
    ) -> Card:
        creatures = ["Fire Dragon", "Goblin Warrior", "Ice Giant"]
        rarities = [Rarity.LEGENDARY,
                    Rarity.COMMON,
                    Rarity.RARE,
                    Rarity.UNCOMMON,
                    Rarity.EPIC]

        if isinstance(name_or_power, str):
            return CreatureCard(
                name_or_power, random.randint(1, 5),
                random.choice(rarities),
                random.randint(1, 7), random.randint(1, 7)
            )

        elif isinstance(name_or_power, int):
            return CreatureCard(
                random.choice(creatures), name_or_power,
                random.choice(rarities),
                name_or_power, name_or_power
            )

        else:
            return CreatureCard(
                random.choice(creatures), random.randint(1, 5),
                random.choice(rarities),
                random.randint(1, 7), random.randint(1, 7)
            )

    def create_spell(
        self, name_or_power: str | int | None = None
    ) -> Card:
        spells = ["Fireball", "Ice Bolt", "Lightning Strike"]
        effect_types = ["damage", "heal", "buff", "debuff"]
        rarities = [Rarity.LEGENDARY,
                    Rarity.COMMON,
                    Rarity.RARE,
                    Rarity.UNCOMMON,
                    Rarity.EPIC]

        if isinstance(name_or_power, str):
            return SpellCard(
                name_or_power, random.randint(1, 5),
                random.choice(rarities),
                random.choice(effect_types)
            )

        elif isinstance(name_or_power, int):
            return SpellCard(
                random.choice(spells), name_or_power,
                random.choice(rarities),
                random.choice(effect_types)
            )

        else:
            return SpellCard(
                random.choice(spells), random.randint(1, 5),
                random.choice(rarities), "damage"
            )

    def create_artifact(
            self, name_or_power: str | int | None = None
    ) -> Card:
        artifacts = ["Rings", "Staffs", "Crystals"]
        effects = ["Mana boost",
                   "Attack boost",
                   "Card draw",
                   "Cost reduction",
                   "Regeneration"]
        rarities = [Rarity.LEGENDARY,
                    Rarity.COMMON,
                    Rarity.RARE,
                    Rarity.UNCOMMON,
                    Rarity.EPIC]

        if isinstance(name_or_power, str):
            return ArtifactCard(name_or_power, random.randint(1, 5),
                                random.choice(rarities),
                                random.randint(1, 7),
                                random.choice(effects))
        elif isinstance(name_or_power, int):
            return ArtifactCard(random.choice(artifacts), name_or_power,
                                random.choice(rarities),
                                name_or_power,
                                random.choice(effects))
        else:
            return ArtifactCard(
                random.choice(artifacts), random.randint(1, 5),
                random.choice(rarities),
                random.randint(1, 5),
                random.choice(effects)
            )

    def create_themed_deck(self, size: int) -> dict:
        creatures = []
        spells = []
        artifacts = []

        for _ in range(size):
            card_type = random.choice(['creatures', 'spells', 'artifacts'])
            if card_type == 'creatures':
                creatures.append(self.create_creature())
            elif card_type == 'spells':
                spells.append(self.create_spell())
            elif card_type == 'artifacts':
                artifacts.append(self.create_artifact())

        return {
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts
        }

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['fire_dragon', 'goblin_warrior', 'ice_giant'],
            'spells': ['fireball', 'ice_bolt', 'lightning_strike'],
            'artifacts': ['mana_ring', 'power_staff', 'soul_crystal']
        }
