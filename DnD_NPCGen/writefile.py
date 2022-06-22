import settings

def write_file():
    with open("npc.txt", "w") as f:
        for x in settings.NPCs:
            f.write(x + '\n')
