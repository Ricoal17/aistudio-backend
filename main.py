import openai
from mega import Mega

# Masukkan API key OpenAI-mu
openai.api_key = "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"

# Fungsi generate AI
def generate_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI content generator."},
            {"role": "user", "content": prompt}
        ]
    )
    result = response['choices'][0]['message']['content']
    return result

# Prompt input
prompt = "Buatkan cerita edukatif lucu untuk karakter Plompi dan Lumi berdurasi 1 menit."
hasil = generate_ai(prompt)

# Simpan hasil ke file
with open("hasil_ai.txt", "w") as f:
    f.write(hasil)

# Upload ke MEGA
mega = Mega()
m = mega.login("romlirico67@gmail.com", "Rico@say4")
m.upload("hasil_ai.txt")

print("Berhasil generate dan upload ke MEGA!")
