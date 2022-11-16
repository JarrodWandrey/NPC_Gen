import settings

def write_file(): #function to write in all gen'd npc into the file
    with open("npc.txt", "w") as f:
        for x in settings.NPCs:
            f.write(x + '\n')
