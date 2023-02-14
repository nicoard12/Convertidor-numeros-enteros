from tkinter import *
raiz=Tk()
raiz.title("Convertidor")
raiz.config(bg="white")
frame= Frame(raiz)
frame.pack()
label= Label(frame, text="Escriba el texto a convertir", width="22", height="0",font=("Times New Roman",13))
label.grid(row="0", column="0")
texto= Text(frame, width="167",height="20")
texto.grid(row="1",column="0")
scroll= Scrollbar(frame, command=texto.yview,width="20")
scroll.grid(row="1",column="1", sticky="nsew")
texto.config(yscrollcommand=scroll.set)

def BOTON():
	def num2dig(s,i,cars,enteros):
		if (s[i-1] == "0") and (s[i]=="0"):
			numfinal=""
			return numfinal
		elif (s[i-1]=="0"):
			numfinal= cars[s[i]]
			return numfinal
		else:
			num=s[i-1] + s[i]
			if (num in cars):
				return cars[num]
			else:
				num1= int(s[i-1])*10
				string1= enteros[num1]
				numfinal= cars[string1] + " y "+ cars[s[i]]
				return numfinal
	def num2digV2 (s,i,cars,enteros):
		if (s[i-1]=="0"):
			if (s[i]=="1"):
				numfinal= "un"
			else:
				numfinal= cars[s[i]]
			return numfinal
		else:
			num=s[i-1] + s[i]
			if (num in cars):
				if (num == "21"):
					return "veintún"
				else:
					return cars[num]
			else:
				num1= int(s[i-1])*10
				string1= enteros[num1]
				if (s[i]== "1"):
					ultdig= "un"
				else:
					ultdig= cars[s[i]]
				numfinal= cars[string1] + " y "+ ultdig
				return numfinal
	def num3digV2 (s,i,cars,enteros):
		num= s[i-2] + s[i-1] + s[i]
		if (num in cars):
			return cars[num]
		else:
			num1= int(s[i-2])*100
			string1=enteros[num1]
			if (num1 == 100):
				numfinal="ciento "+num2digV2(s,i,cars,enteros)
			else:
				numfinal= cars[string1]+" "+ num2digV2(s,i,cars,enteros)
			return numfinal
	def num3dig(s,i,cars,enteros):
		if (s[i-2] == "0"):
			numfinal= num2dig(s,i,cars,enteros)
			return numfinal
		else:
			num= s[i-2] + s[i-1] + s[i]
			if (num in cars):
				return cars[num]
			else:
				num1= int(s[i-2])*100
				string1=enteros[num1]
				if (num1 == 100):
					numfinal="ciento "+num2dig(s,i,cars,enteros)
				else:
					numfinal= cars[string1]+" "+ num2dig(s,i,cars,enteros)
				return numfinal
	def num4dig(s,i,cars,enteros):
		if (s[i-3]=="0"):
			numfinal= num3dig(s,i,cars,enteros)
			return numfinal
		else:
			num= s[i-3] + s[i-2] + s[i-1]+ s[i]
			if (num in cars):
				return cars[num]
			else:	
				num1=int(s[i-3])*1000
				string1= enteros[num1]
				numfinal= cars[string1]+" "+num3dig(s,i,cars,enteros)
				return numfinal
	def num5dig(s,i,cars,enteros):
		if (s[i-4]=="0"):
			numfinal= num4dig(s,i,cars,enteros)
		else:
			numfinal= num2digV2(s,i-3,cars,enteros)+" mil "+num3dig(s,i,cars,enteros)
		return numfinal
	def num6dig(s,i,cars,enteros):
		if (s[i-5]=="0"):
			numfinal= num5dig(s,i,cars,enteros)
		else:	
			numfinal= num3digV2(s,i-3,cars,enteros)+" mil "+num3dig(s,i,cars,enteros)
		return numfinal
	def num7dig(s,i,cars,enteros):
		if (s[i-6]=="0"):
			numfinal= num6dig(s,i,cars,enteros)
		else:
			dig1= s[i-6]
			if (dig1 == "1"):
				numfinal= "un"+ " millón "+num6dig(s,i,cars,enteros)
			else:
				numfinal= cars[dig1]+ " millones "+ num6dig(s,i,cars,enteros)
		return numfinal
	def num8dig(s,i,cars,enteros):
		if (s[i-7]=="0"):
			numfinal= num7dig(s,i,cars,enteros)
		else:
			numfinal= num2digV2(s,i-6,cars,enteros)+" millones "+num6dig(s,i,cars,enteros)
		return numfinal
	def num9dig(s,i,cars,enteros):
		if (s[i-8]=="0"):
			numfinal= num8dig(s,i,cars,enteros)
		else:
			numfinal= num3digV2(s,i-6,cars,enteros)+" millones "+num6dig(s,i,cars,enteros)
		return numfinal
	def num10dig(s,i,cars,enteros):
		if (s[i-9]=="0"):
			numfinal= num9dig(s,i,cars,enteros)
			return numfinal
		else:
			numfinal= num4dig(s,i-6,cars,enteros)+" millones "+num6dig(s,i,cars,enteros)
			return numfinal
	def num11dig(s,i,cars,enteros):
		if (s[i-10]=="0"):
			numfinal= num10dig(s,i,cars,enteros)
		else:
			numfinal= num5dig(s,i-6,cars,enteros)+" millones "+num6dig(s,i,cars,enteros)
		return numfinal
	def num12dig(s,i,cars,enteros):
		if (s[i-11]=="0"):
			numfinal= num11dig(s,i,cars,enteros)
		else:
			numfinal= num6dig(s,i-6,cars,enteros)+" millones "+num6dig(s,i,cars,enteros)
		return numfinal
	def conversion(s):
		enteros={0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"11",12:"12",13:"13",14:"14",15:"15",16:"16",17:"17",18:"18",19:"19",20:"20",21:"21",22:"22",23:"23",24:"24",25:"25",26:"26",27:"27",28:"28",29:"29",30:"30",40:"40",50:"50",60:"60",70:"70",80:"80",90:"90",100:"100",200:"200",300:"300",400:"400",500:"500",600:"600",700:"700",800:"800",900:"900",1000:"1000",2000:"2000",3000:"3000",4000:"4000",5000:"5000",6000:"6000",7000:"7000",8000:"8000",9000:"9000"}
		cars={"0":"cero","1":"uno","2":"dos","3":"tres","4":"cuatro","5":"cinco","6":"seis","7":"siete","8":"ocho","9":"nueve","10":"diez","11":"once","12":"doce","13":"trece","14":"catorce","15":"quince","16":"dieciséis","17":"diecisiete","18":"dieciocho","19":"diecinueve","20":"veinte","21":"veintiuno","22":"veintidos","23":"veintitres","24":"veinticuatro","25":"veinticinco","26":"veintiséis","27":"veintisiete","28":"veintiocho","29":"veintinueve","30":"treinta","40":"cuarenta","50":"cincuenta","60":"sesenta","70":"setenta","80":"ochenta","90":"noventa","100":"cien","200":"doscientos","300":"trescientos","400":"cuatrocientos","500":"quinientos","600":"seiscientos","700":"setecientos","800":"ochocientos","900":"novecientos","1000":"mil","2000":"dos mil","3000":"tres mil","4000":"cuatro mil","5000":"cinco mil", "6000":"seis mil","7000": "siete mil","8000":"ocho mil","9000":"nueve mil","10000":"diez mil"}
		enumerados={"1":"primero","2":"segundo","3":"tercero","4":"cuarto","5":"quinto","6":"sexto","7":"séptimo","8":"octavo","9":"noveno"}
		i= 0
		final=""
		mayus= True
		while (i <= len(s)-1):
			if (s[i] not in cars):
				final= final + s[i]
				i+=1
				if (s[i-2] == ".") and (s[i-1] == " ") or (s[i-1] == "\n"):
					mayus= True
				else:
					mayus= False
			else:
				dig=0
				x=""
				xi=-1
				while (i < len(s)-1) and (s[i] in cars):
					dig+=1
					x=x+s[i]
					xi+=1
					i+=1
					if (s[i]==".") and (i < len(s)-1) and (s[i+1] in cars):
						i+=1
				if (i == len(s)-1) and (s[i] in cars):
					dig+=1
					x=x+s[i]
					xi+=1
					i+=1
				if (dig == 1):
					if (mayus):
						if (s[i] == "°"):
							final= final + enumerados[s[i-1]].capitalize()
							i+=1
						else:
							final= final + cars[s[i-1]].capitalize()
					else:
						if (s[i] == "°"):
							final= final + enumerados[s[i-1]]
							i+=1
						else:
							final= final + cars[s[i-1]]
				elif (dig == 2):
					if (mayus):
						final= final + num2dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num2dig(x,xi,cars,enteros)
				elif (dig == 3):
					if (mayus):
						final= final + num3dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num3dig(x,xi,cars,enteros)
				elif (dig == 4):
					if (mayus):
						final= final + num4dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num4dig(x,xi,cars,enteros)
				elif (dig == 5):
					if (mayus):
						final= final + num5dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num5dig(x,xi,cars,enteros)
				elif (dig == 6):
					if (mayus):
						final= final + num6dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num6dig(x,xi,cars,enteros)
				elif (dig == 7):
					if (mayus):
						final= final + num7dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num7dig(x,xi,cars,enteros)
				elif (dig == 8):
					if (mayus):
						final= final + num8dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num8dig(x,xi,cars,enteros)
				elif (dig == 9):
					if (mayus):
						final= final + num9dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num9dig(x,xi,cars,enteros)
				elif (dig == 10):
					if (mayus):
						final= final + num10dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num10dig(x,xi,cars,enteros)
				elif (dig == 11):
					if (mayus):
						final= final + num11dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num11dig(x,xi,cars,enteros)
				elif (dig == 12):
					if (mayus):
						final= final + num12dig(x,xi,cars,enteros).capitalize()
					else:
						final= final + num12dig(x,xi,cars,enteros)
		return final 
	pantalla.delete("1.0","end-1c")
	string= texto.get("1.0","end-1c")
	pantalla.insert("1.0", conversion(string))

boton= Button(frame,text="Convertir", command=BOTON)
boton.grid(row="2",column="0")

pantalla= Text(frame, width="167",height="20")
pantalla.grid(row="3",column="0")
scroll2= Scrollbar(frame, command=pantalla.yview,width="20")
scroll2.grid(row="3",column="1", sticky="nsew")
pantalla.config(yscrollcommand=scroll2.set)
raiz.mainloop()