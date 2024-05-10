#en esta ventana habra que usar flet para crear la interface y migrar la ejecucion de las funciones aqui
from flet import *
from lector_multiple import lector_multiple
from lector_transferencia import lector_de_transferencia
from exportador_a_excel import exportar_excel,exportar_excel_simple
from lector_factura_multiple import lector_de_facturas
def data_scraper (page: Page):
    
    page.theme_mode=ThemeMode.DARK
    page.window_height=700
    page.window_width=900
    page.vertical_alignment=MainAxisAlignment.CENTER
    page.horizontal_alignment=CrossAxisAlignment.CENTER
    page.window_center()
    page.title="Extractor de datos"
    path_de_salida=list()
    
    columna_de_paths=Column(scroll=ScrollMode.AUTO)
    
    path_list = []
    
    
    
    def abrir_modal(e,titulo:str,mensaje:str):
        dlg_modal.open = True
        dlg_modal.title=titulo
        dlg_modal.content=mensaje
        page.update()
        
    def cerrar_modal(e):
        dlg_modal.open=False
        page.update()
    dlg_modal = AlertDialog(
        modal=True,
        title=Text(""),
        content=Text(""),
        actions=[
            TextButton("Ok", on_click=cerrar_modal),
        ],
        actions_alignment=MainAxisAlignment.END,
        #on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )
    
    def obtener_path(e:FilePickerResultEvent):
       path_list.clear()
       paths=list(map(lambda f: f.path,e.files))
       files_name=list(map(lambda f: (Text(f.name)),e.files))
       for e in paths:
           path_list.append(e)
       columna_de_paths.controls=files_name
       page.update()

    def salida_seleccionada(e:FilePickerResultEvent):
        path_de_salida.clear()
        text_field_to_write.value = e.files[0].path
        path_de_salida.append(e.files[0].path)
        page.update()
        
    def gestor_de_cp(pathList,archivoDeSalida):
        if len(pathList) > 0:
            try:
                #print(path_list)
                datos = lector_multiple(pathList)
                exportar_excel(datos,(archivoDeSalida[-1]))
            except AttributeError as e:
                
                print(e)
                
                abrir_modal(e=None,titulo="Error de Lectura",
                            mensaje="Se produjo un error al intentar abrir el archivo, por favor intente nuevamente")
        else:
            print("Por favor seleccione al menos un archivo para continuar")
            
            abrir_modal(e=None,titulo="Error",mensaje="Por favor seleccione al menos un archivo para continuar")
           
    def gestor_de_RT(pathList,archivoDeSalida):
        if len(pathList) > 0:
            try:
                datos = lector_de_transferencia(pathList)
                exportar_excel(datos,archivoDeSalida[-1])
            except Exception as e:
                
                print("Se produjo un error al intentar abrir el archivo, por favor intente nuevamente")
                
                abrir_modal(e=None,titulo="Error de Lectura",
                            mensaje="Se produjo un error al intentar abrir el archivo, por favor intente nuevamente")
                
        else:
            print("Por favor seleccione al menos un archivo para continuar")
            
            abrir_modal(e=None,titulo="Error",mensaje="Por favor seleccione al menos un archivo para continuar")
            
    def gestor_de_fact(pathList,archivoDeSalida):
        if len(pathList) > 0:
            if len(pathList)==1:
                try:
                    datos = lector_de_facturas(pathList)
                    exportar_excel_simple(datos,archivoDeSalida[-1])
                except AttributeError as e:
                    print(archivoDeSalida)
                    print("Se produjo un error al intentar abrir el archivo, por favor intente nuevamente")
                        
                    abrir_modal(e=None,titulo="Error de Lectura",
                                mensaje="Se produjo un error al intentar abrir el archivo, por favor intente nuevamente")
            else:
                try:
                    datos = lector_de_facturas(pathList)
                    exportar_excel(datos,archivoDeSalida[-1])
                except AttributeError as e:
                    print(archivoDeSalida)
                    print("Se produjo un error al intentar abrir el archivo, por favor intente nuevamente")
                        
                    abrir_modal(e=None,titulo="Error de Lectura",
                                mensaje="Se produjo un error al intentar abrir el archivo, por favor intente nuevamente")        
        else:
            print("Por favor seleccione al menos un archivo para continuar")
                
            abrir_modal(e=None,titulo="Error",mensaje="Por favor seleccione al menos un archivo para continuar")
        
        
    contenedor_de_path = Container(content=columna_de_paths,width=600,height=300,alignment=alignment.center,border_radius=BorderRadius(20,20,20,20),border=Border(BorderSide(1.5,"white"),BorderSide(1.5,"white"),BorderSide(1.5,"white"),BorderSide(1.5,"white")))
    selector = FilePicker(on_result=obtener_path)
    selector_de_salida = FilePicker(on_result=salida_seleccionada)
    
    
    
    boton_cp=ElevatedButton("Extractor de CP",width=300,height=50,on_click=lambda _: page.go("/ExtractorDeCp"))
    boton_factura=ElevatedButton("Extractor de Facturas",width=300,height=50,on_click= lambda _: page.go("/ExtractorDeFact"))
    boton_rt=ElevatedButton("Extractor de RT",width=300,height=50,on_click= lambda _ : page.go("/ExtractorDeRT"))
    boton_select_file=ElevatedButton(text="Seleccionar archivos",icon="file_open_rounded", on_click=lambda _:selector.pick_files(allow_multiple=True,file_type=FilePickerFileType.CUSTOM,allowed_extensions=["pdf"]))
    boton_select_file_to_write=IconButton(icon="file_open_rounded", on_click=lambda _:selector_de_salida.pick_files(allow_multiple=False,file_type=FilePickerFileType.CUSTOM,allowed_extensions=["xls","xlsx"]))
    boton_home=FloatingActionButton(icon="home",on_click=lambda _ :page.go("/"),mini=True)
    boton_extraer_cp=ElevatedButton(text="Extraer",on_click = lambda _: gestor_de_cp(path_list,path_de_salida))
    boton_extraer_RT=ElevatedButton(text="Extraer",on_click = lambda _: gestor_de_RT(path_list,path_de_salida))
    boton_extraer_fact=ElevatedButton(text="Extraer",on_click = lambda _: gestor_de_fact(path_list,path_de_salida))
    text_field_to_write = TextField(label="Archivo de Salida",hint_text="Seleccione un archivo de Salida",read_only=True,value=path_de_salida,width=page.window_width -250)
    contenedor_de_botones = Column(
            controls=[
                boton_cp,
                boton_factura,
                boton_rt            
            ],
            alignment=alignment.center        
        )
    fila_de_seleccion_de_salida=Row(controls=[boton_select_file_to_write,text_field_to_write],width=page.window_width-200)
    pagina_bienvenida =Column(
            controls=[
                Text("Bienvenido!",theme_style=TextThemeStyle.DISPLAY_SMALL),
                Text("Selecciona el tipo de archivo del que quieres obtener sus datos:",theme_style=TextThemeStyle.LABEL_MEDIUM),
            
                Container(
                    content= contenedor_de_botones,
                    width= 400,
                    height=300,
                    padding=padding.all(30),
           
                )
            ]
        )
    pagina_extractor_cp = Column(
            controls=[
                boton_home,
                contenedor_de_path,
                selector,
                boton_select_file,
                selector_de_salida,
                fila_de_seleccion_de_salida,
                boton_extraer_cp
            ],alignment=MainAxisAlignment.CENTER
        )
    pagina_extractor_RT = Column(
            controls=[
                boton_home,
                contenedor_de_path,
                selector,
                boton_select_file,
                selector_de_salida,
                fila_de_seleccion_de_salida,
                boton_extraer_RT
            ],alignment=MainAxisAlignment.CENTER
        )
    pagina_extractor_fact = Column(
            controls=[
                boton_home,
                contenedor_de_path,
                selector,
                boton_select_file,
                selector_de_salida,
                fila_de_seleccion_de_salida,
                boton_extraer_fact
            ],alignment=MainAxisAlignment.CENTER
        )
    paginas = {
        "/": View(
            
            "/",[pagina_bienvenida],vertical_alignment=MainAxisAlignment.CENTER,horizontal_alignment=CrossAxisAlignment.CENTER
        ),
        "/ExtractorDeCp": View(
            "/ExtractorDeCp",[pagina_extractor_cp],vertical_alignment=MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=CrossAxisAlignment.CENTER,padding=padding.all(40)
        ),
        "/ExtractorDeRT": View(
            "/ExtractorDeRT",[pagina_extractor_RT],vertical_alignment=MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=CrossAxisAlignment.CENTER,padding=padding.all(40)
        ),
        "/ExtractorDeFact":View(
            "/ExtractorDeFact",[pagina_extractor_fact],vertical_alignment=MainAxisAlignment.SPACE_BETWEEN,horizontal_alignment=CrossAxisAlignment.CENTER,padding=padding.all(40)
        )
    }
    def route_change(route):
        path_list.clear()
        path_de_salida.clear()
        page.views.clear()
        page.views.append(
            
        paginas[page.route]
    )

  

    page.on_route_change = route_change
    page.go(page.route)
app(target=data_scraper,name="Extractor de datos")

   
