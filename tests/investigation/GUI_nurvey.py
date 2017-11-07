import gi
import numpy
from keras.models import model_from_json
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

dataset = [2,47,0,2,2,1,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1]


cobertura = Gtk.CheckButton("Cobertura medica")
subsidio = Gtk.CheckButton("Subsidio")
categoria = Gtk.Label("")

estado1 = Gtk.RadioButton.new_with_label_from_widget(None, "Ocupado")
estado2 = Gtk.RadioButton.new_with_label_from_widget(estado1, "Inactivo")
estado3 = Gtk.RadioButton.new_with_label_from_widget(estado1, "Desocupado")
inactivo1 = Gtk.RadioButton.new_with_label_from_widget(None, "becado o nada")
inactivo2 = Gtk.RadioButton.new_with_label_from_widget(inactivo1, "jubilado")
inactivo3 = Gtk.RadioButton.new_with_label_from_widget(inactivo1, "rentista")
ocupa1 = Gtk.RadioButton.new_with_label_from_widget(None, "relac depend")
ocupa2 = Gtk.RadioButton.new_with_label_from_widget(ocupa1, "cuenta propia")
ocupa3 = Gtk.RadioButton.new_with_label_from_widget(ocupa1, "empleador")
jerarquia1 = Gtk.RadioButton.new_with_label_from_widget(None, "sin jerarquia")
jerarquia2 = Gtk.RadioButton.new_with_label_from_widget(jerarquia1, "jefe intermedio")
jerarquia3 = Gtk.RadioButton.new_with_label_from_widget(jerarquia1, "directivo")
califlaboral1 = Gtk.RadioButton.new_with_label_from_widget(None, "no calif")
califlaboral2 = Gtk.RadioButton.new_with_label_from_widget(califlaboral1, "operat")
califlaboral3 = Gtk.RadioButton.new_with_label_from_widget(califlaboral1, "tecnico")
califlaboral4 = Gtk.RadioButton.new_with_label_from_widget(califlaboral1, "prof")
intensidad1 = Gtk.RadioButton.new_with_label_from_widget(None, "menos de 35 hs")
intensidad2 = Gtk.RadioButton.new_with_label_from_widget(intensidad1, "mas de 35 hs")
tamanio1 = Gtk.RadioButton.new_with_label_from_widget(None, "hasta 5 pers")
tamanio2 = Gtk.RadioButton.new_with_label_from_widget(tamanio1, "de 6 a 40 pers")
tamanio3 = Gtk.RadioButton.new_with_label_from_widget(tamanio1, "de 41 a 200 pers")
tamanio4 = Gtk.RadioButton.new_with_label_from_widget(tamanio1, "mas de 200 personas pers")
tamanio5 = Gtk.RadioButton.new_with_label_from_widget(tamanio1, "nada")

sexo1 = Gtk.RadioButton.new_with_label_from_widget(None, "Masculino")
sexo2 = Gtk.RadioButton.new_with_label_from_widget(sexo1, "Femenino")
educacion1 = Gtk.RadioButton.new_with_label_from_widget(None, "Primario")
educacion2 = Gtk.RadioButton.new_with_label_from_widget(educacion1, "Secundario")
educacion3 = Gtk.RadioButton.new_with_label_from_widget(educacion1, "Universitario")

edad = Gtk.Entry()
edad.set_text("edad: 25")
Miembros = Gtk.Entry()
Miembros.set_text("Cant. Miembros Familiares")
Aportantes = Gtk.Entry()
Aportantes.set_text("Cant. Miembros Aportantes")


class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))


