from tkinter import *
from time import sleep
coords = [0,0]
class managerw(object):
    debug = False
    boolc = False
    window = None
    time_cview = 0
    def interface(window):
        window.bind('<Motion>', managerw.move)
    def move(event):
        global coords
        coords[0] = event.x
        coords[1] = event.y
        if(managerw.boolc):
            try:sleep(managerw.time_cview);print(coords[0], coords[1])
            except:print("ERROR TYPE: time_cview SHOULD be integer or float.")
    def run(window):
        managerw.interface(window)
    def coord_view(window,boolc):
        managerw.interface(window)
    def typely(listm):
        typely = True
        for coord in listm:
            for coords in coord[1]:
                try:
                    ex = coord[1][0] + coord[1][1]
                except:
                    typely = False
                finally:
                    if(typely == True):return True
                    else: return False
                    
    "Creating Main Page"
    def create_mpage(window,ui_page,size):
        if(type(ui_page) == list):
            window.geometry(size)
            for ui in ui_page:
                ui.pack()
            if(managerw.debug == True):
                print("Page ui loaded.")
        else:
            print('\033[31m' + "ERROR TYPE: create_mpage(ui_page), ui_page SHOULD be list type.")
    def redirect_pages(page_ui_1,page_ui_2,side=None):
        "This function makes redirecting from page_1 to page_2, ui reconstruction."
        if(type(page_ui_1) and type(page_ui_2) == list):
            if(type(side) != list and type(side) != str and side != None): print('\033[31m' + "\n\nERROR TYPE: redirect_pages(ui_page_1,ui_page_2,side), side SHOULD be str type. \nEXAMPLE:\n\nmanagerw.redirect_pages(main,second,'left')\nOR\nmanagerw.redirect_pages(ui_page_1,ui_page_2,['top','right',left'])\n\n")
            else:
                print("Start Redirecting.")
                for ui_page_1 in page_ui_1:
                    ui_page_1.pack_forget()
                if(type(side) != list and side != None and type()):
                    for ui_page_2 in page_ui_2:
                        ui_page_2.pack(side=side)
                        print("Packed ui.")
                else:
                    if(side in ["bottom","top","right","left"]):
                        side_index = 0
                        for ui_page_2 in page_ui_2:
                            try:
                                ui_page_2.pack(side=side[side_index])
                            except:
                                print(Fore.RED+"\n\nERROR SYNTAX: if side is a list, count index side SHOULD be == count index ui_page_2.\n\n")
                        side_index += 1
                        print("Packed ui.")
                    else:
                        if(managerw.typely(page_ui_2)):
                            for sidec in page_ui_2:
                                print(sidec[1][0])
                                try:
                                    sidec[0].place(x=sidec[1][0],y=sidec[1][1])
                                    print("x: {},\ny:{}.".format(sidec[1][0],sidec[1][1]))
                                except:
                                    print('\033[31m' + "\n\nERROR SYNTAX: if side is a list, count index side SHOULD be == count index ui_page_2.\n\n")
                                print("Packed ui.")
                        else:
                            print("ERROR SYNTAX list.")
                
        else:
            print('\033[31m' + "ERROR TYPE: redirect_pages(ui_page), page_ui_1 and page_ui_2 SHOULD be list type.")
            
    def p_e(title: str, message: str):
        "Procces Exit"
        output = messagebox.askyesno(title=title,message=message)
        if(output==True):
	    if managerw.debug == True:
		print("Program Exit.")
            exit()
