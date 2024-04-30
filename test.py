from typing import Protocol, TypeVar

from attr import frozen


class TraitHasReasoning(Protocol):
    reasoning: str


T_HasReasoning = TypeVar("T_HasReasoning", bound=TraitHasReasoning)


@frozen
class ConcreteHasReasoning(TraitHasReasoning):
    reasoning: str


def mutate_reasoning(obj: T_HasReasoning, val: str) -> T_HasReasoning:
    obj.reasoning = val
    return obj


if __name__ == "__main__":
    result = mutate_reasoning(ConcreteHasReasoning(reasoning="a"), "b")
