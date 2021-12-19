from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import random
import time
import datetime
import mysql.connector


class Hospital:
	
	#=======FUNCTIONALITY DECLARATION========
	
	def iPrescriptiondata(self):
		if self.NameOfTablets.get()=="" or self.ref.get()=="":
			messagebox.showerror("Error", "All Fields are Required!")
		else:
			conn=mysql.connector.connect(host='localhost', 
																	  user='root', 
																	  passwd='nishu', 
																	  database='myhospitaldata')
			my_cursor=conn.cursor()
			s = "INSERT INTO hospital (tabname , ref , dose , quantity , lot , issuedate , expdate , nhs_no , pname , dob , p_add) VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s)"
			d1=(self.NameOfTablets.get() , self.ref.get() , self.Dose.get() , self.NumberOfTablets.get() , self.Lot.get() , self.IssueDate.get() , self.ExpDate.get() , self.nhsNumber.get() , self.PatientName.get() , self.DateOfBirth.get() , self.PatientAddress.get())
			my_cursor.execute(s,d1)
			conn.commit()
			messagebox. showinfo("Success","Record inserted successfully")
			self.fetch_all_data()
			conn.close()
	
	
	
	def fetch_all_data(self):
		conn=mysql.connector.connect(host='localhost', 
																	  user='root', 
																	  passwd='nishu', 
																      database='myhospitaldata')
		my_cursor=conn.cursor()
		my_cursor.execute("select * from hospital")
		rows=my_cursor.fetchall()
		if len(rows)!=0:
			self.hospital_table.delete(*self.hospital_table.get_children())
			for i in rows:
				self.hospital_table.insert("",END,values=i)
			conn.commit()
		conn.close()
	
	
	
	def get_cursor(self , event=""):
		cursor_row=self.hospital_table.focus()
		content=self.hospital_table.item(cursor_row)
		row=content["values"]
		self.NameOfTablets.set(row[0])
		self.ref.set(row[1])
		self.Dose.set(row[2])
		self.NumberOfTablets.set(row[3])
		self.Lot.set(row[4])
		self.IssueDate.set(row[5])
		self.ExpDate.set(row[6])
		self.nhsNumber.set(row[7])
		self.PatientName.set(row[8])
		self.DateOfBirth.set(row[9])
		self.PatientAddress.set(row[10])
		
	
	def update_data(self):
		conn=mysql.connector.connect(host='localhost', 
																	  user='root', 
																	  passwd='nishu', 
																      database='myhospitaldata')
		my_cursor=conn.cursor()
		d2=(self.NameOfTablets.get() , self.Dose.get() , self.NumberOfTablets.get() , self.Lot.get() , self.IssueDate.get() , self.ExpDate.get() , self.nhsNumber.get() , self.PatientName.get() , self.DateOfBirth.get() , self.PatientAddress.get() , self.ref.get(),)
		my_cursor.execute("update hospital set tabname=%s , dose=%s , quantity=%s , lot=%s , issuedate=%s , expdate=%s , nhs_no=%s , pname=%s , dob=%s , p_add=%s where ref=%s" , d2)
		conn.commit()
		messagebox. showinfo("Success","Record updated successfully")
		self.fetch_all_data()
		conn.close()
	
	
	def iDelete(self):
		conn=mysql.connector.connect(host='localhost', 
																	  user='root', 
																	  passwd='nishu', 
																      database='myhospitaldata')
		my_cursor=conn.cursor()
		query="delete from hospital where ref=%s"
		value=(self.ref.get(),)
		my_cursor.execute(query,value)
		conn.commit()
		conn.close()
		self.fetch_all_data()
		messagebox.showinfo("Delete","Patient record has been deleted successfully")
		
		
		
	
		
	
	def iPrescription(self):
		self.txtPrescription.insert(END,"Name of Tablets:\t\t\t" + self.NameOfTablets.get() + "\n")
		self.txtPrescription.insert(END,"Reference:\t\t\t" + self.ref.get() + "\n")
		self.txtPrescription.insert(END,"Dose:\t\t\t" + self.Dose.get() + "\n")
		self.txtPrescription.insert(END,"No. of Tablets:\t\t\t" + self.NumberOfTablets.get() + "\n")
		self.txtPrescription.insert(END,"Lot:\t\t\t" + self.Lot.get() + "\n")
		self.txtPrescription.insert(END,"Issue Date:\t\t\t" + self.IssueDate.get() + "\n")
		self.txtPrescription.insert(END,"Exp Date:\t\t\t" + self.ExpDate.get() + "\n")
		self.txtPrescription.insert(END,"Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
		self.txtPrescription.insert(END,"Side Effect:\t\t\t" + self.SideEffect.get() + "\n")
		self.txtPrescription.insert(END,"Further Info:\t\t\t" + self.FurtherInformation.get() + "\n")
		self.txtPrescription.insert(END,"Storage:\t\t\t" + self.StorageAdvice.get() + "\n")
		self.txtPrescription.insert(END,"Blood Pressure:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
		self.txtPrescription.insert(END,"Patient Id:\t\t\t" + self.PatientId.get() + "\n")
		self.txtPrescription.insert(END,"NHS No:\t\t\t" + self.nhsNumber.get() + "\n")
		self.txtPrescription.insert(END,"Patient Name:\t\t\t" + self.PatientName.get() + "\n")
		self.txtPrescription.insert(END,"Date of Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
		self.txtPrescription.insert(END,"Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")
	
	
	def iExit(self):
		iExit=messagebox.askyesno("Hospital Management Sysytem" , "Confirm you want to exit")
		if iExit>0:
			root.destroy()
			return
			
				
					
			
	def clear_data(self):
		self.NameOfTablets.set("")
		self.ref.set("")
		self.Dose.set("")
		self.NumberOfTablets.set("")
		self.Lot.set("")
		self.IssueDate.set("")
		self.ExpDate.set("")
		self.DailyDose.set("")
		self.SideEffect.set("")
		self.FurtherInformation.set("")
		self.DrivingUsingMachine.set("")
		self.StorageAdvice.set("")
		self.HowToUseMedication.set("")
		self.PatientId.set("")
		self.nhsNumber.set("")
		self.PatientName.set("")
		self.DateOfBirth.set("")
		self.PatientAddress.set("")
		self.txtPrescription.delete("1.0",END)
	
	
	#=========CREATING UI===============
	def __init__(self,root):
		self.root=root
		self.root.title("Hospital Management System")
		self.root.geometry("1540x800+0+0")
		
		self.NameOfTablets=StringVar()
		self.ref=StringVar()
		self.Dose=StringVar()
		self.NumberOfTablets=StringVar()
		self.Lot=StringVar()
		self.IssueDate=StringVar()
		self.ExpDate=StringVar()
		self.DailyDose=StringVar()
		self.SideEffect=StringVar()
		self.FurtherInformation=StringVar()
		self.StorageAdvice=StringVar()
		self.DrivingUsingMachine=StringVar()
		self.HowToUseMedication=StringVar()
		self.PatientId=StringVar()
		self.nhsNumber=StringVar()
		self.PatientName=StringVar()
		self.DateOfBirth=StringVar()
		self.PatientAddress=StringVar()
		
		
		
		lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hospital Management System", fg="red", bg="white", font=("times new roman",10,"bold"))
		lbltitle.pack(side=TOP,fill=X)
		
		#======DATAFRAME=======
		Dataframe=Frame(self.root,bd=20,relief=RIDGE)
		Dataframe.place(x=0,y=110,width=2210,height=500)
		
		DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE, padx=10,font=("times new roman",4,"bold"),text="Patient Information")
		DataframeLeft.place(x=10,y=5,width=1200,height=450)
		
		DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE, padx=10,font=("times new roman",4,"bold"),text="Prescription")
		DataframeRight.place(x=1210,y=5,width=950,height=450)
		
		#=======BUTTONS==========
		Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
		Buttonframe.place(x=0,y=610,width=2210,height=100)
		
		#=======DETAILS==========
		Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
		Detailsframe.place(x=0,y=710,width=2210,height=300)	
		
		#==========DataframeLeft=========
		lblNameTablet=Label(DataframeLeft,text="Name of Tablet  ", font=("arial",5,"bold"),padx=2,pady=6)
		lblNameTablet.grid(row=0,column=0)
		comNametablet=ttk.Combobox(DataframeLeft, textvariable=self.NameOfTablets ,state="readonly",font=("arial",5,"bold"),width=22)
		comNametablet["values"]=("Select","Lisinopril", "Levothyroxine","Azithromycin","Metformin","Lipitor","Amlodipine","Amoxicillin","Hydrochlorothiazide")
		comNametablet.current(0)
		comNametablet.grid(row=0,column=1)
		
		lblref=Label(DataframeLeft,text="Reference", font=("arial",5,"bold"),padx=2)
		lblref.grid(row=1,column=0,sticky=W)
		textref=Entry(DataframeLeft,font=("arial",5,"bold"), textvariable=self.ref ,width=23)
		textref.grid(row=1,column=1)
		
		lblDose=Label(DataframeLeft,text="Dose", font=("arial",5,"bold"),padx=2,pady=4)
		lblDose.grid(row=2,column=0,sticky=W)
		textDose=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.Dose ,width=23)
		textDose.grid(row=2,column=1)
		
		lblNoOfTablets=Label(DataframeLeft,text="No. Of Tablets", font=("arial",5,"bold"),padx=2,pady=6)
		lblNoOfTablets.grid(row=3,column=0,sticky=W)
		textNoOfTablets=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.NumberOfTablets,width=23)
		textNoOfTablets.grid(row=3,column=1)
		
		lblLot=Label(DataframeLeft,text="Lot", font=("arial",5,"bold"),padx=2,pady=6)
		lblLot.grid(row=4,column=0,sticky=W)
		textLot=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.Lot,width=23)
		textLot.grid(row=4,column=1)
		
		lblIssueDate=Label(DataframeLeft,text="Issue Date", font=("arial",5,"bold"),padx=2,pady=6)
		lblIssueDate.grid(row=5,column=0,sticky=W)
		textIssueDate=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.IssueDate,width=23)
		textIssueDate.grid(row=5,column=1)
		
		lblExpDate=Label(DataframeLeft,text="Expiry Date", font=("arial",5,"bold"),padx=2,pady=6)
		lblExpDate.grid(row=6,column=0,sticky=W)
		textExpDate=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.ExpDate,width=23)
		textExpDate.grid(row=6,column=1)
		
		lblDailyDose=Label(DataframeLeft,text="Daily Dose", font=("arial",5,"bold"),padx=2,pady=6)
		lblDailyDose.grid(row=7,column=0,sticky=W)
		textDailyDose=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.DailyDose,width=23)
		textDailyDose.grid(row=7,column=1)
		
		lblSideEffect=Label(DataframeLeft,text="Side Effect", font=("arial",5,"bold"),padx=2,pady=6)
		lblSideEffect.grid(row=8,column=0,sticky=W)
		textSideEffect=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.SideEffect,width=23)
		textSideEffect.grid(row=8,column=1)

		# ==========NOW RIGHT SIDE ENTRIES===========
		
		lblFurtherInfo=Label(DataframeLeft,text="Further Info", font=("arial",5,"bold"),padx=2)
		lblFurtherInfo.grid(row=0,column=2,sticky=W)
		textFurtherInfo=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.FurtherInformation,width=23)
		textFurtherInfo.grid(row=0,column=3)
		
		lblBloodPressure=Label(DataframeLeft,text="Blood Pressure", font=("arial",5,"bold"),padx=2,pady=6)
		lblBloodPressure.grid(row=1,column=2,sticky=W)
		textBloodPressure=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.DrivingUsingMachine,width=23)
		textBloodPressure.grid(row=1,column=3)
		
		lblStorage=Label(DataframeLeft,text="Storage", font=("arial",5,"bold"),padx=2,pady=6)
		lblStorage.grid(row=2,column=2,sticky=W)
		textStorage=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.StorageAdvice,width=23)
		textStorage.grid(row=2,column=3)
		
		lblMedication=Label(DataframeLeft,text="Medication", font=("arial",5,"bold"),padx=2,pady=6)
		lblMedication.grid(row=3,column=2,sticky=W)
		textMedication=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.HowToUseMedication,width=23)
		textMedication.grid(row=3,column=3)
		
		lblPatientId=Label(DataframeLeft,text="Patient ID", font=("arial",5,"bold"),padx=2,pady=6)
		lblPatientId.grid(row=4,column=2,sticky=W)
		textPatientId=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.PatientId,width=23)
		textPatientId.grid(row=4,column=3)
		
		lblNhsNumber=Label(DataframeLeft,text="NHS Number", font=("arial",5,"bold"),padx=2,pady=6)
		lblNhsNumber.grid(row=5,column=2,sticky=W)
		textNhsNumber=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.nhsNumber,width=23)
		textNhsNumber.grid(row=5,column=3)
		
		lblPatientName=Label(DataframeLeft,text="Patient Name", font=("arial",5,"bold"),padx=2,pady=6)
		lblPatientName.grid(row=6,column=2,sticky=W)
		textPatientName=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.PatientName,width=23)
		textPatientName.grid(row=6,column=3)
		
		lblDateOfBirth=Label(DataframeLeft,text="Date Of Birth", font=("arial",5,"bold"),padx=2,pady=6)
		lblDateOfBirth.grid(row=7,column=2,sticky=W)
		textDateOfBirth=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.DateOfBirth,width=23)
		textDateOfBirth.grid(row=7,column=3)
		
		lblPatientAddress=Label(DataframeLeft,text="Patient Address", font=("arial",5,"bold"),padx=2,pady=6)
		lblPatientAddress.grid(row=8,column=2,sticky=W)
		textPatientAddress=Entry(DataframeLeft,font=("arial",5,"bold"),textvariable=self.PatientAddress,width=23)
		textPatientAddress.grid(row=8,column=3)
		
		#==========DATAFRAMERIGHT========
		self.txtPrescription=Text(DataframeRight, font=("arial",5,"bold"),width=60,height=11.5,padx=2,pady=6)
		self.txtPrescription.grid(row=0,column=0)
		
		#============BUTTONS==============
		btnPrescription = Button(Buttonframe, command=self.iPrescription ,text = 'Prescription' , fg="white", bg="green",bd='5', font=("arial",6,"bold"), padx=100, pady=4)
		btnPrescription.grid(row=0,column=0)
		
		btnPrescriptiondata = Button(Buttonframe, text = 'Prescription Data' , fg="white", bg="green",bd='5', font=("arial",6,"bold"), padx=100, pady=4, command=self.iPrescriptiondata)
		btnPrescriptiondata.grid(row=0,column=1)
		
		btnUpdate = Button(Buttonframe, command=self.update_data , text = 'Update' , fg="white", bg="green",bd='5', font=("arial",6,"bold"), padx=100, pady=4)
		btnUpdate.grid(row=0,column=2)
		
		btnDelete = Button(Buttonframe, command=self.iDelete , text = 'Delete' , fg="white", bg="green",bd='5', font=("arial",6,"bold"), padx=100, pady=4)
		btnDelete.grid(row=0,column=3)
		
		btnReset = Button(Buttonframe, command=self.clear_data , text = 'Reset' , fg="white", bg="green",bd='5', font=("arial",6,"bold"), padx=100, pady=4)
		btnReset.grid(row=0,column=4)
		
		btnExit = Button(Buttonframe, command=self.iExit , text = 'Exit' , fg="white", bg="green",bd='5', font=("arial",6,"bold"), padx=140, pady=4)
		btnExit.grid(row=0,column=5)
		
		#===========Table===============
		scroll_x=ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(Detailsframe, orient=VERTICAL)
		
		self.hospital_table=ttk.Treeview(Detailsframe, column=("nameoftablet", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "nhsnumber", "pname", "dob", "address"), xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM , fill=X)
		scroll_y.pack(side=RIGHT , fill=Y)
		
		style=ttk.Style()
		style.configure("Treeview", rowheight=30 , font=("arial", 4, "bold"))
		style.configure("Treeview.Heading", font=("arial", 4))
		
		
		scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
		scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
		
		
		self.hospital_table.heading("nameoftablet" , text= "Tablet Name")
		self.hospital_table.heading("ref" , text= "Ref.")
		self.hospital_table.heading("dose" , text= "Dose")
		self.hospital_table.heading("nooftablets" , text= "Quantity")
		self.hospital_table.heading("lot" , text= "Lot")
		self.hospital_table.heading("issuedate" , text= "Issue Date")
		self.hospital_table.heading("expdate" , text= "Exp Date")
		self.hospital_table.heading("nhsnumber" , text= "NHS No.")
		self.hospital_table.heading("pname" , text= "Name")
		self.hospital_table.heading("dob" , text= "DOB")
		self.hospital_table.heading("address" , text= "Add.")
		
		self.hospital_table["show"]="headings"
		
		self.hospital_table.column("nameoftablet",width=170)
		self.hospital_table.column("ref" , width=70)
		self.hospital_table.column("dose" , width=70)
		self.hospital_table.column("nooftablets" , width=100)
		self.hospital_table.column("lot" , width=20)
		self.hospital_table.column("issuedate" , width=140)
		self.hospital_table.column("expdate" , width=100)
		self.hospital_table.column("nhsnumber" , width=100)
		self.hospital_table.column("pname" , width=100)
		self.hospital_table.column("dob" , width=70)
		self.hospital_table.column("address" , width=10)
		
		self.hospital_table.pack(fill=BOTH , expand=1)
		self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
		
		
		self.fetch_all_data()
		
																			
root=Tk()
ob=Hospital(root)
root.mainloop()