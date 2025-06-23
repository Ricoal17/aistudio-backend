import openai from mega import Mega import asyncio import tenacity

Masukkan API key OpenAI-mu

openai.api_key = "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"

Retry dengan tenacity untuk menghindari limit error OpenAI

@tenacity.retry(wait=tenacity.wait_fixed(2), stop=tenacity.stop_after_attempt(5)) async def generate_ai(prompt): response = await asyncio.to_thread(openai.ChatCompletion.create, model="gpt-3.5-turbo", messages=[ {"role": "system", "content": "You are an AI content generator."}, {"role": "user", "content": prompt} ] ) return response['choices'][0]['message']['content']

async def main(): prompt = "Buatkan cerita edukatif lucu untuk karakter Plompi dan Lumi berdurasi 1 menit." hasil = await generate_ai(prompt)

with open("hasil_ai.txt", "w") as f:
    f.write(hasil)

mega = Mega()
m = mega.login("romlirico67@gmail.com", "Rico@say4")
m.upload("hasil_ai.txt")
print("Berhasil generate dan upload ke MEGA!")

if name == "main": asyncio.run(main())

