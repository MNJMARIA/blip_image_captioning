# Image Captioning with BLIP

![Demo](test_blip_image_captioning.png)  <!-- замініть на реальне зображення -->

Цей проєкт використовує модель [BLIP (Bootstrapping Language-Image Pre-training)](https://huggingface.co/Salesforce/blip-image-captioning-base) від Salesforce для автоматичного створення текстових описів до завантажених зображень. Інтерфейс побудований за допомогою бібліотеки Gradio.

## Особливості
- Генерація природномовного підпису до будь-якого зображення.
- Простий веб-інтерфейс (перетягніть файл або виберіть через провідник).
- Оптимізовані параметри генерації для уникнення повторень (`repetition_penalty`, `no_repeat_ngram_size`).
- Автоматична конвертація зображень у формат RGB (підтримка PNG з прозорістю).

## Встановлення

1. Клонуйте репозиторій:
   ```bash
   git clone https://github.com/MNJMARIA/blip-image-captioning.git
   cd blip-image-captioning
