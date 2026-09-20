import asyncio
import aiohttp
from openai import OpenAI



async def data_fetch_from_wether() -> list:

    api_key = "76ebe517808963e9bcbfd579a75c3568"

    lat = 20.82995822420193
    lon = 85.05696466179847
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={api_key}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()


        temp = f"Tempreture - {data["list"][0]["main"]["temp"]}"
        feels_like = f"feels like - {data['list'][0]['main']['feels_like']}"
        humidity = f"humidity - {data['list'][0]['main']['humidity']}"
        descripton = f"whether description - {data["list"][0]["weather"][0]["description"]}"

        return [temp, feels_like, humidity, descripton]
    except Exception as e:
        print(f"something wrong while fetch whether {type(e).__name__} : {e}")

async def data_fetch_fitness() -> str:
    hight =  int(input('Your Hight: '))
    waight =  int(input('your waight: '))
    data = f"my hight is - {hight} & my waigth is - {waight}"
    return data

async def marathon_data() -> str:
    marathon_lenght = input('marathon lenght: ')

    data = f"the length of marathon {marathon_lenght}"
    if data == "":
        return None

    return data


async def main():
    result = await asyncio.gather(
        data_fetch_from_wether(),
        data_fetch_fitness(),
        marathon_data()
    )

    return result

    
def join_input():
    merged_data = asyncio.run(main())

    whether_data = "data about current whether and temprature - "
    for d in merged_data[0]:
        whether_data += d + "\n"

    fitness = merged_data[1]
    marathon_data = merged_data[2]

    return {
        "whether_data":whether_data,
        "data_about_my_fitness":fitness,
        "marathon_data":marathon_data
    }


def chat_bot():

    client_data = join_input()
    CLIENT_WHEHTER = client_data['whether_data']
    CLIENT_FITNESS = client_data['data_about_my_fitness']
    CLIENT_MARATHON_DATA = client_data['marathon_data']

    client = OpenAI(
        base_url = "https://integrate.api.nvidia.com/v1",
        api_key = "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",
        timeout=60.0
    )

    try:
        completion = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b",

        messages = [
            {
                "role":"system",
                "content":"You are the fittnes coach of me You have to give optimal startagy like what to carry what to avoid some tips and tricks and  using my data given, and give the output in ~300 words, "
             
            },
            {
                "role":"assistant",
                "content":CLIENT_WHEHTER + CLIENT_FITNESS + CLIENT_MARATHON_DATA + input('Prompt: ')
            }
        ],

        temperature=1,
        top_p=0.95,
        max_tokens=1384,
        extra_body={"chat_template_kwargs":{"enable_thinking":True}},
        stream=True
        )

        response = ""

        for chunk in completion:
            if not chunk.choices:
                continue
            reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
            if reasoning:
                print(reasoning, end="")
            if chunk.choices[0].delta.content is not None:
                print( chunk.choices[0].delta.content , end=" ")
    except Exception as e:
        print(f"something went wrong {type(e).__name__ }: {e}")

if __name__ == "__main__":
    chat_bot()