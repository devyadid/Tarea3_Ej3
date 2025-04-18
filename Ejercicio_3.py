# instrumentos.py

from datetime import datetime

class Instrumento:
    """Clase base para instrumentos musicales."""
    def tocar(self):
        """Devuelve un sonido genérico de instrumento."""
        return "Sonido de instrumento"

class Guitarra(Instrumento):
    """Subclase que representa una guitarra."""
    def tocar(self):
        """Sobrescribe tocar() para emitir sonido de guitarra."""
        return "Trrrrr"

class Piano(Instrumento):
    """Subclase que representa un piano."""
    def tocar(self):
        """Sobrescribe tocar() para emitir sonido de piano."""
        return "Plin plin"

class Flauta(Instrumento):
    """Subclase que representa una flauta."""
    def tocar(self):
        """Sobrescribe tocar() para emitir sonido de flauta."""
        return "Piii"

if __name__ == "__main__":
    # Fecha y hora de ejecución (para tu captura de pantalla)
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Ejecución realizada el: {ahora}\n")

    # Instancias y demostración de sonidos
    instrumentos = [
        Instrumento(),
        Guitarra(),
        Piano(),
        Flauta()
    ]
    nombres = [
        "Instrumento genérico",
        "Guitarra",
        "Piano",
        "Flauta"
    ]

    for nombre, inst in zip(nombres, instrumentos):
        print(f"{nombre}: {inst.tocar()}")
