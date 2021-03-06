#encoding: utf-8
#!/usr/bin/python

#FIRST RELEASE 0.1 CODENAME LUPIN ! By Ekianjo, 2013. 
#LICENSE: GPLv3 / http://opensource.org/licenses/GPL-3.0


#----- SECOND RELEASE GOALS (0.2)
#DONE
#ADD CONFIRMATION BEFORE DELETION - DONE
#ADD ICONS ON BUTTONS - DONE
#PROGRESS DOWNLOAD BAR OR INDICATION - DONE
#ADD BOOK YEAR INFO IN DATABASE - DONE
#ADD INFO on HOW MANY BOOKS ARE DOWNLOADED ADD INFO ON HOW MUCH SIZE THEY TAKE AND DISPLAY IN STATUS BAR - DONE
#NEED TO ADD SYSTEM IDENTIFICATION (PANDORA OR DESKTOP) - DONE
#ADD DOWNLOAD ALL BOOKS OPTION - DONE
#ADDED DIFFERENT WINDOW SIZE FOR DESKTOP AND PANDORA VERSION
#ADD OPTION TO SEE WHAT BOOKS WERE OPENED SO FAR- DONE
#ADD KEYBOARDS SHORTCUTS FOR MENUS - DONE

#ONGOING
#DISPLAY WHICH VERSION IS RUNNING, PANDORA OR DESKTOP, in STATUS BAR
#CHECK IF UPDATE IS AVAILABLE WHEN CHECKING VERSION IF ONLINE - VERSION NUMBER ADDED IN SOFT, need verification now
#change font size for desktop version and make description window a little bigger
#FIND IF THERE IS A FIX FOR CHECKING CONNECTION NOT ONLY ONCE
#COLOR BOOKS ALREADY OWNED IN CERTAIN SHADE IN "ALL" LIST


#-----THIRD RELEASE GOALS (0.3)
#ADD MORE BOOKS
#FIND OUT IF XOURNAL IS INSTALLED:SEARCH FOR PND IN DIRECTORIES - or package XOURNAL WITH IT
#ALLOW USAGE OF XOURNAL TO OPEN PDFs : find out command line
#SEND STATS TO SERVER (ANONYMOUS) 
#ADD FAVORITES 
#SHOW BOOKS ALREADY OPENED
#REPORT DOWNLOAD ERRORS TO SERVER

#----FOURTH RELEASE GOALS (0.4)
#SUGGEST BOOKS TO DATABASE (QUERY) THROUGH MENU
#UPDATE LOCAL DATABASE WITH ONLINE VERSION -> with GITHUB instead of version update ? 
#ADD BOOK LICENSE INFORMATION ? (should be in PDF anyway...)
#ALLOW READING OF HTML at least (reader tbc)

####FOR HTML SUPPORT
#add html in the file type
#make array after the file type
#first element of the array should be either all_links or follow_links
#all_links will simply fetch all html contents from pages where the html files are clearly separated
#follow_links will provide specific links to download from
#need to create specific rule on how to store the book
#need to add update in case new content is available
#need to use specific browser to open the book as well -> I have half the answer from Ptitseb already...
#add BS as dependency.

##REMINDER: Typical data structure
#(name of book, topic, author, file type, link, description)



import time #used for letting the download sleep and keep GUI active
import gtk #for the graphical user interface
import urllib, urllib2, os #os for file system operations, urllib for downloading and verifying the online connection. 
import subprocess #needed to launch separate application, in this case evince. 
import pango #used to determine a consistant style across the different systems. 
import httplib, socket
import fnmatch #matching index.html file
from hacker import *  #imports local database for books.
import shutil #to delete recursively directory in python std library
#from bs4 import BeautifulSoup #import bs for link extraction, for HTML books

versionsoft=0.20  #global version of the soft.
stillreading=[]  #captures the books already opened once at least

def list_books_being_read():
        global stillreading
		
        stillreading=[]
        try:
			if check_reading_file()==True:
				with open("Reading.txt") as f:
					data = f.readlines()
					for line in data:
						print str(line)
						stillreading.append(str(line))
			#print "that is "+stillreading
        except:
			pass