class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ListBox Demo")
        self.set_border_width(20)

        #wraper global de la ventana
        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        # Sexo seccion vector[0] =================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(sexo1, False, False, 0)
        hbox.pack_start(sexo2, False, False, 0)

        listbox.add(row)
        # Edad seccion vector[1]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        hbox.pack_start(edad, False, False, 0)

        listbox.add(row)
        # Subsidio seccion vector[2]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(subsidio, False, True, 0)

        listbox.add(row)
        # Miembros seccion vector[3] =================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(Miembros, False, False, 0)

        listbox.add(row)
        # Aportantes seccion vector[4] =================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(Aportantes, False, False, 0)

        listbox.add(row)
        # Educacion seccion vector[5 6 7]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(educacion1, False, False, 0)
        hbox.pack_start(educacion2, False, False, 0)
        hbox.pack_start(educacion3, False, False, 0)

        listbox.add(row)
        # Estado seccion vector[8 9]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(estado1, False, False, 0)
        hbox.pack_start(estado2, False, False, 0)
        hbox.pack_start(estado3, False, False, 0)

        listbox.add(row)
        # Inactivo seccion vector[10 11]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(inactivo1, False, False, 0)
        hbox.pack_start(inactivo2, False, False, 0)
        hbox.pack_start(inactivo3, False, False, 0)

        listbox.add(row)
        # Ocupacion seccion vector[12 13]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(ocupa1, False, False, 0)
        hbox.pack_start(ocupa2, False, False, 0)
        hbox.pack_start(ocupa3, False, False, 0)

        listbox.add(row)
        # Jerarquia seccion vector[14 15]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(jerarquia1, False, False, 0)
        hbox.pack_start(jerarquia2, False, False, 0)
        hbox.pack_start(jerarquia3, False, False, 0)

        listbox.add(row)
        # Calificacion seccion vector[16 17 18]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(califlaboral1, False, False, 0)
        hbox.pack_start(califlaboral2, False, False, 0)
        hbox.pack_start(califlaboral3, False, False, 0)
        hbox.pack_start(califlaboral4, False, False, 0)

        listbox.add(row)
        # intensidad seccion vector[19]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(intensidad1, False, False, 0)
        hbox.pack_start(intensidad2, False, False, 0)

        listbox.add(row)
        # Tamanio seccion vector[20 21 22]=================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(tamanio1, False, False, 0)
        hbox.pack_start(tamanio2, False, False, 0)
        hbox.pack_start(tamanio3, False, False, 0)
        hbox.pack_start(tamanio4, False, False, 0)
        hbox.pack_start(tamanio5, False, False, 0)

        listbox.add(row)
        # cobertura seccion vector[23] =================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        hbox.pack_start(cobertura, False, True, 0)

        listbox.add(row)

        # Tercera seccion =================================
        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)

        button = Gtk.Button.new_with_mnemonic("Check")
        button.connect("clicked", self.on_open_clicked)

        hbox.pack_start(button, True, True, 0)
        hbox.pack_start(categoria, True,True,0)
        listbox.add(row)

    def on_open_clicked(self, button):

        # verifica sexo vector[0]
        if (sexo1.get_active()):
            dataset[0] = 1
        else:
            dataset[0] = 2

        #verifica edad vector[1]
        dataset[1] = float(edad.get_text())

        #verifica subsidio vector[2]
        if (subsidio.get_active()):
            dataset[2] = 1
        else:
            dataset[2] = 0

        #Verifica miembros vector[3]
        dataset[3] = float(Miembros.get_text())

        # Verifica aportantes vector[4]
        dataset[4] = float(Aportantes.get_text())

        #Verifica estudios vector[5 6 7]
        if (educacion1.get_active()):
            dataset[5] = 1
            dataset[6] = 0
            dataset[7] = 0
        elif (educacion2.get_active()):
            dataset[5] = 1
            dataset[6] = 1
            dataset[7] = 0
        else:
            dataset[5] = 1
            dataset[6] = 1
            dataset[7] = 1

        # Verifica estado vector[8 9]
        if (estado1.get_active()):
            dataset[8] = 1
            dataset[9] = 1
        elif (estado2.get_active()):
            dataset[8] = 0
            dataset[9] = 0
        else:
            dataset[8] = 1
            dataset[9] = 0

        # Verifica inactivo vector[10 11]
        if (inactivo1.get_active()):
            dataset[10] = 0
            dataset[11] = 0
        elif (inactivo2.get_active()):
            dataset[10] = 1
            dataset[11] = 0
        else:
            dataset[10] = 1
            dataset[11] = 1

        # Verifica ocupado vector[12 13]
        if (ocupa1.get_active()):
            dataset[12] = 0
            dataset[13] = 0
        elif (ocupa2.get_active()):
            dataset[12] = 1
            dataset[13] = 0
        else:
            dataset[12] = 1
            dataset[13] = 1

        # Verifica jerarquia vector[14 15]
        if (jerarquia1.get_active()):
            dataset[14] = 0
            dataset[15] = 0
        elif (jerarquia2.get_active()):
            dataset[14] = 1
            dataset[15] = 0
        else:
            dataset[14] = 1
            dataset[15] = 1

        # Verifica calificacion vector[16 17 18]
        if (califlaboral1.get_active()):
            dataset[16] = 0
            dataset[17] = 0
            dataset[18] = 0
        elif (califlaboral2.get_active()):
            dataset[16] = 1
            dataset[17] = 0
            dataset[18] = 0
        elif (califlaboral3.get_active()):
            dataset[16] = 1
            dataset[17] = 1
            dataset[18] = 0
        else:
            dataset[16] = 1
            dataset[17] = 1
            dataset[18] = 1

        # verifica intensidad vector[19]
        if (intensidad1.get_active()):
            dataset[19] = 0
        else:
            dataset[19] = 1

        # Verifica tamanio vector[20 21 22]
        if (tamanio1.get_active()):
            dataset[20] = 0
            dataset[21] = 0
            dataset[22] = 0
        elif (tamanio2.get_active()):
            dataset[20] = 1
            dataset[21] = 0
            dataset[22] = 0
        elif (tamanio3.get_active()):
            dataset[20] = 1
            dataset[21] = 1
            dataset[22] = 0
        elif (tamanio4.get_active()):
            dataset[20] = 1
            dataset[21] = 1
            dataset[22] = 1
        else:
            dataset[20] = 0
            dataset[21] = 0
            dataset[22] = 0

        #verifica cobertura vector[23]
        if (cobertura.get_active()):
            dataset[23] = 0
        else:
            dataset[23] = 1

        print(dataset)
        print("======")
        dataset2 = numpy.vstack([dataset, dataset])
        print(dataset2)

        salida = loaded_model.predict(dataset2[:, 0:24])
        i,j = numpy.unravel_index(salida.argmax(), salida.shape)
        print("==============================")
        print("==============================")
        print("salida:")
        print(salida)
        print("categoria")
        categoria.set_text(str(j))
        print(j)


win = ListBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()