from __future__ import annotations

import strawberry
from enum import Enum
from typing import NewType


@strawberry.type
class Query:
    # @strawberry.field(description="Get a specific character by ID")
    # def character(self, id: int) -> Character | None:
    #     ...

    @strawberry.field(description="Get all characters with selected status (TECH: to test enums in args)")
    def characters_by_status(self, status: Status) -> Characters | None:
        ...

    # @strawberry.field(description="Get the list of all characters")
    # def characters(self, page: int, filter: FilterCharacter) -> Characters | None:
    #     ...

    # @strawberry.field(description="Get a list of characters selected by ids")
    # def characters_by_ids(self, ids: list[int]) -> list[Character | None] | None:
    #     ...

    # @strawberry.field(description="Get a specific locations by ID")
    # def location(self, id: int) -> Location | None:
    #     ...

    # @strawberry.field(description="Get the list of all locations")
    # def locations(self, page: int, filter: FilterLocation) -> Locations | None:
    #     ...

    # @strawberry.field(description="Get a list of locations selected by ids")
    # def locations_by_ids(self, ids: list[int]) -> list[Location | None] | None:
    #     ...

    # @strawberry.field(description="Get a specific episode by ID")
    # def episode(self, id: int) -> Episode | None:
    #     ...

    # @strawberry.field(description="Get the list of all episodes")
    # def episodes(self, page: int, filter: FilterEpisode) -> Episodes | None:
    #     ...

    # @strawberry.field(description="Get a list of episodes selected by ids")
    # def episodes_by_ids(self, ids: list[int]) -> list[Episode | None] | None:
    #     ...


@strawberry.type(description="")
class Character:
    id: strawberry.ID | None = strawberry.field(description="The id of the character.")
    name: str | None = strawberry.field(description="The name of the character.")
    status: Status | None = strawberry.field(description="The status of the character ('Alive', 'Dead' or 'unknown').")
    species: str | None = strawberry.field(description="The species of the character.")
    type: str | None = strawberry.field(description="The type or subspecies of the character.")
    gender: str | None = strawberry.field(description="The gender of the character ('Female', 'Male', 'Genderless' or 'unknown').")
    origin: Location | None = strawberry.field(description="The character's origin location")
    location: Location | None = strawberry.field(description="The character's last known location")
    image: str | None = strawberry.field(description="""
Link to the character's image.
All images are 300x300px and most are medium shots or portraits since they are intended to be used as avatars.
""")
    episode: list[Episode | None] = strawberry.field(description="Episodes in which this character appeared.")
    created: str | None = strawberry.field(description="Time at which the character was created in the database.")


@strawberry.enum
class Status(Enum):
    alive = "Alive"
    dead = "Dead"
    unknown = "unknown"


@strawberry.type(description="")
class Location:
    id: strawberry.ID | None = strawberry.field(description="The id of the location.")
    name: str | None = strawberry.field(description="The name of the location.")
    type: str | None = strawberry.field(description="The type of the location.")
    dimension: str | None = strawberry.field(description="The dimension in which the location is located.")
    residents: list[Character | None] = strawberry.field(description="List of characters who have been last seen in the location.")
    created: str | None = strawberry.field(description="Time at which the location was created in the database.")


@strawberry.type(description="")
class Episode:
    id: strawberry.ID | None = strawberry.field(description="The id of the episode.")
    name: str | None = strawberry.field(description="The name of the episode.")
    air_date: str | None = strawberry.field(description="The air date of the episode.")
    episode: str | None = strawberry.field(description="The code of the episode.")
    characters: list[Character | None] = strawberry.field(description="List of characters who have been seen in the episode.")
    created: str | None = strawberry.field(description="Time at which the episode was created in the database.")


@strawberry.input(description="")
class FilterCharacter:
    name: str | None
    status: Status | None
    species: str | None
    type: str | None
    gender: str | None


@strawberry.type(description="")
class Characters:
    info: Info | None
    results: list[Character | None] | None


@strawberry.type(description="")
class Info:
    count: int | None = strawberry.field(description="The length of the response.")
    pages: int | None = strawberry.field(description="The amount of pages.")
    next: int | None = strawberry.field(description="Number of the next page (if it exists)")
    prev: int | None = strawberry.field(description="Number of the previous page (if it exists)")


@strawberry.input(description="")
class FilterLocation:
    name: str | None
    type: str | None
    dimension: str | None


@strawberry.type(description="")
class Locations:
    info: Info | None
    results: list[Location | None] | None


@strawberry.input(description="")
class FilterEpisode:
    name: str | None
    episode: str | None


@strawberry.type(description="")
class Episodes:
    info: Info | None
    results: list[Episode | None] | None


@strawberry.enum
class CacheControlScope(Enum):
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


Upload = strawberry.scalar(
    NewType("Upload", object),
    description="The `Upload` scalar type represents a file upload.",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)


schema = strawberry.Schema(query=Query)

