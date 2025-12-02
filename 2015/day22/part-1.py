from __future__ import annotations

import heapq
from dataclasses import dataclass


@dataclass
class Player:
    mana: int
    hit_points: int
    shield: int = 0
    poison: int = 0
    recharge: int = 0
    armor: int = 0

    def has_shield(self) -> bool:
        return self.shield > 0

    def has_poison(self) -> bool:
        return self.poison > 0

    def has_recharge(self) -> bool:
        return self.recharge > 0

    def can_cast_magic_missile(self) -> bool:
        return self.mana >= 53

    def can_cast_drain(self) -> bool:
        return self.mana >= 73

    def can_cast_shield(self) -> bool:
        return self.mana >= 113 and not self.has_shield()

    def can_cast_poison(self) -> bool:
        return self.mana >= 173 and not self.has_poison()

    def can_cast_recharge(self) -> bool:
        return self.mana >= 229 and not self.has_recharge()

    def __lt__(self, other):
        return True


@dataclass
class Boss:
    damage: int
    hit_points: int

    def __lt__(self, other):
        return True


h = []
heapq.heappush(h, (0, Player(mana=500, hit_points=50), Boss(damage=10, hit_points=71)))


def effects(player: Player, boss: Boss):
    if player.has_shield():
        player.armor = 7
        player.shield -= 1
    if player.has_poison():
        boss.hit_points -= 3
        player.poison -= 1
    if player.has_recharge():
        player.mana += 101
        player.recharge -= 1


while True:
    mana, player, boss = heapq.heappop(h)
    if boss.hit_points <= 0:
        break

    if player.hit_points <= 0:
        continue

    effects(player, boss)

    if player.can_cast_magic_missile():
        p = Player(
            mana=player.mana - 53,
            hit_points=player.hit_points,
            shield=player.shield,
            poison=player.poison,
            recharge=player.recharge,
        )
        b = Boss(damage=boss.damage, hit_points=boss.hit_points - 4)
        effects(p, b)
        p.hit_points -= max(boss.damage - p.armor, 1)
        heapq.heappush(h, (mana + 53, p, b))

    if player.can_cast_drain():
        p = Player(
            mana=player.mana - 73,
            hit_points=player.hit_points + 2,
            shield=player.shield,
            poison=player.poison,
            recharge=player.recharge,
        )
        b = Boss(damage=boss.damage, hit_points=boss.hit_points - 2)
        effects(p, b)
        p.hit_points -= max(boss.damage - p.armor, 1)
        heapq.heappush(h, (mana + 73, p, b))

    if player.can_cast_shield():
        p = Player(
            mana=player.mana - 113,
            hit_points=player.hit_points,
            shield=6,
            poison=player.poison,
            recharge=player.recharge,
        )
        b = Boss(damage=boss.damage, hit_points=boss.hit_points)
        effects(p, b)
        p.hit_points -= max(boss.damage - p.armor, 1)
        heapq.heappush(h, (mana + 113, p, b))

    if player.can_cast_poison():
        p = Player(
            mana=player.mana - 173,
            hit_points=player.hit_points,
            shield=player.shield,
            poison=6,
            recharge=player.recharge,
        )
        b = Boss(damage=boss.damage, hit_points=boss.hit_points)
        effects(p, b)
        p.hit_points -= max(boss.damage - p.armor, 1)
        heapq.heappush(h, (mana + 173, p, b))

    if player.can_cast_recharge():
        p = Player(
            mana=player.mana - 229,
            hit_points=player.hit_points,
            shield=player.shield,
            poison=player.poison,
            recharge=5,
        )
        b = Boss(damage=boss.damage, hit_points=boss.hit_points)
        effects(p, b)
        p.hit_points -= max(boss.damage - p.armor, 1)
        heapq.heappush(h, (mana + 229, p, b))

print(mana)
