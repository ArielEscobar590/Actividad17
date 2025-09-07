import tkinter as tk
class Participante:
    def __init__(self, nombreinst):
        self.nombreinst = nombreinst

    def Mostrar(self):
        print(f" {self.nombreinst}")

class BandaEscolar(Participante):
    categorias = ["Primaria", "Básico", "Diversificado"]
    criterios = ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]

    def __init__(self, nombreinst, categoria):
        super().__init__(nombreinst)
        self._categoria = None
        self._categoria(categoria)
        self._puntajes = {}

    def registrar_puntajes(self, puntajes: dict):
        if set(puntajes.keys()) != set(self.criterios):
            raise ValueError("Faltan o sobran criterios de evaluación")

        for crit, val in puntajes.items():
            if not (0 <= val <= 10):
                raise ValueError(f"El puntaje de {crit} está fuera de rango (0–10)")
        self._puntajes = puntajes

    @property
    def total(self):
        return sum(self._puntajes.values()) if self._puntajes else 0

    @property
    def promedio(self):
        return self.total / len(self._puntajes) if self._puntajes else 0

    def Mostrar(self):
        base = super().Mostrar()
        if self._puntajes:
            return f"{base} | {self._categoria} | Total: {self.total}"
        else:
            return f"{base} | {self._categoria} | Sin evaluación"

class Categoria:
    def revisarcategoria(self, categoria):
        if categoria not in self.categorias:
            ValueError(f"Categoría inválida: {categoria}")
        self.categoria = categoria

class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        tk.Toplevel(self.ventana).title("Inscribir Banda")

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        tk.Toplevel(self.ventana).title("Registrar Evaluación")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        tk.Toplevel(self.ventana).title("Listado de Bandas")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        tk.Toplevel(self.ventana).title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()
