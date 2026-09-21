import asyncio
import aiohttp
from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()



async def data_fetch_from_weather() -> list:

    api_key = os.getenv('WEATHER_API')

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
        data_fetch_from_weather(),
        data_fetch_fitness(),
        marathon_data()
    )

    return result

    
def join_input():
    merged_data = asyncio.run(main())

    try:

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
    except Exception as e:
        print(f"The Error is - {type(e).__name__} : {e}")
        


def chat_bot():

    client_data = join_input()
    CLIENT_WHEHTER = client_data['whether_data']
    CLIENT_FITNESS = client_data['data_about_my_fitness']
    CLIENT_MARATHON_DATA = client_data['marathon_data']

    client = OpenAI(
        base_url = "https://integrate.api.nvidia.com/v1",
        api_key = os.getenv('AI_KEY'),
        timeout=60.0
    )

    try:
        completion = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b",

        messages = [
            {
                "role":"system",
                "content":"""You are the fittnes coach of me You have to give optimal startagy like what to carry what to avoid some tips and tricks and  using my data given, and give the output in ~300 words max, 
                The response contains useful advice, but it needs improvement in both formatting and race strategy quality.

                Formatting Improvements:
                1. Remove excessive spacing between letters and words. Use normal text formatting.
                2. Reduce overuse of bold text, capital letters, and separators. Reserve emphasis for critical information only.
                3. Use a clear heading structure:
                - Race Overview
                - Weather Impact
                - Pre-Race Preparation
                - Pacing Plan
                - Heat Management
                - Post-Race Recovery
                4. Make the response mobile-friendly with short paragraphs and bullet points.
                5. Highlight the most important takeaway at the top (for example: "Start 15-20 seconds per km slower than usual due to heat and humidity.").

                Strategy Improvements:
                1. Add a proper warm-up section (5-10 min easy jog, dynamic mobility, and a few strides).
                2. Include specific pace guidance in addition to RPE so runners can execute the plan more easily.
                3. Tone down dramatic statements such as "Survival > PB" and replace them with practical performance guidance.
                4. Simplify the physiology explanation and focus on actionable advice.
                5. Make hydration recommendations more realistic for a 5 km race; carrying a flask may not be necessary if aid stations are available.
                6. Mention race-day decision points, including when to push harder and when to back off because of heat-related symptoms.
                7. Prioritize evidence-based recovery recommendations (walking, hydration, carbohydrates, protein, cooling down) over less-supported suggestions like compression tights.

                Target Style:
                Write like an experienced running coach: concise, practical, professional, and easy to follow. Use clean Markdown formatting and focus on actionable race-day instructions rather than dramatic language.

                """
             
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