import openai
from mega import Mega

# Masukkan API key OpenAI-mu
openai.api_key = "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"

# Proses generate AI
async def generate_ai(prompt):
    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI content generator."},
            {"role": "user", "content": prompt}
        ]
    )
    result = response['choices'][0]['message']['content']
    return result

import asyncio

async def main():
    prompt = "Buatkan cerita edukatif lucu untuk karakter Plompi dan Lumi berdurasi 1 menit."
    hasil = await generate_ai(prompt)

    with open("hasil_ai.txt", "w") as f:
        f.write(hasil)

    mega = Mega()
    m = mega.login("romlirico67@gmail.com", "Rico@say4")
    m.upload("hasil_ai.txt")

    print("Berhasil generate dan upload ke MEGA!")

if __name__ == "__main__":
    asyncio.run(main())