def check_if_being_read(bookname):
        global stillreading
		
        print "contenu de stillreading"
        print stillreading
        found=0
		
        if stillreading:
			print "yo mannnn"
			for books in stillreading:
				print "les books c'est "+books
				print "le check c'est "+bookname
				if books==bookname+'\n':
					print bookname+" is already opened"
					found+=1
				else:
					print bookname+" was not opened until now"

			if found>0:
				return True
			else:
				return False

        else:
			print "list is empty"
			return False

def check_reading_file():
        if os.path.isfile("Reading.txt"):
			return True
        else:
			return False


class InfoBooks(gtk.Window):
    def __init__(self):
        
        super(InfoBooks,self).__init__()

        #set info window size attributes
        
        
        self.set_size_request(mainwindow.winwidth-70,400)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(8)
        self.set_title(mainwindow.caca+" : Book Information")

		#check if book is html or pdf
        self.isbookhtml(mainwindow.caca)
        print "bookishtml value is",self.bookishtml

        #check if book was already downloaded or not
        if self.check_book_exists():
			print "book exists"

        #connect the close window function
        self.connect("destroy",self.close_window)

        #layout of the contents
        table = gtk.Table(8, 4, False)
        table.set_col_spacings(10)
        
        #title of the text field
        #title = gtk.Label("Book Information")
        halign = gtk.Alignment(0, 0, 0, 0)
        #halign.add(title)
        table.attach(halign, 0, 1, 0, 1, gtk.FILL, gtk.FILL, 0, 0);

        #get information to put into the text field. Textbuffer is the object that goes in textview field.
        textbuffer = gtk.TextBuffer()
        #textbuffer.set_text(self.findbookinfo())
        
        #set properties for the textview object.
        wins = gtk.TextView(buffer=textbuffer)

        #sets pango text attributes to define some standard style at display that does not depend on the OS settings only.
        h_tag = textbuffer.create_tag( "h", size_points=16, weight=pango.WEIGHT_BOLD) 
        position = textbuffer.get_end_iter()
        textbuffer.insert_with_tags( position, "\n"+mainwindow.caca+"\n", h_tag) 
        position = textbuffer.get_end_iter()
        n_tag = textbuffer.create_tag( "n", size_points=8,weight=pango.WEIGHT_NORMAL) 
        textbuffer.insert_with_tags( position, self.findbookinfo(), n_tag) 

        wins.set_left_margin(20)
        wins.set_right_margin(20)
        
        wins.set_pixels_inside_wrap(3)
        


        wins.set_wrap_mode(gtk.WRAP_WORD)
        wins.set_editable(False)
        wins.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(5140, 5140, 5140))
        wins.set_cursor_visible(False)
        table.attach(wins, 0, 2, 1, 3, gtk.FILL | gtk.EXPAND, gtk.FILL | gtk.EXPAND, 1, 1)

        #Download button attributes and connection
        self.download = gtk.Button("_Download",stock=None,use_underline=True)

        if self.check_book_exists()==True:
			self.download.set_sensitive(False)
        self.download.set_size_request(100, 40)
        table.attach(self.download, 3, 4, 1, 2, gtk.FILL, gtk.SHRINK, 1, 1)
        self.download.connect_object("clicked", self.downloadbook, None)

        #Close button attributes and connection to signals
        valign = gtk.Alignment(0, 0, 0, 0)
        self.close = gtk.Button("__Close", stock=gtk.STOCK_CLOSE,use_underline=True)
        self.close.set_size_request(100, 40)
        valign.add(self.close)
        table.set_row_spacing(1, 3)
        table.attach(valign, 3, 4, 2, 3, gtk.FILL, gtk.FILL | gtk.EXPAND, 1, 1)
        self.close.connect_object("clicked", self.close_window, None)

        # "delete"
        #make sure this button only appears if the book is downloaded. 
        halign2 = gtk.Alignment(0, 1, 0, 0)
        self.delete = gtk.Button("De__lete",stock=gtk.STOCK_DELETE,use_underline=True)
        if self.check_book_exists()==False:
			self.delete.set_sensitive(False)
        self.delete.set_size_request(100, 40)
        self.delete.connect_object("clicked", self.delete_book, None)
        halign2.add(self.delete)
        
        table.set_row_spacing(3, 6)
        table.attach(halign2, 0, 1, 4, 5, gtk.FILL, gtk.FILL, 0, 0)
        
        #read button attributes 
        self.readbtn = gtk.Button(label="__Read",stock=gtk.STOCK_OPEN,use_underline=True)
        if self.check_book_exists()==False:
		    self.readbtn.set_sensitive(False)
        self.readbtn.set_size_request(100, 40)
        table.attach(self.readbtn, 3, 4, 4, 5, gtk.FILL, gtk.FILL, 0, 0);
        self.readbtn.connect_object("clicked", self.open_book, None)
        
        #add the finalized table layout to the window
        self.add(table)

        #display all
        self.show_all()


    
    def isbookhtml(self,bookname):
		
		for books in hackerbooks:
			if books[0]==bookname:
				if books[3]=='html':
					self.bookishtml=True
				else:
					self.bookishtml=False
					
		#return bookishtml
    

    #deletes a book from the ones already downloaded
    def delete_book(self,widget):
		
		
		if self.bookishtml==False:
		
			filename=mainwindow.caca+".pdf"
			try:
				dm= gtk.MessageDialog(self, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, "Do you really want to delete this book?")
				if dm.run()==gtk.RESPONSE_YES:
					dm.destroy()
					os.remove(filename)
					print "book was deleted"
					md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "You just deleted the book.")
					md.run()
					md.destroy()
					self.readbtn.set_sensitive(False)
					self.download.set_sensitive(True)
					self.delete.set_sensitive(False)
					mainwindow.refresh_list()
				else:
					dm.destroy()
			
			except:
				
				print "File was not deleted"
				
		else:
			try:
				dm= gtk.MessageDialog(self, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, "Do you really want to delete this book?")
				if dm.run()==gtk.RESPONSE_YES:
					dm.destroy()
					shutil.rmtree('HTMLBOOKS/{0}'.format(mainwindow.caca))
					md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "You just deleted the book.")
					md.run()
					md.destroy()
					self.readbtn.set_sensitive(False)
					self.download.set_sensitive(True)
					self.delete.set_sensitive(False)
					mainwindow.refresh_list()
				else:
					dm.destroy()
			
			except:
				
				print "File was not deleted"
			

	#check if book exists first
    def open_book(self, widget):
    	try:

			for books in hackerbooks:
				if books[0]==mainwindow.caca: 
				
					if books[3]=='html':
						
						if mainwindow.system_check()=="Desktop":
						
							rootPath = 'HTMLBOOKS/{0}/'.format(books[0])
							pattern = 'index.html'
							
							#will look for index.html location in case it's not obvious... and use it after
							for root, dirs, files in os.walk(rootPath):
								for filename in fnmatch.filter(files, pattern):
									#print(os.path.join(root, filename))
									foundpath=os.path.join(root, filename)
									
							
							#use xdg-open on desktop with the index.html file ! 
							command=['xdg-open','{0}'.format(foundpath)]
							p=subprocess.Popen(command)
						
						else:
							#use thunar on Pandora at first, before PND mounting
							print "html on Pandora"
							command=['thunar','HTMLBOOKS/{0}/'.format(books[0])]
							p=subprocess.Popen(command)
						
					else:
						
				
						#need to separate the arguments in an array to give arguments instead of a single command!!
						command=["evince", "{0}.pdf".format(mainwindow.caca)]
						print command
						subprocess.Popen(command)
						self.register_opened_books(mainwindow.caca)
						#send command here to register this book as opened
    		
    		
    		
        except:
			print "reading did not work"

    def register_opened_books(self,bookname):
		#check if file exists
		
		#print "coucou je suis la"
		#create file if not
		list_books_being_read()
		
		if check_reading_file()==False:
			
			if check_if_being_read(bookname)==False:
				f = open('Reading.txt','w')
				f.write(bookname+'\n')
				f.close()
				print "created reading and added "+bookname
				list_books_being_read()
				
		else:
			if check_if_being_read(bookname)==False:
				with open('Reading.txt','a') as myfile:
				    myfile.write(bookname+'\n')
				    myfile.close()
				    print "added "+bookname
				    list_books_being_read()
				
		#if file exist, check if the book is already opened.

		#return the fact that it was found
				
		#if not yet oepened; add to the file
		#f.open with w+

	#checks if the internet connection is active
    def check_internet(self):
		try:
			response=urllib2.urlopen('http://www.google.com',timeout=2)
			print "you are connected"
			return True

		except urllib2.URLError as err:
			if mainwindow.check_internet_babu()==True:
				return True
			else:
				#print err
				md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "You are Offline - Please Connect.")
				md.run()
				md.destroy()
				return False

	#closes the info window
    def close_window(self, widget):
        self.destroy()

    #returns the book information 
    def findbookinfo(self):
        try:
	        for books in hackerbooks:
	            #returns the description of the book
	            if books[0]==mainwindow.caca: return books[5]
        except:
        	return ""

    #checks if the book exists in the folder where they are downloaded
    def check_book_exists(self):
		
		if self.bookishtml==False:
				
			
			bookname = mainwindow.caca+".pdf"
			if os.path.isfile(bookname):
				return True
			else:
				return False
				
		else:
			if os.path.isdir("HTMLBOOKS/{0}".format(mainwindow.caca)):
				return True
			else:
				return False
			

    #downloads the book
    def downloadbook(self,widget):

        if self.check_internet():
	        
	        for books in hackerbooks:
	            #select the right book that is to download
	            if books[0]==mainwindow.caca: 
	                print books[4]
	                try:
                            self.close.set_sensitive(False)
	                    #downloads the book and renames it to the full name and adds pdf extension
	                    #TODO: ADD PROGRESS BAR

                        #TODO: ALLOW FOR HTML FILES AS WELL SINCE MANY BOOKS DONT HAVE PDF
	                    
	                    if books[3]=='html':
							command=['wget','-rkp','-l3','-np','-nH','--cut-dirs=1',books[4],'-P',"HTMLBOOKS/{0}/".format(books[0])]
							print command
							p=subprocess.Popen(command, stdout=subprocess.PIPE)
							stdout, stderr = p.communicate()
							print "Done"

							
	                    #	if books[4][0]=='all_links':
		                #    	soup = BeautifulSoup(books[4][1])
		                #    	linksonpage=soup.find_all('a') # Finds all hrefs from the html doc.
		                    	
		                #    	for eachlink in linksonpage:
		                #    		os.makedirs(books[0])
		                #    		urllib.urlretrieve(eachlink,****name to fix****,reporthook=self.myReportHook)
	                    			#split the name with / and get last string ? potentially...
	                    	
	                    
	                    else:
	                    	if books[3]=='pdf':
		                    	urllib.urlretrieve(books[4],books[0]+".pdf",reporthook=self.myReportHook)
	                    
	                    #print "Download finished"
	                    if mainwindow.downloadmode==0:
							md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "Download Completed")
							md.run()
							md.destroy()
			    mainwindow.refresh_list()
	                    self.readbtn.set_sensitive(True)
	                    self.download.set_sensitive(False)
                            self.download.set_label("Download")
	                    self.delete.set_sensitive(True)
                            self.close.set_sensitive(True)
                        #self.close.set_sensitive(True)
	                    #TODO: CONFIRM THE FILE IS DOWNLOADED AND CONFIRM SIZE.
	                    #TODO: CHANGE PROPERTIES SO THAT ONE CAN LAUNCH THE PDF TO READ OR THE HTML FILE, AND MAKE THE DOWNLOAD BUTTON GREY
	                except:
	                    print "Download did not work"
    	else:
    		print "you are offline"

    #use the urlretrieve hooks to confirm how fast the download is progressing
    def myReportHook(self,blocks,blockSize,totalSize):
        percentage = round(float ( blocks * blockSize ) / totalSize,3)
        if percentage > 1:
            percentage = 1

        self.download.set_label(str(percentage*100)+" %")

        self.refresh_gui(0.0001,0.0001)

    #refreshes the main windows contents so that the download progress can be updated.  
    def refresh_gui(self,delay=0.0001,wait=0.0001):
        
        time.sleep(delay)
        
        while gtk.events_pending():
            gtk.main_iteration_do(block=False)
            time.sleep(wait)

