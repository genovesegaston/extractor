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
                if text == "Campaña:":
                    print(x,y)
                elif text == "N° CPE:":
                    print("cpe",x,y)
                elif x >= 471 and y < 793.23 and y > 780 and text not in filtros:
                    print(int(text.split("-")[1]),y)
                elif x > 463 and y < 525 and y > 510 and text not in filtros:
                    print("campaña",text,y)
                """ if y >225 and y < 265 and x> 210 and x < 298:
                    if y not in result.keys():
                        result[y]= [text]
                    if y in result.keys():
                        result[y].append(text) """
        try:
            pagina.extract_text(visitor_text=visitante)
        except:
            pass
    return result
#print(lector_de_test(["C:\\Users\\franc\\Descargas 2324\\cp\\cpe-00000-00002688.pdf"]))
exportar_excel(lector_multiple((['C:\\Users\\franc\\Descargas 2324\\cp\\cpe-00000-00002687.pdf',
                        'C:\\Users\\franc\\Descargas 2324\\cp\\cpe-00000-00002688.pdf'
                        ])))


