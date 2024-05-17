import PyPDF2 as lector
from lector_simple import lector_simple
from lector_multiple import lector_multiple
from exportador_a_excel import exportar_excel,exportar_excel_simple

def lector_de_test(path): 
    filtros = (""," ","\n")
    result={}
    for element in path:
        archivo = open(element,"rb")
        reader = lector.PdfReader(archivo)
        pagina = reader.pages[0]
        
        def visitante(text,nn,tm,nnn,nnnn):
            
            
            y=tm[5]
            x=tm[4]
            
            if text not in filtros:
                if text == "C - PROCEDENCIA":
                   
                    global y_procedencia  
                    y_procedencia = y +1
                elif text == "D - DESTINO DE LA MERCADERÍA":
                    global y_destino
                    y_destino = y +1
                
                if y >400 and y <500 and x <90 and x >83 :
                    print(text ,x, y)
                
                
                elif y > 510 and y < 520  and x > 270 and x < 300 :
                    print(text, x,y)

        try:
            pagina.extract_text(visitor_text=visitante)
            print(f'y procedencia {y_procedencia}  y destino {y_destino}')
        except:
            pass
    return result
#lector_de_test(["C:\\Users\\franc\\Descargas 2324\\cp\\cpe-00000-00002688.pdf"])
exportar_excel(lector_multiple((['C:\\Users\\franc\\Descargas 2324\\cp\\cpe-00000-00002687.pdf',
                        'C:\\Users\\franc\\Descargas 2324\\cp\\cpe-00000-00002688.pdf'
                        ])))


