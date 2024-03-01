import customtkinter as ctk
import numbers

class MyCustomUI:

    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        def calcCircularPitch():
            # given module
            try:
                if circularpitchtext_field.get() == "0" and isinstance(float(moduletext_field.get()), numbers.Number) and float(moduletext_field.get()) > 0:
                    val = float(moduletext_field.get()) * 22 / 7
                    circularpitchtext_field.delete(0, ctk.END)
                    circularpitchtext_field.insert(0, val)
                    return True
            except Exception as e:
                print(str("e"))
                return True
            
            # given tooth thickness
            try:
                if circularpitchtext_field.get() == "0" and isinstance(float(toothwidthtext_field.get()), numbers.Number) and float(toothwidthtext_field.get()) > 0:
                    val = float(toothwidthtext_field.get()) * 2
                    circularpitchtext_field.delete(0, ctk.END)
                    circularpitchtext_field.insert(0, val)
                    return True
            except Exception as e:
                print(str("e"))
                return True
        
        def calcNumberOfTeeth():
            # given number of pcd and module
            try:
                if teethcounttext_field.get() == "0" and isinstance(float(pcdtext_field.get()), numbers.Number) and float(pcdtext_field.get()) > 0 and isinstance(float(moduletext_field.get()), numbers.Number) and float(moduletext_field.get()) > 0:
                    val = float(pcdtext_field.get()) * float(moduletext_field.get())
                    teethcounttext_field.delete(0, ctk.END)
                    teethcounttext_field.insert(0, val)
                    return True
            except Exception as e:
                print(str("e"))
                return True
            return 0
        
        def calcAdd():
            try:
                if addtext_field.get() == "0" and isinstance(float(moduletext_field.get()), numbers.Number) and float(moduletext_field.get()) > 0:
                    val = float(moduletext_field.get())
                    addtext_field.delete(0, ctk.END)
                    addtext_field.insert(0, val)
                    return True
            except Exception as e:
                print(str("e"))
                return True
        
        def calcDed():
            try:
                if dedtext_field.get() == "0" and isinstance(float(moduletext_field.get()), numbers.Number) and float(moduletext_field.get()) > 0:
                    val = float(moduletext_field.get()) * 1.25
                    dedtext_field.delete(0, ctk.END)
                    dedtext_field.insert(0, val)
                    return True
            except Exception as e:
                print(str("e"))
                return True
        
        def calcFR():
            try:
                if frtext_field.get() == "0" and isinstance(float(moduletext_field.get()), numbers.Number) and float(moduletext_field.get()) > 0:
                    val = float(moduletext_field.get()) * 0.3
                    frtext_field.delete(0, ctk.END)
                    frtext_field.insert(0, val)
                    return True
            except Exception as e:
                print(str("e"))
                return True
        
        def calcToothWidth():
            try:
                if toothwidthtext_field.get() == "0" and isinstance(float(circularpitchtext_field.get()), numbers.Number) and float(circularpitchtext_field.get()) > 0:
                    val = float(circularpitchtext_field.get()) / 2
                    toothwidthtext_field.delete(0, ctk.END)
                    toothwidthtext_field.insert(0, val)
                    return True
            except Exception as e:
                print(str("e"))
                return True
        
        def calcModule():
            try:
                # given pcd and number of teeth
                if moduletext_field.get() == "0" and isinstance(float(pcdtext_field.get()), numbers.Number) and float(pcdtext_field.get()) > 0 and isinstance(float(teethcounttext_field.get()), numbers.Number) and float(teethcounttext_field.get()) > 0:
                    val = float(pcdtext_field.get()) / float(teethcounttext_field.get())
                    moduletext_field.delete(0, ctk.END)
                    moduletext_field.insert(0, val)
                    return True
                
                # given Addendum
                try:
                    if moduletext_field.get() == "0" and isinstance(float(addtext_field.get()), numbers.Number) and float(addtext_field.get()) > 0:
                        val = float(addtext_field.get())
                        moduletext_field.delete(0, ctk.END)
                        moduletext_field.insert(0, val)
                        return True
                except Exception as e:
                    print(str("e"))
                    return True
                
                # given Dedendum
                try:
                    if moduletext_field.get() == "0" and isinstance(float(dedtext_field.get()), numbers.Number) and float(dedtext_field.get()) > 0:
                        val = float(dedtext_field.get()) / 1.25
                        moduletext_field.delete(0, ctk.END)
                        moduletext_field.insert(0, val)
                        return True
                except Exception as e:
                    print(str("e"))
                    return True
                
                # given Fillet Radius
                try:
                    if moduletext_field.get() == "0" and isinstance(float(dedtext_field.get()), numbers.Number) and float(dedtext_field.get()) > 0:
                        val = float(dedtext_field.get()) / 0.3
                        moduletext_field.delete(0, ctk.END)
                        moduletext_field.insert(0, val)
                        return True
                except Exception as e:
                    print(str("e"))
                    return True
                
            except Exception as e:
                print(e)
                return True
        
        def calcPitchCircleDiameter():
            try:
                # given module and number of teeth
                if pcdtext_field.get() == "0" and isinstance(float(moduletext_field.get()), numbers.Number) and float(moduletext_field.get()) > 0 and isinstance(float(teethcounttext_field.get()), numbers.Number) and float(teethcounttext_field.get()) > 0:
                    val = float(moduletext_field.get()) * float(teethcounttext_field.get())
                    pcdtext_field.delete(0, ctk.END)
                    pcdtext_field.insert(0, val)
                    return True
            except Exception as e:
                print(e)
                return True
        
        def clearFields():
            # pcd
            pcdtext_field.delete(0, ctk.END)
            pcdtext_field.insert(0,0)
            # module
            moduletext_field.delete(0, ctk.END)
            moduletext_field.insert(0,0)
            # circular pitch
            circularpitchtext_field.delete(0, ctk.END)
            circularpitchtext_field.insert(0,0)
            # number of teeth
            teethcounttext_field.delete(0, ctk.END)
            teethcounttext_field.insert(0,0)
            # tooth width 
            toothwidthtext_field.delete(0, ctk.END)
            toothwidthtext_field.insert(0,0)
            # addendum
            addtext_field.delete(0, ctk.END)
            addtext_field.insert(0,0)
            # dedendum
            dedtext_field.delete(0, ctk.END)
            dedtext_field.insert(0,0)
            # fillet radius
            frtext_field.delete(0, ctk.END)
            frtext_field.insert(0,0)
            return True
        
        def updateButtonClick():
            if calcButton._text == "Clear":
                clearFields()
                calcButton.configure(text="Calculate")
            elif calcButton._text == "Calculate":
                calcButton.configure(text="Clear")
                for _ in range(2):
                    calcPitchCircleDiameter()
                    calcModule()
                    calcAdd()
                    calcDed()
                    calcFR()
                    calcCircularPitch()
                    calcNumberOfTeeth()
                    calcToothWidth()
            return True
            
        
               
        self.root = ctk.CTk()
        self.root.title("My Custom UI")
        self.root.geometry("1024x768")  # Set the window size
        
        leftframe = ctk.CTkScrollableFrame(self.root)
        leftframe.pack(padx=60, pady=20, side="left", fill="y", expand=False)
        
        
        # Create 12 labels and text fields
        calcButton = ctk.CTkButton(master=leftframe, text="Calculate", command=updateButtonClick)
        calcButton.pack(pady=2, padx=5)
        
        # Pitch Circle Diameter and Module
        pcdleftframe = ctk.CTkFrame(master=leftframe)
        pcdleftframe.pack(padx=10, pady=12, fill="both", expand=False)
        
        pcdlabel = ctk.CTkLabel(master=pcdleftframe, text="pitch-circle diameters (PCD)")
        pcdlabel.pack(pady=2, padx=5)

        pcdtext_field = ctk.CTkEntry(master=pcdleftframe)
        pcdtext_field.insert(0, 0)
        pcdtext_field.pack(pady=2, padx=5)
        
        modulelabel = ctk.CTkLabel(master=pcdleftframe, text="Module (M)")
        modulelabel.pack(pady=2, padx=5)

        moduletext_field = ctk.CTkEntry(master=pcdleftframe)
        moduletext_field.insert(0, 0)
        moduletext_field.pack(pady=2, padx=5)
        
        
        # Circular Pitch
        circularpitchleftframe = ctk.CTkFrame(master=leftframe)
        circularpitchleftframe.pack(padx=10, pady=12, fill="both", expand=False)
        
        circularpitchlabel = ctk.CTkLabel(master=circularpitchleftframe, text="Circular Pitch (P)")
        circularpitchlabel.pack(pady=2, padx=5)

        circularpitchtext_field = ctk.CTkEntry(master=circularpitchleftframe)
        circularpitchtext_field.insert(0, 0)
        circularpitchtext_field.pack(pady=2, padx=5)
        
        
        # Number Of Teeth
        teethcountleftframe = ctk.CTkFrame(master=leftframe)
        teethcountleftframe.pack(padx=10, pady=12, fill="both", expand=False)
        
        teethcountlabel = ctk.CTkLabel(master=teethcountleftframe, text="Number of teeth (T)")
        teethcountlabel.pack(pady=2, padx=5)

        teethcounttext_field = ctk.CTkEntry(master=teethcountleftframe)
        teethcounttext_field.insert(0, 0)
        teethcounttext_field.pack(pady=2, padx=5)
        
        
        # Tooth Width        
        toothwidthlabel = ctk.CTkLabel(master=teethcountleftframe, text="Tooth Width (t)")
        toothwidthlabel.pack(pady=2, padx=5)

        toothwidthtext_field = ctk.CTkEntry(master=teethcountleftframe, placeholder_text=0.0)
        toothwidthtext_field.insert(0, 0)
        toothwidthtext_field.pack(pady=2, padx=5)
        
        
        # Addendum and Dedendum
        adddedleftframe = ctk.CTkFrame(master=leftframe)
        adddedleftframe.pack(padx=10, pady=12, fill="both", expand=False)
        
        addlabel = ctk.CTkLabel(master=adddedleftframe, text="Addendum")
        addlabel.pack(pady=2, padx=5)

        addtext_field = ctk.CTkEntry(master=adddedleftframe, placeholder_text=0.0, validate="all")
        addtext_field.insert(0, 0)
        addtext_field.pack(pady=2, padx=5)
        
        dedlabel = ctk.CTkLabel(master=adddedleftframe, text="Dedendum")
        dedlabel.pack(pady=2, padx=5)

        dedtext_field = ctk.CTkEntry(master=adddedleftframe, placeholder_text=0.0, validate="all")
        dedtext_field.insert(0, 0)
        dedtext_field.pack(pady=2, padx=5)
        
        frlabel = ctk.CTkLabel(master=adddedleftframe, text="Fillet Radius")
        frlabel.pack(pady=2, padx=5)

        frtext_field = ctk.CTkEntry(master=adddedleftframe, placeholder_text=0.0, validate="all")
        frtext_field.insert(0, 0)
        frtext_field.pack(pady=2, padx=5)
        
        
        #Separator for other variables to remember
        otherVarsleftframe = ctk.CTkFrame(master=leftframe)
        otherVarsleftframe.pack(padx=10, pady=12, fill="both", expand=False)
        
        pressureanglelabel = ctk.CTkLabel(master=otherVarsleftframe, text="Pressure Angle")
        pressureanglelabel.pack(pady=2, padx=5)

        pressureangletext_field = ctk.CTkEntry(master=otherVarsleftframe, placeholder_text="20")
        pressureangletext_field.pack(pady=2, padx=5)
        
        sdlabel = ctk.CTkLabel(master=otherVarsleftframe, text="Shaft Diameter")
        sdlabel.pack(pady=2, padx=5)

        sdtext_field = ctk.CTkEntry(master=otherVarsleftframe)
        sdtext_field.pack(pady=2, padx=5)

        
        
        #main loop
        self.root.mainloop()



if __name__ == "__main__":
    app = MyCustomUI()