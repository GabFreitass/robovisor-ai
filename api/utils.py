from typing import List, Tuple, Union
from api import client


def transcribe(audio_file, initial_context: str = "") -> str:
    # TODO: take of the errors
    if initial_context == "":
        initial_context = "Esta transcrição deve ser feita em língua portuguesa gramaticamente correta,"
        "mas termos em inglês, acrônimos e siglas estrangeiras podem ocorrer com frequência."

    transcription_response = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text",
        language="pt",
        prompt=initial_context,
        temperature=0.2,
    )
    return transcription_response


def generate_text_response(
    text_input: str, previous_messages: Union[List, None] = None
) -> Tuple[str, List]:

    if previous_messages == []:
        messages = [
            {
                "role": "system",
                "content": "Você é um assistente embarcado em um robô. Você é responsável por response"
                "perguntas de pessoas que interagem com o robô. Você deverá utilizar somente a língua portuguesa falada no Brasil. "
                "O texto que você receberá dos usuários é transcrito a partir da voz deles, portanto fique atento a erros gramaticais, "
                "à presença de termos em inglês, acrônimos e siglas, pois eles podem aparecer no texto de maneira incorreta, "
                "mas você deverá levar isso em conta ao gerar sua resposta."
                "Como um assistente, você deverá guiar os usuários de maneira gentil e dando respostas precisas. A fim de que eles se sintam satisfeitos com "
                "o atendimento e com as suas repsostas. Se não souber responder alguma coisa, tente dizer que não tem conhecimento sobre o assunto.",
            }
        ]
    else:
        messages = previous_messages

    messages.append({"role": "user", "content": f"{text_input}"})

    response = client.chat.completions.create(
        model="gpt-4o", messages=messages, temperature=0.1, max_tokens=2000
    )
    messages.append(
        {"role": "assistant", "content": f"{response.choices[0].message.content}"}
    )

    return response.choices[0].message.content, messages