#main window start. 
class HackerBooks(gtk.Window): 
    def __init__(self):
    	global versionsoft
        super(HackerBooks, self).__init__()
        
        
        window=gtk.Window()
        self.create_directory()  #creates BOOKS directory
        self.version=versionsoft  #documents the current version of the soft
        
        list_books_being_read()
        
		#downloadmode, 0 for one by one, 1 for all at once
        self.downloadmode=0
		
        self.check_internet_babu()

        #if displaymode is 0, show all, 1, show downloaded only, if 2, shows the ones left to download.
        self.displaymode=0

        if self.system_check()=="Pandora":
            self.winwidth=750
            self.winheight=400
        else:
			self.winwidth=800
			self.winheight=window.get_screen().get_height()-200
			
        self.set_size_request(self.winwidth, self.winheight)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        self.set_title("Hacker Books")
        #self.caca="yooo"

        vbox = gtk.VBox(False, 8)

        #Definition of menu bar
        mb=gtk.MenuBar()
        filemenu=gtk.Menu()
        filem=gtk.MenuItem("_File")
        filem.set_submenu(filemenu)

        #about menu
        aboutmenu=gtk.Menu()
        aboutm=gtk.MenuItem("_About")
        aboutm.set_submenu(aboutmenu)
        version=gtk.MenuItem("Version")
        version.connect("activate",self.about_this_application)
        aboutmenu.append(version)

	#add accelerators in menu
	agr = gtk.AccelGroup() #create accelerator group
	self.add_accel_group(agr) #add accelerator group agr

        #Show menu
        showmenu=gtk.Menu()
        showm=gtk.MenuItem("_Display")
        showm.set_submenu(showmenu)
        showall=gtk.MenuItem("Show All Books")
        key, mod = gtk.accelerator_parse("<Control>A")
        showall.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        showall.connect("activate",self.all_books)
        showmenu.append(showall)
        showgotbooks=gtk.MenuItem('Show Downloaded Books')
        key, mod = gtk.accelerator_parse("<Control>D")
        showgotbooks.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        showgotbooks.connect("activate",self.downloaded_books_only)
        showmenu.append(showgotbooks)
        showleftbooks=gtk.MenuItem('Show Books Left to Download')
        key, mod = gtk.accelerator_parse("<Control>L")
        showleftbooks.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        showleftbooks.connect("activate",self.left_to_download)
        showmenu.append(showleftbooks)
        showreadingbooks=gtk.MenuItem('Show Opened Books')
        key, mod = gtk.accelerator_parse("<Control>O")
        showreadingbooks.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        showreadingbooks.connect("activate",self.books_being_read)
        showmenu.append(showreadingbooks)
        
        #Show special menu
        specialmenu=gtk.Menu()
        specialm=gtk.MenuItem("Special")
        specialm.set_submenu(specialmenu)
        downloadall=gtk.MenuItem("Download All")
        downloadall.connect("activate",self.download_all_books)
        specialmenu.append(downloadall)

        #File menu
        exit=gtk.MenuItem('Exit')
        key, mod = gtk.accelerator_parse("<Control>Q")
        exit.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        exit.connect("activate",gtk.main_quit)
        filemenu.append(exit)

        #adding it back in the menu together
        mb.append(filem)
        mb.append(showm)
        mb.append(specialm)
        mb.append(aboutm)

        #packs the vbox
        vbox.pack_start(mb,False,False)
        
        #sw is a scrolled window
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        vbox.pack_start(sw, True, True, 0)

        self.store = self.create_model()

        self.treeView = gtk.TreeView(self.store)
        self.treeView.connect("row-activated", self.on_activated)
        self.treeView.set_rules_hint(True)
        sw.add(self.treeView)

        self.create_columns(self.treeView)
        self.statusbar = gtk.Statusbar()
        
        self.check_nb_books()

        #packs the statusbar
        vbox.pack_start(self.statusbar, False, False, 0)

        #add the vbox in the window
        self.add(vbox)
        self.show_all()

    #function to enable download of all books at once. it checks for books already downloaded, too.
    def download_all_books(self,widget):
		print "downloading"
		
		if self.check_internet():
			
			#confirms the user wants to move forward with it
			dm= gtk.MessageDialog(self, gtk.DIALOG_MODAL, gtk.MESSAGE_QUESTION, gtk.BUTTONS_YES_NO, "Do you really want to download all books? It may take a long time")
			if dm.run()==gtk.RESPONSE_YES:
				dm.destroy()
				
				#set automatic download mode
				self.downloadmode=1
					
				for books in hackerbooks:
					
					mainwindow.caca=books[0]
					
					dlwd=InfoBooks()
					if dlwd.check_book_exists()==False:
						dlwd.downloadbook(None)
					dlwd.destroy()
			
			else:
				dm.destroy()
				
		#resets the download mode to normal
		self.downloadmode=0
		pass


    #another way to check for internet connection but it does not work perfectly either...
    def check_internet_babu(self):
        test_con_url = "www.google.com" # For connection testing
        test_con_resouce = "/intl/en/policies/privacy/" # may change in future
        test_con = httplib.HTTPConnection(test_con_url) # create a connection

        try:
            test_con.request("GET", test_con_resouce) # do a GET request
            response = test_con.getresponse()
        except httplib.ResponseNotReady as e:
            print "Improper connection state"
            test_con.close()
            return False
        except socket.gaierror as e:
            print "Not connected"
            test_con.close()
            return False
        else:
            print "Connected"
            test_con.close()
            return True

	#checks if the internet connection is active
    def check_internet(self):
		try:
			response=urllib2.urlopen('http://www.google.com',timeout=2)
			print "you are connected"
			return True

		except urllib2.URLError as err: 
			print err
			if self.check_internet_babu()==False:
  			    return False
			else:
				return True

    #version check to see if you have the latest version of the software. to upgrade...
    def check_new_version(self):
		if self.check_internet():
			try:
				urllib.urlretrieve("https://raw.github.com/ekianjo/HackerBooks/master/version","latestversion.txt")
				with open('latestversion.txt', 'r') as content_file:
					content = content_file.read()
					content=float(content[0]+content[1]+content[2]+content[3])
					print content
					if content==versionsoft:
						print "you have the latest version"
			except:
				print "didn't work"
		#https://raw.github.com/ekianjo/HackerBooks/master/version
    	#to do if online at start

	#checking if desktop or Pandora Handheld
    def system_check(self):
    	if os.path.isdir("/proc/pandora"):
    		print "You are running this on a Pandora handheld"
    		return "Pandora"
    	else:
    		print "You are running this on Desktop"
    		return "Desktop"

	#about application dialog. Classic stuff. 
    def about_this_application(self,widget):
        self.check_new_version()
        aboutthis = gtk.AboutDialog()
        aboutthis.set_program_name("HackerBooks")
        aboutthis.set_version(str(versionsoft))
        aboutthis.set_copyright("Ekianjo 2013")
        aboutthis.set_comments("HackerBooks is a small application to download and manage free books about Programming and Computer Science")
        aboutthis.set_website("https://github.com/ekianjo/HackerBooks")
        aboutthis.set_logo(gtk.gdk.pixbuf_new_from_file("../icon.png"))
        aboutthis.run()
        aboutthis.destroy()

    #refreshes the main window contents so that it remains updated even when you download books or delete them.
    def refresh_list(self):
        self.treeView.set_model(self.create_model())
	self.check_nb_books()

    #enables the display of all books regardless of whether they were downloaded or not
    def all_books(self,widget):
    	#displaymode is now all books.
    	self.displaymode=0
    	self.refresh_list()

   	#enables only the display of books already available offline
    def downloaded_books_only(self,widget):
    	#ensure that the displaymode is now set to only downloaded books.
    	self.displaymode=1
    	self.refresh_list()

    def left_to_download(self,widget):
        self.displaymode=2
        self.refresh_list()

    def books_being_read(self,widget):
		self.displaymode=3
		self.refresh_list()

   	#creates the folder where books are saved if necessary
    def create_directory(self):
    	if os.path.isdir("BOOKS")==False:
    		os.makedirs("BOOKS")

    	os.chdir("BOOKS")

    #checks the total number of books available in the database
    def check_total_nb_books(self):
    	totalbooks=0
    	
    	for books in hackerbooks:
    		totalbooks+=1
    	
    	return totalbooks

    #checks number of books downloaded and displays how many more are available.
    def check_nb_books(self):
	totalbooks=0
    	totalsize=0
	for books in hackerbooks:
		bookname=books[0]+".pdf"
		if os.path.isfile(bookname):
            		totalsize=totalsize+os.path.getsize(bookname)
			totalbooks=totalbooks+1
	
	if totalbooks>1:
		self.statusbar.push(0, "You have {0} books in your library ({1}). {2} more books are available for download.".format(totalbooks, self.convert_bytes(totalsize), str(self.check_total_nb_books()-totalbooks)))
	elif totalbooks==1:
		self.statusbar.push(0, "You have {0} book in your library ({1}). {2} more books are available for download.".format(totalbooks, self.convert_bytes(totalsize), str(self.check_total_nb_books()-totalbooks)))
	else:	
		self.statusbar.push(0, "You have no book in your library. {0} books are available for download.".format(str(self.check_total_nb_books())))

	#convert bytes sizes to be readable
    def convert_bytes(self,bytes):
	    bytes = float(bytes)
	    if bytes >= 1099511627776:
		terabytes = bytes / 1099511627776
		size = '%.2fTb' % terabytes
	    elif bytes >= 1073741824:
		gigabytes = bytes / 1073741824
		size = '%.2fGb' % gigabytes
	    elif bytes >= 1048576:
		megabytes = bytes / 1048576
		size = '%.2fMb' % megabytes
	    elif bytes >= 1024:
		kilobytes = bytes / 1024
		size = '%.2fKb' % kilobytes
	    else:
		size = '%.2fb' % bytes
	    return size

    def create_model(self):
        self.store = gtk.ListStore(str, str, str, str,str)

        for books in hackerbooks:
            bookname=books[0]+".pdf"
            if self.displaymode==1:
			self.set_title("Hacker Books [Books Downloaded]")
        		if os.path.isfile(bookname):
                            	
        			print bookname
        			
	        		self.store.append([books[0], books[1], books[2],books[3],books[6]])
            elif self.displaymode==2:
                self.set_title("Hacker Books [Books Left to Download]")
                if os.path.isfile(bookname)==False:
                    self.store.append([books[0], books[1], books[2],books[3],books[6]])
            elif self.displaymode==3:
				self.set_title("Hacker Books [Books You Have Opened...]")
				if check_if_being_read(books[0])==True:
					self.store.append([books[0], books[1], books[2],books[3],books[6]])
            else:
			self.set_title("Hacker Books [All Books]")
	        	self.store.append([books[0], books[1], books[2],books[3],books[6]])
	        
        return self.store

    def create_columns(self, treeView):
    
        #display Ttitle
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Title", rendererText, text=0)
        column.set_sort_column_id(0)    
        treeView.append_column(column)
        
        #display topic
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Subject", rendererText, text=1)
        column.set_sort_column_id(1)
        treeView.append_column(column)

        #display author
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Author", rendererText, text=2)
        column.set_sort_column_id(2)
        treeView.append_column(column)

        #display format
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Format", rendererText, text=3)
        column.set_sort_column_id(3)
        treeView.append_column(column)
        
        #display year
        rendererText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Year", rendererText, text=4)
        column.set_sort_column_id(4)
        treeView.append_column(column)

    def on_activated(self, widget, row, col):
        
        model = widget.get_model()
        #text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
        #self.statusbar.push(0, text)
        
        #stores the info about the book selected
        mainwindow.caca=model[row][0]
        
        #print mainwindow.caca
        InfoBooks()

mainwindow=HackerBooks()
gtk.main()
