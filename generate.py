from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


def generatePlaylist(mood):
    prompt = """
    You are a DJ, when given a mood, you will generate a list of 10 songs that match that mood. Here is an example of the desired format:

    "Dreamy Drowsiness"
    "\"Stay\" by Rihanna ft. Mikky Ekko",
    "\"Skinny Love\" by Bon Iver",
    "\"Breathe Me\" by Sia",
    "\"Hallelujah\" by Jeff Buckley",
    "\"Landslide\" by Fleetwood Mac",
    "\"The Scientist\" by Coldplay",
    "\"Mad World\" by Gary Jules",
    "\"To Build a Home\" by The Cinematic Orchestra",
    "\"Hurt\" by Johnny Cash",
    "\"Fade Into You\" by Mazzy Star"
    """
    
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},

            {"role": "user", "content": mood}
        ]
    )

    response = completion.choices[0].message.content
    print(response)
    songs = completion.choices[0].message.content.split('\n')[2::]

    songList = []
    for s in songs:
        index = s.find('"')
        songList.append(s[index:])

    name = completion.choices[0].message.content.split('\n')[0]

    json_data = {
        "name": name,
        "songs": songList
    }

    print(json_data)
    return (json_data)
