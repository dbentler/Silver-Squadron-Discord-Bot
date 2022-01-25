import random

def mini_shoot(user: str) -> str:
    messages = {1: f"> You look at {user} and think angry thoughts.",
                2: "> You shoot yourself in the foot.",
                3: f"> You pick up a revolver and aim it at {user}. Your revolver 'jams'.",
                4: f"> You unload into {user}, but it was a hologram.",
                5: f"> You unload towards {user}, silhouetting them.",
                6: f"> You fire one bullet and hit {user} center of mass.",
                7: f"> You shoot {user}, but now you feel bad.",
                8: f"> You shoot {user}, and you feel good you *psycho*.",
                9: "> You end up shooting @Forsell#9603",
                10: f"> You shoot {user}."}
    roll = random.randint(1, 10)
    return messages[roll]