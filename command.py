import codecs
import os
import re
import click
import requests
from dotenv import load_dotenv
import decrypt

@click.group()
def cli1():
    pass

@cli1.command()
@click.option("--link-photo-face-url", help="Link of your face photo bucket for decrypt",required=True)
@click.option("--destination", help="destination folder",required=True)
def download_photo_face(link_photo_face_url, destination):
    # Get name photo face
    regexp = re.compile("face\/(.*)\?")
    name_file = (regexp.search(link_photo_face_url).group(1)) + '.png'
    path_final_destination = os.path.join(destination, name_file)
    # Download file
    r = requests.get(link_photo_face_url, allow_redirects=False)
    # Decrypt file
    aes_key_bytes = codecs.decode(os.getenv("FACE_IMAGE_AES_KEY"), 'hex')
    decrypt_face = decrypt.decode_and_decrypt(r.content, aes_key_bytes)
    with open(path_final_destination, 'wb') as f:
        f.write(decrypt_face)

@click.group()
def cli2():
    pass

@cli2.command()
@click.option("--link-photo-id-url", help="Link of your photo id bucket for decrypt",required=True)
@click.option("--photo-id-key", help="RSA Key for decrypt",required=True)
@click.option("--destination", help="destination folder",required=True)
def download_photo_id(link_photo_id_url, destination, photo_id_key):

    # Get name photo face
    regexp = re.compile("photo_id\/(.*)\?")
    name_file = (regexp.search(link_photo_id_url).group(1)) + '.png'
    path_final_destination = os.path.join(destination, name_file)
    # Download file
    r = requests.get(link_photo_id_url, allow_redirects=False)
    # Decrypt file
    rsa_priv_key = os.getenv("RSA_PRIVATE_KEY")
    sha_key = decrypt.rsa_decrypt_py3(photo_id_key, rsa_priv_key)
    decrypt_face = decrypt.decode_and_decrypt(r.content,sha_key)
    with open(path_final_destination, 'wb') as f:
        f.write(decrypt_face)

cli = click.CommandCollection(sources=[cli1, cli2])
if __name__ == '__main__':
    load_dotenv()
    cli()

