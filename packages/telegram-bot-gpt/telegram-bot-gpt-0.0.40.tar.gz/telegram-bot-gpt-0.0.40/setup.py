import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='telegram-bot-gpt',
    version='0.0.40',
    # url='https://github.com/nuggfr/telegram_bot_gpt',
    license='MIT',
    author='Nugroho Fredivianus',
    author_email='nuggfr@gmail.com',
    description='A simple implementation of GPT-Chatbot for Telegram',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['bot_gpt'],
    install_requires=['python_telegram_bot==13.*', 'openai'],
    include_package_data=True,
    keywords='chatbot, artificial intelligence, gpt transformers, nlp',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
