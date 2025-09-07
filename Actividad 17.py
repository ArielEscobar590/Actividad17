import tkinter as tk

class Participante:
    def __init__(self, nombrebanda, institucion):
        self._nombrebanda = nombrebanda
        self._institucion = institucion

    def mostrar(self):
        return f"Nombre de la Banda: {self._nombrebanda} - Institución: {self._institucion}"


class BandaEscolar(Participante):
    categorias = ["Primaria", "Básico", "Diversificado"]
    criterios = ["ritmo", "uniformidad", "coreografía", "alineación", "puntualidad"]

    def __init__(self, nombrebanda, institucion, categoria):
        super().__init__(nombrebanda, institucion)
        if categoria not in self.categorias:
            raise ValueError(f"Categoría inválida: {categoria}")
        self._categoria = categoria
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

    def mostrar(self):
        base = super().mostrar()
        if self._puntajes:
            return f"{base} | {self._categoria} | Total: {self.total}"
        else:
            return f"{base} | {self._categoria} | Sin evaluación"


class Concurso:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.bandas = {}

    def inscribir_banda(self, banda: BandaEscolar):
        if banda._nombrebanda in self.bandas:
            raise ValueError("Ya existe una banda con ese nombre")
        self.bandas[banda._nombrebanda] = banda

    def registrar_evaluacion(self, nombre_banda, puntajes):
        if nombre_banda not in self.bandas:
            raise ValueError("Banda no inscrita")
        self.bandas[nombre_banda].registrar_puntajes(puntajes)

    def listar_bandas(self):
        return [b.mostrar() for b in self.bandas.values()]

    def ranking(self):
        def quick_sort(lista):
            if len(lista) <= 1:
                return lista
            pivote = lista[0]
            menores = [x for x in lista[1:] if x.total > pivote.total]
            iguales = [x for x in lista if x.total == pivote.total]
            mayores = [x for x in lista[1:] if x.total < pivote.total]
            return quick_sort(menores) + iguales + quick_sort(mayores)

        return quick_sort(list(self.bandas.values()))


class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.concurso = Concurso("Concurso 14 de Septiembre", "14/09/2025")

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
        win = tk.Toplevel(self.ventana)
        win.title("Inscribir Banda")

        tk.Label(win, text="Nombre de la Banda:").grid(row=0, column=0)
        tk.Label(win, text="Institución:").grid(row=1, column=0)
        tk.Label(win, text="Categoría:").grid(row=2, column=0)

        entry_nombre = tk.Entry(win)
        entry_institucion = tk.Entry(win)
        entry_categoria = tk.Entry(win)

        entry_nombre.grid(row=0, column=1)
        entry_institucion.grid(row=1, column=1)
        entry_categoria.grid(row=2, column=1)

    def registrar_evaluacion(self):
        win = tk.Toplevel(self.ventana)
        win.title("Registrar Evaluación")

    def listar_bandas(self):
        win = tk.Toplevel(self.ventana)
        win.title("Listado de Bandas")

    def ver_ranking(self):
        win = tk.Toplevel(self.ventana)
        win.title("Ranking Final")


if __name__ == "__main__":
    ConcursoBandasApp()
