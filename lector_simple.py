import PyPDF2 as pdf 
def lector_simple(path):

     
     archivo = open(str(path),"rb")
     lector = pdf.PdfReader(archivo)
     pagina = lector.pages[0]
     filtros = (""," ","\n")
     diccionario = {
          "Tara":["Tara"],
          "Neto":["Neto"],
          "Bruto":["Bruto"],
          "Campaña":["Campaña"],
          "CPE":["CPE"],
          "GRANO":["GRANO"],
          "LOCALIDAD":["LOCALIDAD"]
     }
     result={
          
     }
     def determinante_de_limites(text,cm,tm,aca,otraaca):
          y = tm[5]
          x= tm[4]
          if y > 219 and y < 290 and x <298 and x >210 and  text not in filtros:
               if "BRUTO" in text.upper():
                    global y_bruto
                    y_bruto = y-1.5
               elif "TARA" in text.upper():
                    global y_tara
                    y_tara = y-1.5
               elif "NETO" in text.upper():
                    global y_neto
                    y_neto = y-1.5
          elif x >= 471 and y < 793 and y > 780 and text not in filtros:
                    diccionario["CPE"].append(int(text.split("-")[1]))
          
          elif x > 463 and y < 525 and y > 510 and text not in filtros:
               diccionario["Campaña"].append(text) 
               
          elif y >400 and y <500 and x <90 and x >83 and text not in filtros :
                         diccionario["LOCALIDAD"].append(text)
                         
                
                
          elif y > 510 and y < 520  and x > 270 and x < 300  and text not in filtros:
                    diccionario["GRANO"].append(text)

     pagina.extract_text(visitor_text=determinante_de_limites) 

     def visitante(text,cm,tm,aca,otraaca):
          y = tm[5]
          x= tm[4]

          for contador in range(530,770,10):

               if  y >= contador and y < contador + 10 :
                    
                    if x <120 and text != '\n' and text != '':
                         if text not in filtros :
                              diccionario[y]=[text]

                    elif x > 120 and text not in filtros:
                         try:
                          diccionario[y].append(text)
                         except:
                          if text.split(" ")[0] =="CTG:":
                           diccionario[y]=["CTG:",text.split(" ")[1]] 
                          elif y == 759.23:
                              diccionario[y]=["Fecha de arribo",text]
          
                     
          if y > 219 and y < 299 and x > 296 and x <298 and  text not in filtros:

                    try:
                        if  y > y_bruto and y < 270:
                            diccionario['Bruto'].append(int(text)) 
                        elif  y > y_tara and y < y_bruto:
                            diccionario['Tara'].append(int(text))
                        elif  y > 220 and y < y_tara:
                            diccionario['Neto'].append(int(text))
                    except Exception as e:
                        if  y > y_bruto and y < 270:
                            diccionario['Bruto'].append(None) 
                        elif  y > y_tara and y < y_bruto:
                            diccionario['Tara'].append(None)
                        elif  y > 220 and y < y_tara:
                            diccionario['Neto'].append(None)
                            
     pagina.extract_text(visitor_text=visitante)

     for e in diccionario:
        
          if len(diccionario[e])<=1:
               diccionario[e].append(None)


     for e in diccionario:
         result[diccionario[e][0]] = diccionario[e][1]
     print ("diccionario--->",diccionario)
     return  [[result],diccionario]

#print(lector_simple('C:/Users/franc/Descargas 2324/cp/cpe-00000-00002729 SOJA DON FACUNDO GRANELES LOPEZ JOSE.pdf')[0])