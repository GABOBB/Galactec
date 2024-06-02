import yagmail
import random

# Clase para manejar el envío de correos electrónicos
class CorreoManager:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
        self.yag = yagmail.SMTP(usuario, password)

    def enviar_correo(self, destinatario, asunto, mensaje):
        self.yag.send(destinatario, asunto, mensaje)
        print(f"Correo enviado a {destinatario}")

    def verificar_correo(self, destinatario):
        random_code = ''.join(random.choices('0123456789', k=5))
        try:
            self.enviar_correo(destinatario, "Verificación de correo", "Gracias por registrarte en Galatec" + "\n" + "Tu código de verificación es: " + random_code)
            return random_code

        except Exception as e:
            print(f"Error al enviar correo de verificación a {destinatario}: {str(e)}")
            return None

    def cerrar_sesion(self):
        self.yag.close()
