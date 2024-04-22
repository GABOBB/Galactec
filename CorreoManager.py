import yagmail


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
        try:
            self.enviar_correo(destinatario, "Verificación de correo", "Gracias por registrarte en Galatec")
            return True

        except Exception as e:
            print(f"Error al enviar correo de verificación a {destinatario}: {str(e)}")
            return False

    def cerrar_sesion(self):
        self.yag.close()

