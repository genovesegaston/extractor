import PyPDF2 as pdf
import lector_simple as ls

#AGREGAR EXTRCCION DE GRANO Y LOCALIDAD DE ORIGEN

def lector_multiple(path_list):
    diccionario = {
        "Tara":[],
          "Neto":[],
          "Bruto":[],
          "Campaña":["Campaña"],
          "CPE":["CPE"],
          "GRANO":["GRANO"],
          "LOCALIDAD":["LOCALIDAD"]
    }
    filtros = (""," ","\n") 
    for  i,path in enumerate(path_list):
        archivo = open(path,"rb")
        lector = pdf.PdfReader(archivo)
        pagina = lector.pages[0]
        
        if i == 0 :
            diccionario = ls.lector_simple(path_list[0])[1]
        else:
            def determinante_de_limites(text,cm,tm,aca,otraaca):
                y = tm[5]
                x= tm[4]
                if y > 219 and y < 290 and x < 296 and x >210 and  text not in filtros:
                    if "BRUTO" in text.upper():
                        global y_bruto 
                        y_bruto = y
                    elif "TARA" in text.upper():
                        global y_tara
                        y_tara = y
                    elif "NETO" in text.upper():
                        global y_neto
                        y_neto = y
                elif x >= 471 and y < 793 and y > 780 and text not in filtros:
                    diccionario["CPE"].append(int(text.split("-")[1]))
          
                elif x > 463 and y < 525 and y > 510 and text not in filtros:
                    diccionario["Campaña"].append(text)
                elif y >400 and y <500 and x <90 and x >83 and text not in filtros:
                         diccionario["LOCALIDAD"].append(text)

                
                elif y > 510 and y < 520  and x > 270 and x < 300 and text not in filtros:
                     if len(text)>0:
                        diccionario["GRANO"].append(text)

            pagina.extract_text(visitor_text=determinante_de_limites)   
        
            def visitante(text,cm,tm,aca,otraaca):
                y = tm[5]
                x= tm[4]
                for contador in range(520,780,10):

                    if  y >= contador and y < contador + 10 :
                            if x > 120 and text not in filtros:
                                try:
                                    if y != 762.15:
                                     diccionario[y].append(text)
                                    else:
                                     diccionario[y].append(text.split(" ")[1])
                                except:
                                    pass
                                
                if y > 219 and y < 290 and x > 296 and x <298 and  text not in filtros:
                    
                    try:
                        global y_bruto
                        global y_tara 
                            
                        if  y > y_bruto and y < 290:
                            diccionario['Bruto'].append(int(text))
                        elif  y >= y_tara and y < y_bruto:
                            diccionario['Tara'].append(int(text))
                        elif  y > 220 and y < y_tara:
                            diccionario['Neto'].append(int(text))
                    except Exception as e:
                        if  y > y_bruto and y < 290:
                            diccionario['Bruto'].append(None) 
                        elif  y > y_tara and y < y_bruto:
                            diccionario['Tara'].append(None)
                        elif  y > 220 and y < y_tara:
                            diccionario['Neto'].append(None)
                            
            pagina.extract_text(visitor_text=visitante)
            for el in diccionario:
                 if len(diccionario[el])<i+2:
                    diccionario[el].append(None)
    #print (diccionario)       
    return diccionario
""" print(lector_multiple(('C:/Users/franc/Descargas 2324/cp/cpe-00000-00002729 SOJA DON FACUNDO GRANELES LOPEZ JOSE.pdf','C:/Users/franc/Descargas 2324/cp/cpe-00000-00002730 SOJA DON FACUNDO FRIAS FELIPA.pdf','C:/Users/franc/Descargas 2324/cp/cpe-00000-00002728 SOJA RANCHO TEXTURAR FRIAS.pdf','C:/Users/franc/Descargas 2324/cp/cpe-00000-00002726.pdf',
'C:/Users/franc/Descargas 2324/cp/cpe-00000-00002725.pdf'))) """