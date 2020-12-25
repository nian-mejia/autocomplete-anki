import main
import time
import boto3
import time
import yaml
from boto3.session import Session

with open(r'aws_key.yaml') as file_aws:
    lista_aws = yaml.full_load(file_aws)
    file_aws.close()


def delete(my_bucket, name_file):
    respuesta = my_bucket.delete_objects(Bucket=lista_aws["buckets"],
                                         Delete={'Objects': [{'Key': name_file}]})
    return respuesta


def status():
    statu = {'scheduled': "en peticion", 'inProgress': "en proceso",
             'completed': "generado", 'failed': "fallido"}

    generado = statu["completed"]
    estado = statu["scheduled"]
    while estado != generado:
        try:
            polly_client = cliente()
            task_status = polly_client.get_speech_synthesis_task(TaskId=taskId)
            s = task_status["SynthesisTask"]["TaskStatus"]
            estado = statu[s]
            if estado == generado:
                print("audio generado")
            time.sleep(5)
        except:
            print("Audio no encontrado")

    if estado == generado:
        global word
        descargar()
        s3 = sessionS3()
        my_bucket = s3.Bucket(lista_aws["buckets"])
        delete(my_bucket, taskId + ".mp3")


def cliente():
    polly_client = boto3.Session(
        aws_access_key_id=lista_aws["access_key_id"],
        aws_secret_access_key=lista_aws["secret_access_key"],
        region_name='us-east-1').client("polly")
    return polly_client


def sessionS3():
    session = Session(aws_access_key_id=lista_aws["access_key_id"],
                      aws_secret_access_key=lista_aws["secret_access_key"],
                      region_name='us-east-1')
    s3 = session.resource('s3')
    return s3


def polly_tarea(word_input):
    global word
    word = word_input
    polly_client = cliente()

    response = polly_client.start_speech_synthesis_task(
        Engine='neural',
        LanguageCode='en-US',
        OutputS3BucketName=lista_aws["buckets"],
        OutputFormat='mp3',
        SampleRate='24000',
        VoiceId='Salli',
        Text=word)

    global taskId
    taskId = response['SynthesisTask']['TaskId']

    word = word.replace(" ", "_") + ".mp3"

    print("Task id is {} ".format(taskId))
    status()
    return word + ".mp3"


def descargar():
    global word

    s3 = sessionS3()
    my_bucket = s3.Bucket(lista_aws["buckets"])

    print("Descargando elemento...")

    my_bucket.download_file(taskId + ".mp3", "{}{}".format(
        lista_aws["root"], word))
    print("Descarga completada")


def solicitud():
    global word
    word = str(input("Ingresa una palabra/oración: ")).lower()
    if not word:
        solicitud()
    return word
