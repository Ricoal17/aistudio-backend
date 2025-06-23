import openai

# Masukkan API key OpenAI kamu di sini:
openai.api_key = "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"

# Prompt AI yang ingin kamu kirimkan
prompt = "Buatkan cerita edukatif lucu untuk anak-anak tentang persahabatan Plompi dan Lumi."

# Kirim ke OpenAI
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Ambil hasilnya
hasil = response.choices[0].message.content

# Cetak hasil
print("Hasil dari AI:")
print(hasil)

# Simpan ke file (opsional)
with open("hasil_ai.txt", "w", encoding="utf-8") as f:
    f.write(hasil)
