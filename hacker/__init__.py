#encoding: utf-8
#!/usr/bin/python

global hackerbooks

hackerbooks = [('Pro Git', 'Git', 'Scott Chacon','pdf','https://github.s3.amazonaws.com/media/progit.en.pdf',
'''
Git is the version control system developed by Linus Torvalds for Linux kernel development. 
It took the open source world by storm since its inception in 2005, and is used by small development shops and giants like Google, Red Hat, and IBM, and of course many open source projects. 

A book by Git experts to turn you into a Git expert.

• Introduces the world of distributed version control
• Shows how to build a Git development workflow''','2009'), 

('Think Complexity', 'General', 'Allen B. Downey','pdf','http://greenteapress.com/compmod/thinkcomplexity.pdf',
'''
This book is about complexity science, data structures and algorithms, intermediate programming in Python, and the philosophy of science:''','2012'
),

    ('The Linux Command Line', 'Command Line', 'William E. Shotts Jr.','pdf','http://downloads.sourceforge.net/project/linuxcommand/TLCL/09.12/TLCL-09.12.pdf?r=http%3A%2F%2Flinuxcommand.org%2Ftlcl.php&ts=1372170077&use_mirror=jaist',
'''
You have experienced the shiny, point-and-click surface of your Linux computer—now dive below and explore its depths with the power of the command line.

The Linux Command Line takes you from your very first terminal keystrokes to writing full programs in Bash, the most popular Linux shell. Along the way you'll learn the timeless skills handed down by generations of gray-bearded, mouse-shunning gurus: file navigation, environment configuration, command chaining, pattern matching with regular expressions, and more.

In addition to that practical knowledge, author William Shotts reveals the philosophy behind these tools and the rich heritage that your desktop Linux machine has inherited from Unix supercomputers of yore.
''','2009'),
('Think Stats','Statistics','Allen B. Downey','pdf','http://greenteapress.com/thinkstats/thinkstats.pdf',
'''
Think Stats: Probability and Statistics for Programmers is a textbook for a new kind of introductory prob-stat class. It emphasizes the use of statistics to explore large datasets. It takes a computational approach. 

The book lends itself to a project-based approach. In my class, students work on a semester-long project that requires them to pose a statistical question, find a dataset that can address it, and apply each of the techniques they learn to their own data.
''','2011'),
("Street-Fighting Mathematics",'Problem Solving','Sanjoy Mahajan','pdf','https://mitpress.mit.edu/sites/default/files/titles/content/9780262514293_Creative_Commons_Edition.pdf',
	'''
In problem solving, as in street fighting, rules are for fools: do whatever works—don't just stand there! Yet we often fear an unjustified leap even though it may land us on a correct result. Traditional mathematics teaching is largely about solving exactly stated problems exactly, yet life often hands us partly defined problems needing only moderately accurate solutions. This engaging book is an antidote to the rigor mortis brought on by too much mathematical rigor, teaching us how to guess answers without needing a proof or an exact calculation.

In Street-Fighting Mathematics, Sanjoy Mahajan builds, sharpens, and demonstrates tools for educated guessing and down-and-dirty, opportunistic problem solving across diverse fields of knowledge—from mathematics to management. Mahajan describes six tools: dimensional analysis, easy cases, lumping, picture proofs, successive approximation, and reasoning by analogy. Illustrating each tool with numerous examples, he carefully separates the tool—the general principle—from the particular application so that the reader can most easily grasp the tool itself to use on problems of particular interest.
''','2010'),
('Algorithmic Game Theory','Game Theory','Noam Nisan and more','pdf','http://www.cambridge.org/journals/nisan/downloads/Nisan_Non-printable.pdf',
    '''
In the last few years game theory has had a substantial impact on computer science, especially on Internet- and e-commerce-related issues. More than 40 of the top researchers in this field have written chapters that go from the foundations to the state of the art. Basic chapters on algorithmic methods for equilibria, mechanism design and combinatorial auctions are followed by chapters on incentives and pricing, cost sharing, information markets and cryptography and security. Students, researchers and practitioners alike need to learn more about these fascinating theoretical developments and their widespread practical application.
''','2007'),
('Think Python','Python','Allen B. Downey','pdf','http://greenteapress.com/thinkpython/thinkpython.pdf',
'''
The goal of this book is to teach you to think like a computer scientist. This way of thinking combines some of the best features of mathematics, engineering, and natural science. Like mathematicians, computer scientists use formal languages to denote ideas (speciﬁcally computations). 

Like engineers, they design things, assembling components into systems and evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex systems, form hypotheses, and test predictions.''',
'2013'),
('A Byte of Vim','Vim','Swaroop CH','pdf','http://files.swaroopch.com/vim/byte_of_vim_v051.pdf',
'''
“A Byte of Vim” is a book which aims to help you to learn how to use the Vim editor (version 7), even if all you know is how to use the computer keyboard.

The first part of this book is meant for new users who want to understand what Vim is and learn how to use it.

The second part of this book is for people who already know how to use Vim and want to learn about features that make Vim so powerful, such as windows and tabs, personal information management, making it a programmer’s editor, how to extend Vim with your own plugins, and more.
''','2008'),
('Advanced Linux Programming','Linux','CodeSourcery', 'pdf','http://www.advancedlinuxprogramming.com/alp-folder/advanced-linux-programming.pdf',
'''
Advanced Linux Programming is intended for the programmer already familiar with the C programming language. Authors Alex Samuel, Jeffrey Oldham, and Mark Mitchell of CodeSourcery, LLC take a tutorial approach and teach the most important concepts and power features of the GNU/Linux system in application programs.

If you're a developer already experienced with programming for the GNU/Linux system, are experienced with another UNIX-like system and are interested in developing GNU/Linux software, or want to make the transition for a non-UNIX environment and are already familiar with the general principles of writing good software, this book is for you. In addition, you will find that this book is equally applicable to C and C++ programming. Even those progamming in other languages will find this book useful since the C language APIs and conventions are the lingua franca of GNU/Linux.
''','2001'),
('Ruby Best Practices','Ruby','Gregory Brown','pdf','http://majesticseacreature.com/rbp-book/pdfs/rbp_1-0.pdf',
'''
In 1993, when Ruby was born, Ruby had nothing. No user base except for me and a few close friends. No tradition. No idioms except for a few inherited from Perl, though I regretted most of them afterward.

But the language forms the community. The community nourishes the culture. In the last decade, users increased—hundreds of thousands of programmers fell in love with Ruby. They put great effort into the language and its community. Projects were born. Idioms tailored for Ruby were invented and introduced. Ruby was influenced by Lisp and other functional programming languages. Ruby formed relationships between technologies and methodologies such as test-driven development and duck typing.

This book introduces a map of best practices of the language as of 2009. I’ve known Greg Brown for years, and he is an experienced Ruby developer who has contributed a lot of projects to the language, such as Ruport and Prawn. I am glad he compiled his knowledge into this book.

His insights will help you become a better Ruby programmer.''','2009'),
('Introduction to Machine Learning','Machine Learning','Alex Smola','pdf','http://alex.smola.org/drafts/thebook.pdf',
'''
Over the past two decades Machine Learning has become one of the main-stays of information technology and with that, a rather central, albeit usually hidden, part of our life. With the ever increasing amounts of data becoming available there is good reason to believe that smart data analysis will become even more pervasive as a necessary ingredient for technological progress.''','2008'),
('Dive Into Python 3','Python','Mark Pilgrim','pdf','https://github.com/downloads/diveintomark/diveintopython3/dive-into-python3.pdf',
	'''
Dive Into Python 3 covers Python 3 and its differences from Python 2. Compared to Dive Into Python, it’s about 20% revised and 80% new material.''','2009'),
('Building Skills in Python','Python','Steven F. Lott','pdf','http://www.itmaybeahack.com/book/python-2.6/latex/BuildingSkillsinPython.pdf',
'''
How do you learn Python? By doing a series of exercises, each of which adds a single new feature of the language. This 450+ page book has 42 chapters that will help you build Python programming skills through a series of exercises. This book includes six projects from straight-forward to sophisticated that will help solidify your Python skills.

The 2.6 edition was significantly revised and expanded to cover Python 2.6 and some elements of Python 3.1. Many chapters have been updated, reorganized and added since the 2.5 edition.

The current release has benefitted from a great deal of support from readers who sent detailed lists of errors and suggestions. Professional programmers who need to learn Python are this book’s primary audience. We provide specific help for you in a number of ways.

Since Python is simple, we can address newbie programmers who don’t have deep experience in a number of other languages. We will call out some details in specific newbie sections. 
''','2010'),
('How to Think Like A Computer Scientist','Python','Allen B. Downey (more)', 'pdf', 'http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf',
'''
Despite Python’s appeal to many different communities, you may still wonder why Python? or why teach programming with Python? Answering these questions is no simple task—especially when popular opinion is on the side of more masochistic alternatives such as C++ and Java. However, I think the most direct answer is that programming in Python is simply a lot of fun and more productive.

One of the reasons why I like Python is that it provides a really nice balance between the practical and the conceptual. Since Python is interpreted, beginners can pick up the language and start doing neat things almost immediately without getting lost in the problems of compilation and linking. Furthermore, Python comes with a large library of modules that can be used to do all sorts of tasks ranging from web-programming to graphics. Having such a practical focus is a great way to engage students and it allows them to complete significant projects. However, Python can also serve as an excellent foundation for introducing important computer science concepts. 
''','2012'),
('Functional C','C','Pieter Hartel','pdf','http://eprints.eemcs.utwente.nl/1077/02/book.pdf',
'''
The Computer Science Departments of many universities teach a functional language as the first programming language. Using a functional language with its high level of abstraction helps to emphasize the principles of programming. Func-tional programming is only one of the paradigms with which a student should be acquainted. Imperative, Concurrent, Object-Oriented, and Logic programming are also important. Depending on the problem to be solved, one of the paradigms will be chosen as the most natural paradigm for that problem.
This book is the course material to teach a second paradigm: imperative programming, using C as the programming language. The book has been written so that it builds on the knowledge that the students have acquired during their rst course on functional programming, using SML. The prerequisite of this book is that the principles of programming are already understood; this book does not specically aim to teach `problem solving' or `programming'.''',
'1999'),

('Mastering Node','NodeJS','TJ Holowaychuk','pdf','http://github.com/visionmedia/masteringnode/raw/master/book.pdf',
'''
Mastering node is an open source eBook by node hackers for node hackers. I started this as a side project and realized that I don't have time :) so go nuts, download it, build it, fork it, extend it and share it. If you come up with something you wish to contribute back, send me a pull request.''',
''),
('''Mobile Developer's Guide to the Galaxy''','Mobile Development', 'Robert Virkus (more)', 'pdf', 'http://www.enough.de/fileadmin/uploads/dev_guide_pdfs/Guide_12thEdition_WEB.pdf',
'''
The free, non-commercial book that provides an overview on the different mobile technologies and platforms for developers and decision-makers. Learn everything about how to create solutions for iOS, Android, BlackBerry, Java ME or Windows Phone.

More than 20 writers from the mobile community share their know-how, across more than 250 pages, in dealing with topics such as accessibility in mobile apps, LBS, mobile analytics, prototyping, cross-platform development, native development, mobile web and app marketing. This project was initiated in 2009 and we have since published a number of updated versions. As of today, we have distributed over 50,000 hardcopies. The 12th, and latest, edition was published in February 2013.''',
'2013')
,('Getting Started with Open Source Development','Open Source','Rachna Kapur (more)','pdf','http://public.dhe.ibm.com/software/dw/db2/express-c/wiki/Getting_started_with_open_source_development_p2.pdf',
'''
Keeping your skills current in today's world is becoming increasingly challenging. There are too many new technologies being developed, and little time to learn them all. The DB2® on Campus Book Series has been developed to minimize the time and effort required to learn many of these new technologies.

Who should read this book?
This book is a good starting point for beginners to the open source world. It is specially written to equip students, and open source enthusiasts with the norms and best practices of open source. You should read this book if you want to:

• Educate yourself on the objectives of open source
• Understand open source software licensing requirements 
• Get an introduction to the norms followed in the open source world
• Join the open source movement and begin contributing. ''',
'2010')
,('Programming from the Ground Up','Assembly','Jonathan Bartlett','pdf','http://ftp.twaren.net/Unix/NonGNU//pgubook/ProgrammingGroundUp-1-0-booksize.pdf',
'''
Most introductory books on programming frustrate me to no end. At the end of them you can still ask "how does the computer really work?" and not have a good answer. They tend to pass over topics that are difﬁcult even though they are important. I will take you through the difﬁcult issues because that is the only way to move on to masterful programming. 
My goal is to take you from knowing nothing about programming to understanding how to think, write, and learn like a programmer. You won’t know everything, but you will have a background for how everything ﬁts together. At the end of this book, you should be able to do the following:

• Understand how a program works and interacts with other programs
• Read other people’s programs and learn how they work
• Learn new programming languages quickly
• Learn advanced concepts in computer science quickly
''',
'2003'),
('BashGuide','Bash','Lhunath','pdf','http://folk.ntnu.no/geirha/bashguide.pdf',
'''
This guide aims to aid people interested in learning to work with BASH1. It aspires to teach good practice techniques for using BASH, and writing simple scripts. This guide is targeted at beginning users. It assumes no advanced knowledge -- just the ability to login to a Unix-like system and open a command-line (terminal) interface. It will help if you know how to use a text editor; we will not be covering editors, nor do we endorse any particular editor choice.

Familiarity with the fundamental Unix tool set, or with other programming languages or programming concepts, is not required, but those who have such knowledge may understand some of the examples more quickly. If something is unclear to you, you are invited to report this (usehttp://mywiki.wooledge.org/BashGuideFeedback, or the #bash channel on irc.freenode.org) so that it may be clariﬁed in this document for future readers. You are invited to contribute to the development of this document by extending it or correcting invalid or incomplete information.''',
'2013'),
('Essential C','C','Nick Parlante','pdf','http://cslibrary.stanford.edu/101/EssentialC.pdf',
'''
This Stanford CS Education document tries to summarize all the basic features of the C language. The coverage is pretty quick, so it is most appropriate as review or for someone with some programming background in another language. Topics include variables, int types, floating point types, promotion, truncation, operators, control structures (if, while, for), functions, value parameters, reference parameters, structs, pointers, arrays, the preprocessor, and the standard C library functions.''',
'2003')
,('An Introduction to Programming in Emacs Lisp', 'Emacs', 'Robert J. Chassell','pdf','https://www.gnu.org/software/emacs/emacs-lisp-intro/emacs-lisp-intro.pdf',
'''
Most of the GNU Emacs integrated environment is written in the programming language called Emacs Lisp. The code written in this programming language is the software—the sets of instructions—that tell the computer what to do when you give it commands. Emacs is designed so that you can write new code in Emacs Lisp and easily install it as an extension to the editor. (GNU Emacs is sometimes called an “extensible editor”, but it does much more than provide editing capabilities. It is better to refer to Emacs as an “extensible computing environment”. However, that phrase is quite a mouthful. It is easier to refer to Emacs simply as an editor. Moreover, everything you do in Emacs—find the Mayan date and phases of the moon, simplify polynomials, debug code, manage files, read letters, write books—all these activities are kinds of editing in the most general sense of the word.)

Although Emacs Lisp is usually thought of in association only with Emacs, it is a full computer programming language. You can use Emacs Lisp as you would any other programming language. 
''',
'2009'),
('The Not So Short Introduction to LaTeX','LaTeX','Tobias Oetiker (more)','pdf','http://tobi.oetiker.ch/lshort/lshort.pdf',
'''
LATEX is a typesetting system that is very suitable for producing scientiﬁc and mathematical documents of high typographical quality. It is also suitable for producing all sorts of other documents, from simple letters to complete books. LATEX uses TEX [2] as its formatting engine.

This short introduction describes LATEX 2ε and should be suﬃcient for most applications of LATEX. Refer to [1, 3] for a complete description of the LATEX system.''',
'2011'),
('Modern Perl','Perl','Chromatic','pdf','http://www.onyxneon.com/books/modern_perl/modern_perl_a4.pdf',
'''
In 1987, Perl 1.0 changed the world. In the decades since then, the language has grown from a simple tool for system administration somewhere between shell scripting and C programming to a powerful, general purpose language steeped in a rich heritage.

Even so, most Perl 5 programs in the world take far too little advantage of the language. You can write Perl 5 programs as if they were Perl 4 programs (or Perl 3 or 2 or 1), but programs written to take advantage of everything amazing the worldwide Perl 5 community has invented, polished, and discovered are shorter, faster, more powerful, and easier to maintain than their alternatives. They solve difficult problems with speed and elegance. They take advantage of the CPAN and its unparalleled library of reusable code. They get things done.

This productivity can be yours, whether you've dabbled with Perl for a decade or someone just handed you this book and said "Fix this code by Friday." Modern Perl is suitable for programmers of every level. It's more than a Perl tutorial—only Modern Perl focuses on Perl 5.12 and 5.14, to demonstrate the latest and most effective time-saving features. Only Modern Perl explains how and why the language works, to let you unlock the full power of Perl. When you have to solve a problem now, reach for Perl. When you have to solve a problem right, reach for Modern Perl.''',
'2012')

, ("Mining of Massive Datasets","Big Data","Anand Rajaraman (more)","pdf",'http://infolab.stanford.edu/~ullman/mmds/book.pdf',
	'''
At the highest level of description, this book is about data mining. However, it focuses on data mining of very large amounts of data, that is, data so large it does not fit in main memory. 

Because of the emphasis on size, many of our examples are about the Web or data derived from the Web. Further, the book takes an algorithmic point of view: data mining is about applying algorithms to data, rather than using data to "train" a machine-learning engine of some sort.''',
'2013')
, ('How Computers Work','Computing','Roger Young','pdf','http://www.fastchip.net/howcomputerswork/bookbpdf.pdf',
	'''
Computers are the most complex machines that have ever been created. Very few people really know how they work. This book will tell you how they work and no technical knowledge is required. It explains the operation of a simple, but fully functional, computer in complete detail. The simple computer described consists mainly of a processor and main memory. Relays, which are explained, are used in the circuitry instead of transistors for simplicity. This book does not cover peripherals like modems, mice, disk drives, or monitors.

Did you ever wonder what a bit, a pixel, a latch, a word (of memory), a data bus, an address bus, a memory, a register, a processor, a timing diagram, a clock (of a processor), an instruction, or machine code is? Though most explanations of how computers work are a lot of analogies or require a background in electrical engineering, this book will tell you precisely what each of them is and how each of them works without requiring any previous knowledge of computers or electronics. 
''',
'2002')

, ('How to Write Parallel Programs','Parallel Programming','Nicholas Carriero (more)','pdf','http://lindaspaces.com/book/book.pdf',
	'''
This book is the raw material for a hands-on, "workshop" type course for undergraduates or graduate students in parallel programming. It can also serves as the core of a more conventional course; and it might profitably be read (we hope and believe) by any professional or researcher who needs an up-to-date synthesis of this fast-growing, fast-changing and fast-maturing field.

The programming examples and exercises use C-Linda (Linda is a registered trademark of Scientific Computing Associates.); C-Linda running on a parallel machine or a network is the ideal lab environment for the workshop course we've described. A C-Linda simulator running on a standard workstation is an adequate environment. Relying on some other parallel language or programming system is perfectly okay as well. The called-for translations between the book and the lab environment might be slightly painful (particularly if the non-Linda parallel language you choose is any variant of the ubiquitous message-passing or remote-procedure-call models), but these translation exercises are always illuminating, and anyway, they build character.''',
'1992')
,('Beautiful Code, Compelling Evidence','Haskell','Jeff Heard','pdf','http://vis.renci.org/jeff/wp-content/uploads/2009/01/beautifulcode.pdf',
'''
This is a tutorial I presented at ICFP last year on visualization and graphics in Haskell.  
It talks at length about why functional programming is a good idea for graphics, and then presents the basic tools that exist today.
''',
'2008'),
('Version Control by Example','Version Control','Eric Sink','pdf','http://www.ericsink.com/vcbe/vcbe_a4_lo.pdf',
'''
This book uses practical examples to explain version control with both centralized and decentralized systems.  Topics covered include:

• Basic version control commands and concepts
• Introduction to Distributed Version Control Systems (DVCS)
• Advanced branching workflows
• Strengths and weaknesses of DVCS vs. centralized tools
• Best practices
• How distributed version control works under the hood

Featuring these open source version control tools:

• Apache Subversion
• Mercurial
• Git
• Veracity

''',
'2011'),
('Learning Statistics with R','R','Daniel Navarro','pdf','http://health.adelaide.edu.au/psychology/ccs/docs/lsr/lsr-0.3.pdf',
'''
Since 2011 I (Dan) have been teaching an introductory statistics class for psychology students, using the R statistical package as the primary tool. 
Because I was a little unhappy with the textbooks available at the time, I started writing my own. The book is still a work in progress, but it has reached a "first draft" stage, at 542 pages. 
''',
'2013')

,('Smooth CoffeeScript','CoffeeScript','E. Hoigaard','pdf','http://autotelicum.github.io/Smooth-CoffeeScript/Smooth%20CoffeeScript%20Web%20Optimized.pdf',
'''
Smooth CoffeeScript is a book about CoffeeScript and programming. Start with programming fundamentals, learn about functional programming with Underscore and problem solving, study object orientation and modularity. It covers client/server web apps with Canvas and WebSockets.

No previous programming knowledge is required. CoffeeScript lets you write web oriented applications simply and elegantly. It is closely related to JavaScript but without its quirky corners. 
''','2011'),
('Text Algorithms','Text Processing','Maxime Crochemore','pdf','http://igm.univ-mlv.fr/~mac/REC/text-algorithms.pdf',
'''
One of the simplest and natural types of information representation is by means of written texts. Data to be processed often does not decompose into independent records. This type of data is characterized by the fact that it can be written down as a long sequence of characters. Such linear sequence is called a text. The texts are central in "word processing" systems, which provide facilities for the manipulation of texts. Such systems usually process objects which are quite large. For example, this book contains probably more than a million characters. Text algorithms occur in many areas of science and information processing. Many text editors and programming languages have facilities for processing texts. In biology, text algorithms arise in the study of molecular sequences. The complexity of text algorithms is also one of the central and most studied problems in theoretical computer science. It could be said that it is the domain where the practice and theory are very close together.

'''	,'1997'),
('Producing Open Source Software','Open Source','Karl Fogel','pdf','http://producingoss.com/en/producingoss.pdf',
'''
At parties, people no longer give me a blank stare when I tell them I write free software. "Oh, yes, open source—like Linux?" they say. I nod eagerly in agreement. "Yes, exactly! That's what I do." It's nice not to be completely fringe anymore. In the past, the next question was usually fairly predictable: "How do you make money doing that?" To answer, I'd summarize the economics of open source: that there are organizations in whose interest it is to have certain software exist, but that they don't need to sell copies, they just want to make sure the software is available and maintained, as a tool instead of a commodity.

Lately, however, the next question has not always been about money. The business case for open source software is no longer so mysterious, and many non-programmers already understand—or at least are not surprised—that there are people employed at it full time. Instead, the question I have been hearing more and more often is "Oh, how does that work?"

I didn't have a satisfactory answer ready, and the harder I tried to come up with one, the more I realized how complex a topic it really is. Running a free software project is not exactly like running a business (imagine having to constantly negotiate the nature of your product with a group of volunteers, most of whom you've never met!). Nor, for various reasons, is it exactly like running a traditional non-profit organization, nor a government. 
'''	,'2013'),
('Making Games with Python & Pygame','Python / Pygame', 'Al Sweigart','pdf','http://inventwithpython.com/makinggames.pdf',
'''
“Making Games with Python & Pygame” covers the Pygame library with the source code for 11 games. “Making Games” was written as a sequel for the same age range as “Invent with Python”. Once you have an understanding of the basics of Python programming, you can now expand your abilities using the Pygame library to make games with graphics, animation, and sound.

The book features the source code to 11 games. The games are clones of classics such as Nibbles, Tetris, Simon, Bejeweled, Othello, Connect Four, Flood It, and others.
''','2012'),
('''Beej's Guide to C Programming''','C','''Brian 'Beej' Hall''','pdf','http://beej.us/guide/bgc/output/print/bgc_A4.pdf',
'''
The bad news is that if you're a beginner in this whole thing, all C code you see looks obfuscated! The good news is, it's not going to be that way for long.
What we'll try to do over the course of this guide is lead you from complete and utter sheer lost confusion on to the sort of enlightened bliss that can only be obtained though pure C programming. Right on.

As with most Beej's Guides, this one tries to cater to people who are just starting on the topic. That's you! If that's not you for whatever reason the best I can hope to provide is some pastey entertainment for your reading pleasure. The only thing I can reasonably promise is that this guide won't end on a cliffhanger...or will it?

'''
,'2007' ),
('The New C Standard','C','Derek M. Jones','pdf','http://www.coding-guidelines.com/cbook/cbook1_2.pdf',
'''
This book contains a detailed analysis of the International Standard for the C language, excluding the library from a number of perspectives. The organization of the material is unusual in that it is based on the actual text of the published C Standard. The unit of discussion is the individual sentences from the C
Standard (2043 of them). 

Readers are assumed to have more than a passing familiarity with C.

''',
'2009'),
('Think Bayes','Bayesian Statistics','Allen B. Downey','pdf','http://www.greenteapress.com/thinkbayes/thinkbayes.pdf',
'''
Think Bayes is an introduction to Bayesian statistics using computational methods. This version of the book is a rough draft. I am making this draft available for comments, but it comes with the warning that it is probably full of errors. 
''','2012'	),
('Free Software, Free Society','Freedom','Richard Stallman','pdf','http://www.gnu.org/doc/fsfs-ii-2.pdf',
'''
This book collects the writing of Richard Stallman in a manner that will make its subtlety and power clear. The essays span a wide range, from copyright to the history of the free software movement. They include many arguments not well known, and among these, an especially insightful account of the changed circumstances that render copyright in the digital world suspect. They will serve as a resource for those who seek to understand the thought of this most powerful man--powerful in his ideas, his passion, and his integrity, even if powerless in every other way. They will inspire other who would take these ideas, and build upon them.
''','2010'),
('The Future of Ideas','Internet','Lawrence Lessig','pdf','http://web.archive.org/web/20110716220221/http://www.the-future-of-ideas.com/download/lessig_FOI.pdf',
'''
The Internet revolution has come. Some say it has gone. What was responsible for its birth? Who is responsible for its demise? In The Future of Ideas, Lawrence Lessig explains how the Internet revolution has produced a counterrevolution of devastating power and effect. The explosion of innovation we have seen in the environment of the Internet was not conjured from some new, previously unimagined technological magic; instead, it came from an ideal as old as the nation. Creativity flourished there because the Internet protected an innovation commons. The Internet's very design built a neutral platform upon which the widest range of creators could experiment. The legal architecture surrounding it protected this free space so that culture and information, the ideas of our era, could flow freely and inspire an unprecedented breadth of expression. But this structural design is changing, both legally and technically.

This shift will destroy the opportunities for creativity and innovation that the Internet originally engendered. ''',
'2001'),
('Learning Go','Go','Miek Gieben','pdf','http://www.miek.nl/files/go/20130612-go.pdf',
'''
This is an introduction to the Go language from Google. Its aim is to provide a guide to this new and innovative language.

The intended audience of this book is people who are familiar with programming and know some programming languages, be it C[3], C++[23], Perl[5], Java[16], Erlang[4], Scala[17] or Haskell[1]. This is not a book that teaches you how to program, this is a book that just teaches you how to use Go.

As with learning new things, probably the best way to do this is to discover it for yourself by creating your own programs. Each chapter therefore includes a number of exercises (and answers) to acquaint you with the language.
''',
'2012'),
('Data Structures & Algorithms Analysis in C++','C++','Clifford A. Schaffer','pdf','http://people.cs.vt.edu/~shaffer/Book/C++3e20130328.pdf',
'''
We study data structures so that we can learn to write more efficient programs. But why must programs be efficient when new computers are faster every year?
The reason is that our ambitions grow with our capabilities. Instead of rendering efficiency needs obsolete, the modern revolution in computing power and storage capability merely raises the efficiency stakes as we attempt more complex tasks. The quest for program efficiency need not and should not conflict with sound design and clear coding. Creating efficient programs has little to do with “program-ming tricks” but rather is based on good organization of information and good algorithms. A programmer who has not mastered the basic principles of clear design is not likely to write efficient programs. Conversely, concerns related to develop-
ment costs and maintainability should not be used as an excuse to justify inefficient performance. Generality in design can and should be achieved without sacrificing performance, but this can only be done if the designer understands how to measure performance and does so as an integral part of the design and implementation process. 

''',
'2013'),
('Data Structures & Algorithms Analysis in Java','Java','Clifford A. Schaffer','pdf','http://people.cs.vt.edu/~shaffer/Book/JAVA3e20130328.pdf',
'''
We study data structures so that we can learn to write more efficient programs. But why must programs be efficient when new computers are faster every year?
The reason is that our ambitions grow with our capabilities. Instead of rendering efficiency needs obsolete, the modern revolution in computing power and storage capability merely raises the efficiency stakes as we attempt more complex tasks. The quest for program efficiency need not and should not conflict with sound design and clear coding. Creating efficient programs has little to do with “program-ming tricks” but rather is based on good organization of information and good algorithms. A programmer who has not mastered the basic principles of clear design is not likely to write efficient programs. Conversely, concerns related to develop-
ment costs and maintainability should not be used as an excuse to justify inefficient performance. Generality in design can and should be achieved without sacrificing performance, but this can only be done if the designer understands how to measure performance and does so as an integral part of the design and implementation process.
''',
'2013'),
('Big Fat Rails','Ruby on Rails','Mitch Guthrie','pdf','http://www.bigfatrails.com/ebooks/bigfatrails-0.7.4.beta.pdf',
'''
There are many resources out there for learning Rails. I've used many myself. The reason to add one more to an already long list may seem needless at best and stupid at worst. The driving factor is simply this: The more resources available to the beginner the better chance they have to become proficient at the subject.

When I'm learning something new I always find several resources to learn from. Often buying many books on the subject. Each resource provides a different point of view, teaching method, or simply a format which I learn better from. It is my intention to provide another resource that may help others better understand everything available to them. 
''',
'2012'	),
('An Introduction to R','R','W.N. Venables (more)','pdf','http://cran.r-project.org/doc/manuals/R-intro.pdf',
'''
This introduction to R is derived from an original set of notes describing the S and SPlus environments written in 1990–2 by Bill Venables and David M. Smith when at the University of Adelaide.
''',
'2013'),
('Version Control with Subversion','Subversion','Ben Collins-Sussman (more)','pdf','http://svnbook.red-bean.com/en/1.7/svn-book.pdf',
'''
In the world of open source software, the Concurrent Versions System (CVS) was the tool of choice for version control for many years. And rightly so. CVS was open source software itself, and its nonrestrictive modus operandi and support for networked operation allowed dozens of geographically dispersed programmers to share their work. It fit the collaborative nature of the open source world very well. CVS and its semi-chaotic development model have since become cornerstones of open source culture.

But CVS was not without its flaws, and simply fixing those flaws promised to be an enormous effort. Enter Subversion. Subversion was designed to be a successor to CVS, and its originators set out to win the hearts of CVS users in two ways—by creating an open source system with a design (and “look and feel”) similar to CVS, and by attempting to avoid most of CVS's noticeable flaws. While the result wasn't—and isn't—the next great evolution in version control design, Subversion is very powerful, very usable, and very flexible.
''','2011'
	),
('Introduction to Good Usability','Usability','Peter Conradie','pdf','http://www.peterpixel.nl/projects/ebook/introduction_to_good_usability.pdf',
'''
Over the past year I have written a few posts about design guidelines. They have also proven to be the most successful ones. I have therefor decided to put a few of them together, add some more and bundle it as an ebook. So without much further ado, I present:

''','2008'),
('Using R for Data Analysis and Graphics','R','J.H. Maindonald','pdf','http://cran.r-project.org/doc/contrib/usingR.pdf',
'''
These notes are designed to allow individuals who have a basic grounding in statistical methodology to work through examples that demonstrate the use of R for a range of types of data manipulation, graphical presentation and statistical analysis. Books that provide a more extended commentary on the methods illustrated in these examples include Maindonald and Braun (2003).

''','2008'),
('Programming Computer Vision with Python','Computer Vision','Jan Erik Solem','pdf','http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf',
'''
Today, images and video are everywhere. Online photo sharing sites and social networks have them in the billions. Search engines will produce images of just about any conceivable query. Practically all phones and computers come with built in cameras. It is not uncommon for people to have many gigabytes of photos and videos on their devices.
Programming a computer and designing algorithms for understanding what is in these images is the field of computer vision. Computer vision powers applications like image search, robot navigation, medical image analysis, photo management and many more.

The idea behind this book is to give an easily accessible entry point to hands-on computer vision with enough understanding of the underlying theory and algorithms to be a foundation for students, researchers and enthusiasts. The Python programming language, the language choice of this book, comes with many freely available powerful modules for handling images, mathematical computing and data mining.
''',
'2012'),
('Markdown Cheat Sheet','MarkDown','Mark Boszko','pdf','http://stationinthemetro.com/storage/dev/Markdown_Cheat_Sheet_v1-1.pdf',
'''
This is a cheat sheet to cover most of the markups used in the Markdown markup language. 
It is now widely used in several blog management systems, and readme files on github, for example. 
''',''),
('Algorithms Course Material','Algorithms','Jeff Erikson','pdf','http://compgeom.cs.uiuc.edu/~jeffe/teaching/algorithms/everything.pdf',
'''
This page contains all my lecture notes for the algorithms classes required for all computer science undergraduate and graduate students at the University of Illinois, Urbana-Champaign. I have taught incarnations of this course eight times: Spring 1999, Fall 2000, Spring 2001, Fall 2002, Spring 2004, Fall 2005, Fall 2006, Spring 2007, Fall 2008, Spring 2009, Spring 2010, and Fall 2010. These notes are numbered roughly in the order I use them in my undergraduate class.
This PDF file is 814 pages long.''','2011'),
('Coding Freedom','Freedom','Gabriella Coleman','pdf','http://gabriellacoleman.org/Coleman-Coding-Freedom.pdf','''
Who are computer hackers? What is free software? And what does the emergence of a community dedicated to the production of free and open source software–and to hacking as a technical, aesthetic, and moral project–reveal about the values of contemporary liberalism? Exploring the rise and political significance of the free and open source software (F/OSS) movement in the United States and Europe, Coding Freedom details the ethics behind hackers’ devotion to F/OSS, the social codes that guide its production, and the political struggles through which hackers question the scope and direction of copyright and patent law. In telling the story of the F/OSS movement, the book unfolds a broader narrative involving computing, the politics of access, and intellectual property.

E. Gabriella Coleman tracks the ways in which hackers collaborate and examines passionate manifestos, hacker humor, free software project governance, and festive hacker conferences. ''',
'2013'),
('Free as in Freedom','Freedom','Sam Williams','pdf','http://static.fsf.org/nosvn/faif-2.0.pdf',
'''
In 2002, Sam Williams wrote Free as in Freedom, a biography of Richard M. Stallman. In its epilogue, Williams expressed hope that choosing to distribute his book under the GNU Free Documentation License would enable and encourage others to share corrections and their own perspectives through modifications to his work.

Free as in Freedom (2.0) is Stallman’s revision of the original biography. While preserving Williams’s viewpoint, it includes factual corrections and extensive new commentary by Stallman, as well as new prefaces by both authors written for the occasion. It is a rare kind of biography, where the reader has the benefit of both the biographer’s original words and the subject’s response.
''','2010'),
('''Don't just roll the dice''','Software Pricing','Neil Davidson','pdf','http://neilgd.wpengine.com/wp-content/uploads/2011/12/dontjustrollthedice.pdf','''
How do you price your software? Is it art, science or magic? How much attention should you pay to your competitors? This short handbook will provide you with the theory, practical advice and case studies you need to stop yourself from reaching for the dice.

At Business of Software 2007 Michael Pryor held an impromptu session on how to price your software. So many people turned up, and so many people kept on arriving, that by the time they’d introduced themselves there was no time left to talk about software pricing. I’ve had similar experiences; in fact, “How do I price my software?” is probably the most common question I’m asked by software entrepreneurs and product managers. This handbook is an attempt to answer that question.” Neil Davidson, Author. About the Author Neil Davidson is co-founder and joint CEO of Red Gate Software. Red Gate was founded in 1999 and now employs some 150 people. It was Cambridge News business of the year in 2006 and has been in the Sunday Times top 100 companies to work for three years running. It was founded with no VC money and little debt. Neil is also founder of the annual Business of Software conference and runs the Business of Software social network. ''',
'2011'),
('Introduction to Embedded Systems','Embedded Systems','Edward Ashford Lee (more)','pdf','http://leeseshia.org/releases/LeeSeshia_DigitalV1_08.pdf',
'''
This book is intended for students at the advanced undergraduate level or the introductory graduate level, and for practicing engineers and computer scientists who wish to understand the engineering principles of embedded systems. 

This book strives to identify and introduce the durable intellectual ideas of embedded systems as a technology and as a subject of study. The emphasis is on modeling, design, and analysis of cyber-physical systems, which integrate computing, networking, and physical processes. This book is divided into three major parts, focused on modeling, design, and analysis.
''',
'2011'),
('Linux Kernel Crash Book','Linux','Igor Ljubuncic','pdf','https://www.dropbox.com/s/ktbz9fy7qbwsyfa/www.dedoimedo.com-crash-book.pdf','''
“Linux Kernel Crash Book”, by Igor Ljubuncic, starts with crash tools via collection all the way to analysis, plus some extras and general tips. Linux kernel crash analysis is not an everyday topic. It is very likely a niche topic, which will interest only system administrators and professionals dabbling in the kernel. 

This condition may stop you from reading the book, as you may not be either the person maintaining server boxes nor the code developer trying to debug his drivers.

However, you may also consider this book as a very extensive learning lesson in what goes behind the curtains of a typical Linux system. While you may not find immediate use to the contents presented in this book, the general knowledge and problem solving methods and tools you find here should serve you universally. Come the day, come the opportunity, you will find this book of value.
	''',''),
('The R Inferno',"R",'Patrick Burns','pdf','http://www.burns-stat.com/pages/Tutor/R_inferno.pdf',
'''
An essential guide to the trouble spots and oddities of R. In spite of the quirks exposed here, R is the best computing environment for most data analysis tasks. R is free, open-source, and has thousands of contributed packages. It is used in such diverse fields as ecology, finance, genomics and music. If you are using spreadsheets to understand data, switch to R. You will have safer – and ultimately, more convenient – computations.
''','2011'),
('An Introduction to Programming in Go', 'Go','Caleb Doxsey','pdf','http://www.golang-book.com/assets/pdf/gobook.pdf',
'''
This book is a short, concise introduction to computer programming using the language Go. Designed by Google, Go is a general purpose programming language with modern features, clean syntax and a robust well-documented common library, making it an ideal language to learn as your first programming language.
''','2012'
	),
('Git Magic','Git','Ben Lynn','pdf','http://www-cs-students.stanford.edu/~blynn/gitmagic/book.pdf',
'''
As Arthur C. Clarke observed, any sufficiently advanced technology is indistinguishable from magic. This is a great way to approach Git: newbies can ignore its inner workings and view Git as a gizmo that can amaze friends and infuriate enemies with its wondrous abilities. Rather than go into details, we provide rough instructions for particular effects. After repeated use, gradually you will understand how each trick works, and how to tailor the recipes for your needs. 
''',
'2007'),
("Harry Potter and the Methods of Rationality",'Rationality','Eliezer Yudkowsky','pdf','http://hpmor.com/wordpress/wp-content/uploads/2012/03/Harry-Potter-and-the-Methods-of-Rationality.pdf',
'''
Harry Potter fanfic-in-progress, Harry Potter and the Methods of Rationality.
''','2013'
),
('TeX for the Impatient','TeX','Paul Abrahams (more)','pdf','http://mirror.ctan.org/info/impatient/book.pdf',
'''
TEX, a software system created by Donald E. Knuth, sets the standard for typesetting in mathematics, science, and engineering. “TEX for the Impatient” is a handbook that arose from the need to help technical writers learn TEX more quickly and once having learned it, to find fast answers to common questions. Clear, concise, and accessible, this book is organized for easy retrieval of information, thoroughly indexed, and carefully designed for learning by example.

TEX for the Impatient is intended to serve scientists, mathematicians, and technical typists for whom TEX is a useful tool rather than a primary interest, as well as computer people who have a strong interest in TEX for its own sake. We also intend it to serve both newcomers to TEX and those who are already familiar with TEX. We assume that our readers are comfortable working with computers and that they want to get the information they need as quickly as possible. Our aim is to provide that information clearly, concisely, and accessibly. This book therefore provides a bright searchlight, a stout walking-stick, and detailed maps for exploring and using TEX.''',
'2003'),
('Data-Intensive Text Processing with MapReduce','MapReduce','Jimmy Lin (more)','pdf','http://www.umiacs.umd.edu/~jimmylin/MapReduce-book-final.pdf',
'''
MapReduce [45] is a programming model for expressing distributed computations on massive amounts of data and an execution framework for large-scale data processing on clusters of commodity servers. It was originally developed by Google and built on well-known principles in parallel and distributed processing dating back several decades. MapReduce has since enjoyed widespread adoption via an open-source implementation called Hadoop, whose development was led by Yahoo (now an Apache project). Today, a vibrant software ecosystem has sprung up around Hadoop, with significant activity in both industry and academia.

This book is about scalable approaches to processing large amounts of text with MapReduce. Given this focus, it makes sense to start with the most basic question: Why? There are many answers to this question, but we focus on two. First, “big data” is a fact of the world, and therefore an issue that real-world systems must grapple with. Second, across a wide range of text processing applications, more data translates into more effective algorithms, and thus it makes sense to take advantage of the plentiful amounts of data that surround us.

''',
'2010'),
('GNU Make Manual','GNU Make','FSF','pdf','https://www.gnu.org/software/make/manual/make.pdf',
'''
Official Manual for GNU Make by the Free Software Foundation
''',
'2010'	),
('Basics of Compiler Design','Compilers','Torben Mogensen','pdf','http://www.diku.dk/hjemmesider/ansatte/torbenm/Basics/basics_lulu2.pdf',
'''
In order to reduce the complexity of designing and building computers, nearly all of these are made to execute relatively simple commands (but do so very quickly). A program for a computer must be built by combining these very simple commands into a program in what is called machine language. Since this is a tedious and error-prone process most programming is, instead, done using a high-level programming language. This language can be very different from the machine language that the computer can execute, so some means of bridging the gap is required. This is where the compiler comes in.

A compiler translates (or compiles) a program written in a high-level programming language that is suitable for human programmers into the low-level machine language that is required by computers. During this process, the compiler will also attempt to spot and report obvious programmer mistakes.

''',
'2010'),
('Logic, Programming and Prolog','Prolog','Ulf Nilsson (more)','pdf','https://www.ida.liu.se/~ulfni/lpp/bok/bok.pdf',
'''
The main objective of both editions of this textbook is to provide a uniform account of both the foundations of logic programming and simple programming techniques in the programming language Prolog. The discussion of the foundations also facilitates a systematic survey of variants of the logic programming scheme, like constraint logic programming, deductive databases or concurrent logic programming. This book is not primarily intended to be a theoretical handbook on logic programming. Nor is it intended to be a book on advanced Prolog programming or on constraint logic programming. For each of these topics there are more suitable books around. Because of the diversity of the field there is of course a risk that nothing substantial is said about anything. We have tried to compensate for this risk by limiting our attention to (what we think are) the most important areas of logic programming and by providing the interested reader with pointers containing suggestions for further reading.
''',
'2000'),
('PyGTK 2.0 Tutorial','PyGTK','John Finlay','pdf','http://www.pygtk.org/dist/pygtk2-tut.pdf',
'''
PyGTK 2.0 is a set of Python modules which provide a Python interface to GTK+ 2.X. Throughout the rest of this document PyGTK refers to the 2.X version of PyGTK and GTK and GTK+ refer to the 2.X version of GTK+. The primary web site for PyGTK is www.pygtk.org. The primary author of PyGTK is: • James Henstridge (james@daa.com.au) who is assisted by the developers listed in the AUTHORS ﬁle in the PyGTK distribution and the PyGTK community.
''','2012'),
('Python Programming', 'Python','Wikibooks','pdf','https://upload.wikimedia.org/wikipedia/commons/9/91/Python_Programming.pdf',
'''
Python is a high-level, structured, open-source programming language that can be used for a wide variety of programming tasks. Python was created by Gudio Van Rossum in the early 1990s, its following has grown steadily and interest is increased markedly in the last few years or so. It is named after Monty Python's Flying Circus comedy program.

Python is used extensively for system administration (many vital components of Linux Distributions are written in it), also its a great language to teach programming to novice. NASA has used Python for its software systems and has adopted it as the standard scripting language for its Integrated Planning System. Python is also extensively used by Google to implement many components of its Web Crawler and Search Engine & Yahoo! for managing its discussion groups.
''','2012'),
('LaTeX','LaTeX','Wikibooks','pdf','https://upload.wikimedia.org/wikipedia/commons/2/2d/LaTeX.pdf',
'''
This is a book from Wikibooks about LaTeX, one of the most popular Macro packages for TeX.  
''','2013'),
('Code Version 2.0','Freedom','Lawrence Lessig','pdf','http://codev2.cc/download+remix/Lessig-Codev2.pdf',
'''
"This is a translation of an old book—indeed, in Internet time, it is a translation of an ancient text." That text is Lessig's "Code and Other Laws of Cyberspace." The second version of that book is "Code v2." The aim of Code v2 is to update the earlier work, making its argument more relevant to the current internet.

Code v2 was written in part through a collaborative Wiki.
'''
,'2006'),
('Matters Computational','Algorithms','Jorg Arndt','pdf','http://www.jjj.de/fxt/fxtbook.pdf',
'''
This is a book for the computationalist, whether a working programmer or anyone interested in methods of computation. The focus is on material that does not usually appear in textbooks on algorithms. Where necessary the underlying ideas are explained and the algorithms are given formally. It is assumed that the reader is able to understand the given source code, it is considered part of the text. We use the C++ programming language for low-level algorithms. However, only a minimal set of features beyond plain C is used, most importantly classes and templates. For material where technicalities in the C++ code would obscure the underlying ideas we use either pseudocode or, with arithmetical algorithms, the GP language. Appendix C gives an introduction to GP.
'''
,'2010'),
('Linux on the Road','Linux','Werner Heuser','pdf','http://tldp.org/LDP/Mobile-Guide/Mobile-Guide.pdf',
'''
Though there are laptop, notebook, PDA and mobile phone related HOWTOs available already, this guide contains a concise survey of documents related to mobile computer devices. Also Linux features, such as installation methods for laptops, notebooks and PDAs as well as configurations for different (network) environments are described.

Although there are some caveats, Linux is a better choice for mobile computer devices than most other operating systems. Because it supports numerous installation methods, works in many heterogenoues environments and needs smaller resources. 
''','2011'),
('Bash Guide for Beginners','Bash','Machtelt Garrels','pdf','http://tldp.org/LDP/Bash-Beginners-Guide/Bash-Beginners-Guide.pdf',
'''
The Bash Guide for Beginners gets you started with Bash scripting and bridges the gap between the Bash HOWTO and the Advanced Bash Scripting Guide. Everybody who wants to make life easier on themselves, power users and sysadmins alike, can benefit from reading this practical course. The guide contains lots of examples and exercises at the end of each chapter, demonstrating the theory and helping you practice. Bash is available on a wide variety of UNIX, Linux, MS Windows and other systems. 
''','2011'),
('Introduction to Linux - A Hands on Guide','Linux','Machtelt Garrels','pdf','http://tldp.org/LDP/intro-linux/intro-linux.pdf',
'''
This guide was created as an overview of the Linux Operating System, geared toward new users as an exploration tour and getting started guide, with exercises at the end of each chapter. For more advanced trainees it can be a desktop reference, and a collection of the base knowledge needed to proceed with system and network administration. This book contains many real life examples derived from the author's experience as a Linux system and network administrator, trainer and consultant. We hope these examples will help you to get a better understanding of the Linux system and that you feel encouraged to try out things on your own. 
''','2008'),
('GNU/Linux Command-Line Tools Summary','Command Line','Gareth Anderson','pdf','http://tldp.org/LDP/GNU-Linux-Tools-Summary/GNU-Linux-Tools-Summary.pdf',
'''
This document is an attempt to provide a summary of useful command-line tools available to a GNU/Linux based operating system, the tools listed are designed to benefit the majority of users and have being chosen at the authors discretion. This document is not a comprehensive list of every existent tool available to a GNU/Linux based system, nor does it have in-depth explanations of how things work. It is a summary which can be used to learn about and how to use many of the tools available to a GNU/Linux-based operating system. 
''','2006'),
('''The Linux System Administrators' Guide''','Linux','Lars Wirzenius (more)','pdf','http://tldp.org/LDP/sag/sag.pdf',
'''
This book cover all of the aspects of keeping the system running, handling user accounts, backups, configuration of the system, installing and upgrading software, and more. Whereas some of this information is in the Installation Guide (just to get the system off the ground) this book should be much more complete.
''','2005'),
('Pocket Linux Guide','Linux','David Horton','pdf','http://tldp.org/LDP/Pocket-Linux-Guide/Pocket-Linux-Guide.pdf',
'''
The Pocket Linux Guide is for anyone interested in learning the techniques of building a GNU/Linux system from source code. The guide is structured as a project that builds a small diskette-based GNU/Linux system called Pocket Linux. Each chapter explores a small piece of the overall system explaining how it works, why it is needed and how to build it. After completing the Pocket Linux project, readers should possess an enhanced knowledge of what makes GNU/Linux systems work as well as the confidence to explore larger, more complex source-code-only projects. 
''','2005'),
('Linux Dictionary','Linux','Binh Nguyen','pdf','http://tldp.org/LDP/Linux-Dictionary/Linux-Dictionary.pdf',
'''
A Dictionary for all elements related to GNU/Linux systems.
''','2005'),
('Linux from Scratch','Linux','Gerard Beekmans','pdf','http://tldp.org/LDP/lfs/LFS-BOOK-6.1.1.pdf',
'''
Derived from the popular Linux-From-Scratch-HOWTO, this book describes the process of creating your own Linux system from scratch from an already installed Linux distribution, using nothing but the sources of software that are needed.
''','2005'),
('The OpenGL Shading Language','OpenGL','John Kessenich (more)','pdf','http://www.opengl.org/registry/doc/GLSLangSpec.4.30.6.pdf',
'''
This document describes a programming language that is a companion to OpenGL 2.0 and higher, called The OpenGL Shading Language. The OpenGL Shading Language is part of the core OpenGL 4.3 specification.
''','2012'),
('The OpenGL 4.3 specification','OpenGL','Mark Segal (more)','pdf','http://www.opengl.org/registry/doc/glspec43.core.20120806.pdf',
'''
This document, referred to as the “OpenGL Specification” or just “Specification” hereafter, describes the OpenGL graphics system: what it is, how it acts, and what is required to implement it. We assume that the reader has at least a rudimentary understanding of computer graphics. This means familiarity with the essentials of computer graphics algorithms and terminology as well as with modern GPUs (Graphic Processing Units).
''','2012'),
('Database Fundamentals', 'Databases', 'Neeraj Sharma (more)','pdf','http://public.dhe.ibm.com/software/dw/db2/express-c/wiki/Database_fundamentals.pdf',
'''
This book is tailored for new database enthusiasts, application developers, database administrators, and anyone with an interest in the subject and looking to get exposure such as university students and new graduates.

This book is divided into chapters, starting with the basic database concepts and information models in Chapter 1. Chapter 2 covers relational data models. Chapter 3 and 4 explain conceptual modeling and relational database design. In Chapters 5, 6 and 7 the focus is geared towards SQL. Chapter 8 highlights XML data storage and retrieval via SQL and XQuery. Chapter 9 addresses database security aspects. The book then concludes with an overview of various other key technologies and relevant applications that are increasingly popular in the industry today.

''',
'2010'),
('Introduction to Information Retrieval','Information Retrieval','Christopher D. Manning (more)','pdf','http://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf',
'''
This book is the result of a series of courses we have taught at Stanford University and at the University of Stuttgart, in a range of durations including a single quarter, one semester and two quarters. These courses were aimed at early-stage graduate students in computer science, but we have also had enrollment from upper-class computer science undergraduates, as well as students from law, medical informatics, statistics, linguistics and various engineering disciplines. 

The first eight chapters of the book are devoted to the basics of information retrieval, and in particular the heart of search engines. Chapters 9–21 build on the foundation of the first eight chapters to cover a variety of more advanced topics. Chapters 13–17 give a treatment of various forms of machine learning and numerical methods in information retrieval. Chapters 16–18 consider the problem of inducing clusters of related documents from a collection. Chapters 19–21 treat the problem of web search.
''',
'2009'),
('Is Parallel Programming Hard?','Parallel Programming','Paul E. McKenney','pdf','http://kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook-1c.2013.01.13a.pdf',
'''
The purpose of this book is to help you understand how to program shared-memory parallel machines without risking your sanity.1 By describing the algorithms and designs that have worked well in the past, we hope to help you avoid at least some of the pitfalls that have beset parallel projects. But you should think of this book as a foundation on which to build, rather than as a completed cathedral. Your mission, if you choose to accept, is to help make further progress in the exciting field of parallel programming, progress that should in time render this book obsolete. Parallel programming is not as hard as it is reputed, and it is hoped that this book makes it even easier for you.
''',
'2013'),
('''Let's Build a Compiler''','Compilers','Jack W. Crenshaw','pdf','http://www.stack.nl/~marcov/compiler.pdf',
'''
This series of articles is a tutorial on the theory and practice of developing language parsers and compilers. Before we are finished, we will have covered every aspect of compiler construction, designed a new programming language, and built a working compiler.

Though I am not a computer scientist by education (my Ph.D. is in a different field, Physics), I have been interested in compilers for many years. I have bought and tried to digest the contents of virtually every book on the subject ever written. I don’t mind telling you that it was slow going. Compiler texts are written for Computer Science majors, and are tough sledding for the rest of us. But over the years a bit of it began to seep in. What really caused it to jell was when I began to branch off on my own and begin to try things on my own computer. Now I plan to share with you what I have learned. At the end of this series you will by no means be a computer scientist, nor will you know all the esoterics of compiler theory. I intend to completely ignore the more theoretical aspects of the subject. What you WILL know is all the practical aspects that one needs to know to build a working system.
''',
'2012'),
('Programming Languages: Application and Interpretation','Racket','Shriram Krishnamurthi','pdf','http://www.cs.brown.edu/courses/cs173/2012/book/book.pdf',
'''
Unlike some other textbooks, this one does not follow a top-down narrative. Rather it has the flow of a conversation, with backtracking. We will often build up programs incrementally, just as a pair of programmers would. We will include mistakes, not because I don’t know the answer, but because this is the best way for you to learn. Including mistakes makes it impossible for you to read passively: you must instead engage with the material, because you can never be sure of the veracity of what you’re reading.

At the end, you’ll always get to the right answer. However, this non-linear path is more frustrating in the short term (you will often be tempted to say, “Just tell me the answer, already!”), and it makes the book a poor reference guide (you can’t open up to a random page and be sure what it says is correct). However, that feeling of frustration is the sensation of learning. I don’t know of a way around it.
''','2012'),
('Optimizing Software in C++','C++','Agner Fog','pdf','http://www.agner.org/optimize/optimizing_cpp.pdf',
'''
This manual is for advanced programmers and software developers who want to make their software faster. It is assumed that the reader has a good knowledge of the C++ programming language and a basic understanding of how compilers work. The C++ language is chosen as the basis for this manual for reasons explained on page 8 below. This manual is based mainly on my study of how compilers and microprocessors work. The recommendations are based on the x86 family of microprocessors from Intel, AMD and VIA including the 64-bit versions. The x86 processors are used in the most common platforms with Windows, Linux, BSD and Mac OS X operating systems, though these operating systems can also be used with other microprocessors. Many of the advices may apply to other platforms and other compiled programming languages as well. 
''',
'2012'),
('Introduction to Programming using Java','Java','David J. Eck','pdf','http://math.hws.edu/eck/cs124/downloads/javanotes6-linked.pdf',
'''
This book is directed mainly towards beginning programmers, although it might also be useful for experienced programmers who want to learn something about Java. It is certainly not meant to provide complete coverage of the Java language.

The sixth edition requires Java 5.0 and can also be used with later versions of java. Almost all the examples in the book will work with Java 5.0, but some features from later versions of Java are also covered. You will find many Java applets on the web pages that make up this book, and most of those applets require Java 5.0 or higher to function. 
'''
,'2011'),
('Mathematical Logic - an Introduction','Logic','Unknown','pdf','http://www.ii.uib.no/~michal/und/i227/book/book.pdf',
'''
An introduction to Mathematical logic concepts with examples.
''','2011'),
('Operating Systems and Middleware','Middleware','Max Hailperin','pdf','https://gustavus.edu/mcs/max/os-book/osm-rev1.1.2.pdf',
'''
Working through this book, you will gain a general knowledge of how contemporary operating systems and middleware work and some idea why they work that way. That knowledge may be interesting in its own right, but it also has practical applications. Recall that these systems provide supporting APIs for application programmers to use. Therefore, one payoff will be that if you program applications, you will be positioned to make more effective use of the supporting APIs. Another payoff will be if you are in a role where you need to alter the configuration of an operating system or middleware product in order to tune its performance or make it best serve a particular context. Again, this one book alone won’t give you all the specific knowledge you need about any particular system, but it will give you the general background to make sense out of more specialized references. Perhaps the most significant payoff for learning the details of today’s systems in the context of the reasons behind their designs is that you will be in a better position to learn tomorrow’s systems.
''',
'2011'),
('The Little Book of Semaphores','Concurrency','Allen B. Downey','pdf','http://greenteapress.com/semaphores/downey08semaphores.pdf',
'''
The Little Book of Semaphores is a free (in both senses of the word) textbook that introduces the principles of synchronization for concurrent programming.

In most computer science curricula, synchronization is a module in an Operating Systems class. OS textbooks present a standard set of problems with a standard set of solutions, but most students don't get a good understanding of the material or the ability to solve similar problems.

The approach of this book is to identify patterns that are useful for a variety of synchronization problems and then show how they can be assembled into solutions. After each problem, the book offers a hint before showing a solution, giving students a better chance of discovering solutions on their own.

The book covers the classical problems, including "Readers-writers," "Producer-consumer", and "Dining Philosophers." In addition, it collects a number of not-so-classical problems, some written by the author and some by other teachers and textbook writers. Readers are invited to create and submit new problems. 
''','2008'),
('On Lisp','Lisp','Paul Graham','pdf','http://lib.store.yahoo.net/lib/paulgraham/onlisp.pdf',
'''
Not long ago, if you asked what Lisp was for, many people would have answered “for artificial intelligence.” In fact, the association between Lisp and AI is just an accident of history. Lisp was invented by John McCarthy, who also invented the term “artificial intelligence.” His students and colleagues wrote their programs in
Lisp, and so it began to be spoken of as an AI language. This line was taken up and repeated so often during the brief AI boom in the 1980s that it became almost an institution.

Fortunately, word has begun to spread that AI is not what Lisp is all about. Recent advances in hardware and software have made Lisp commercially viable: it is now used in Gnu Emacs, the best Unix text-editor; Autocad, the industry standard desktop CAD program; and Interleaf, a leading high-end publishing program. The way Lisp is used in these programs has nothing whatever to do with AI.
''','1993'),
('Common Lisp Quick Reference','Lisp','Bert Burgemeister','pdf','http://clqr.boundp.org/clqr-a4-booklet-all.pdf',
'''
Common Lisp Quick Reference is a free booklet with short descriptions of the thousand or so symbols defined in the ANSI standard. It comes with a comprehensive index.

This rather humble effort is by no means meant to rival the Common Lisp HyperSpec or any of the great introductory web resources and books. Its purpose is to give those who like a piece of dead tree in their hands a quick overview on things they know already, or some clue on what to look up elsewhere. 
''','2012'),
('Common Lisp','Lisp','David S. Touretzky','pdf','https://www.cs.cmu.edu/~dst/LispBook/book.pdf',
'''
This book is about learning to program in Lisp. Although widely known as the principal language of artificial intelligence research—one of the most advanced areas of computer science—Lisp is an excellent language for beginners. It is increasingly the language of choice in introductory programming courses due to its friendly, interactive environment, rich data structures, and powerful software tools that even a novice can master in short order.
''','1990'),
('Mathematica Programming','Mathematica','Leonid Shifrin','pdf','http://www.mathprogramming-intro.org/download/MathProgrammingIntro.pdf',
'''
When writing this book  I mostly had in mind people who want to understand Mathematica  programming, and particularly those Mathematica users who would like to make a transition from a user to a programmer, or perhaps those who already have some  limited Mathematica programming experience but want to improve their command of the system. Expert Mathematica programmers will probably find little new information in the book  - may be, the last chapter could be of some interest to them.

The first part of the audience for this book  are  scientists who would like to  understand Mathematica  programming better, to take advantage of the possibilities it offers. The second part are (software) engineers who may consider Mathematica  as a tool for a prototype design. In this context, Mathematica  can serve as a tool of "experimental programming", especially useful in projects where some non-trivial computations/research have to accompany programming. 
''','2008'),
('Humble Little Ruby Book','Ruby','Jeremy McAnally','pdf','http://www.humblelittlerubybook.com/book/hlrb.pdf',
'''
An up to date book on Ruby programming, written in a style described as "a beautiful display of pragmatically chunky bacon, wrapped in a nutshell." Or something like that.

Mr. Neighborly's Humble Little Ruby Book covers the Ruby language from the very basics of using puts to put naughty phrases on the screen all the way to serving up your favorite web page from WEBrick or connecting to your favorite web service. Written in a conversational narrative rather than like a dry reference book, Mr. Neighborly's Humble Little Ruby Book is an easy to read, easy to follow guide to all things Ruby.
''',
'2006'),
('The Poignant Guide to Ruby','Ruby','Why the Lucky Stiff','pdf','https://github.com/downloads/mislav/poignant-guide/whys-poignant-guide-to-ruby.pdf',
'''
Why's (poignant) Guide to Ruby is an introductory book to the Ruby programming language, written by why the lucky stiff.

The book includes some wacky humour and goes off-topic on occasions. Further, the book includes jokes that are known within the Ruby community as well as cartoon characters.

The contents of the book:

• Kon'nichi wa, Ruby
• A Quick (and Hopefully Painless) Ride Through Ruby (with Cartoon Foxes): basic introduction to central Ruby concepts
• Floating Little Leaves of Code: evaluation and values, hashes and lists
• Them What Make the Rules and Them What Live the Dream: case/when, while/until, variable scope, blocks, methods, class definitions, class attributes, objects, modules, introspection in IRB, dup, self, rbconfig module
• Downtown: metaprogramming, regular expressions
• When You Wish Upon a Beard: send method, new methods in existing classes
• Heaven's Harp
''','2009'),
('Ruby Programming','Ruby','Wikibooks','pdf','https://upload.wikimedia.org/wikipedia/commons/e/ee/Ruby_Programming.pdf',
'''
Ruby is an interpreted, object-oriented programming language. Its creator, Yukihiro Matsumoto, a.k.a “Matz,” released it to the public in 1995. Its history is covered here. Its many features are listed here.
The book is currently broken down into several sections and is intended to be read sequentially. Getting started will show how to install and get started with Ruby in your environment. Basic Ruby demonstrates the main features of the language syntax. The Ruby language section is organized like a reference to the language. Available modules covers some of the standard library. Intermediate Ruby covers a selection of slightly more advanced topics. Each section is designed to be self contained.
''','2012'),
('The Haskell School of Music', 'Haskell','Paul Hudak','pdf','http://haskell.cs.yale.edu/wp-content/uploads/2013/04/HSoM1.pdf',
'''
This textbook (in progress) describes Euterpea, a computer music library developed in Haskell, that allows programming computer music applications both at the note level and the signal level.  The book also teaches functional programming in Haskell from scratch.  It is suitable for use in the classroom to teach functional programming, computer music principles, or both.
''','2013'),
('Yet Another Haskell Tutorial','Haskell','Hal Daume III','pdf','http://hal3.name/docs/daume02yaht.pdf',
'''
Yet Another Haskell Tutorial provides a complete introduction to the Haskell programming language. It assumes no knowledge of the Haskell language or familiarity with functional programming in general.

• Getting Started
• Language Basics - presents the basic concepts of Haskell and the basic syntax of Haskell
• Type Basics - uses a system of static type checking. This means that every expression in Haskell is assigned a type
• Basic Input/Output
• Modules - program subcomponents are divided into modules
• Advanced Features - examines sections and infix operators, local declarations, partial application, pattern matching, guards, instance declarations, datatypes revisited, more lists, arrays, maps, layout, and the final word on lists
• Advanced Types - type synonyms, newtypes, datatypes, classes, instances, kinds, class hierarchies, and default
• Monads - program subcomponents are divided into modules
• Advanced Techniques
''','2006'),
('The Undergraduate Guide to R','R','Trevor Martin','pdf','https://sites.google.com/site/undergraduateguidetor/manual-files/undergradguidetoR.pdf',
'''
Learning R will give you a whole new set of tools with which to manipulate, analyze, compare, and view data. R is designed primarily for use in statistics, but it is useful regardless of which scientific discipline you are pursuing. 

As the data sets used in all scientific disciplines get ever larger it is becoming increasingly more critical for scientists to be knowledgeable about how to use high-level programming languages such as R, which allow for easy and intuitive use. I have titled this manual ―The Undergraduate Guide to R‖ because I want to emphasize that R is a skill that should be learned early in the modern student‘s career. Of course, however, I hope that this manual is useful to everyone who is just starting to use R, undergraduate or not. 

This manual is designed so that no prior knowledge of programming is required or assumed (although rudimentary knowledge of general computer skills and statistics is a must). Thus, it may seem overly simple to many and I would highly recommend that those of you who find yourselves in this situation look at Section 12: Further Resources for more advanced manuals. 
''','2009'),
('Using R for Introductory Statistics','R','John Verzani','pdf','http://cran.r-project.org/doc/contrib/Verzani-SimpleR.pdf',
'''
The cost of statistical computing software has precluded many universities from installing these valuable computational and analytical tools. R, a powerful open-source software package, was created in response to this issue. It has enjoyed explosive growth since its introduction, owing to its coherence, flexibility, and free availability. While it is a valuable tool for students who are first learning statistics, proper introductory materials are needed for its adoption.

Using R for Introductory Statistics fills this gap in the literature, making the software accessible to the introductory student. The author presents a self-contained treatment of statistical topics and the intricacies of the R software. The pacing is such that students are able to master data manipulation and exploration before diving into more advanced statistical concepts. The book treats exploratory data analysis with more attention than is typical, includes a chapter on simulation, and provides a unified approach to linear models.

This text lays the foundation for further study and development in statistics using R. Appendices cover installation, graphical user interfaces, and teaching with R, as well as information on writing functions and producing graphics
''','2002'),
('Introduction to Statistical Thinking With R','R','Benjamin Yakir','pdf','http://pluto.huji.ac.il/~msby/StatThink/IntroStat.pdf',
'''
Introduction to Statistical Thinking is targeted at college students who are required to learn statistics, students with little background in mathematics and often no motivation to learn more. This book uses the basic structure of generic introduction to statistics course.

• Short introduction to statistics and probability
• Data structures and variation
• Provides numerical and graphical tools for presenting and summarizing the distribution of data
• Fundamentals of probability: Concept of a random variable, Examples of special types of random variables, Normal random variable, Sampling distribution and presents the Central Limit Theorem and the Law of Large Numbers
• Discussion of statistical inference. It provides an overview of the topics that are presented in the subsequent chapter.
• Basic tools of statistical inference, namely point estimation, estimation with a confidence interval, and the testing of statistical hypothesis
• Discusses inference that involve the comparison of two measurements
• Analysis of two case studies
''','2011'),
('PHP 5 Power Programming','PHP','Andi Gutsman (more)','pdf','http://ptgmedia.pearsoncmg.com/images/013147149X/downloads/013147149X_book.pdf',
'''
In PHP 5 Power Programming, PHP 5's co-creator and two leading PHP developers show you how to make the most of PHP 5's industrial-strength enhancements in any project, no matter how large or complex.

Their unique insights and realistic examples illuminate PHP 5's new object model, powerful design patterns, improved XML Web services support, and much more. Whether you are creating web applications, extensions, packages, or shell scripts, or migrating PHP 4 code, here are high-powered solutions you will not find anywhere else.

Review PHP's syntax and master its object-oriented capabilities, from properties and methods to polymorphism, interfaces, and reflection.
''','2004'),
('PHP Reference: Beginner to Intermediate PHP5','PHP','Mario Lurig','pdf','http://cdn.phpreferencebook.com/wp-content/uploads/2008/12/php_reference_-_beginner_to_intermediate_php5.pdf',
'''
PHP Reference Book: Beginner to Intermediate PHP5 is a collection of over 250 PHP functions with clear explanations in language anyone can understand, followed with as many examples as it takes to understand what the function does and how it works. One of the best PHP books to keep around as a PHP reference.

This PHP reference includes numerous additional tips, the basics of PHP, MySQL query examples, regular expressions syntax, and two indexes to help you find information faster: a common language index and a function index.
''','2008'),
('Python Module of The Week','Python','Doug Hellmann','pdf','http://pymotw.com/2/PyMOTW-1.132.pdf',
'''
Python Module of the Week (PyMOTW) is a series of blog posts written by Doug Hellmann. It was started as a way to build the habit of writing something on a regular basis. The focus of the series is building a set of example code for the modules in the Python standard library.

PyMOTW is a good source of documentation for Python modules.
''','2013'),
('Aspects of AJAX','Ajax','Matthias Hertel','pdf','http://www.mathertel.de/AJAX/AspectsOfAJAX0704.pdf',
'''
Asynchronous JavaScript and XML (Ajax) is a group of interrelated web development techniques used on the client-side to create asynchronous web applications. Ajax is a group of technologies.
Aspects of AJAX is about an Ajax Framework and an Ajax Engine for JavaScript, XML, SOAP, WSDL und ASP.NET using standard Web Services on the server.

• Asynchronous programming
• Native AJAX programming
• Client-Server Protocols
• The AJAX Engine
• JavaScript Behaviors
• Building JavaScript enabled web controls
• Connecting Controls
• AJAX enabled web controls
• Visual Effects Library
• Some HTML and http basics
• Listings
• JavaScript Proxy Reference
• DataConnections Reference
''','2007'),
('The C Book','C','Mike Banahan (more)','pdf','http://publications.gbdirect.co.uk/c_book/thecbook.pdf',
'''
This book was written with two groups of readers in mind. Whether you are new to C and want to learn it, or already know the older version of the language but want to find out more about the new standard, we hope that you will find what follows both instructive and at times entertaining too.
This is not a tutorial introduction to programming. The book is designed for programmers who already have some experience of using a modern high-level procedural programming language. As we explain later, C isn't really appropriate for complete beginners—though many have managed to use it—so the book will assume that its readers have already done battle with the notions of statements, variables, conditional execution, arrays, procedures (or subroutines) and so on. Instead of wasting your time by ploughing through tedious descriptions of how to add two numbers together and explaining that the symbol for multiplication is *, the book concentrates on the things that are special to C. In particular, it's the way that C is used which is emphasized.
''','1991'),
('Higher Order Perl','Perl','Unknown','pdf','http://hop.perl.plover.com/book/pdf/HigherOrderPerl.pdf',
'''
Higher-Order Perl: Transforming Programs with Programs is a book with the goal to teach Perl programmers with a strong C and Unix background how to use techniques with roots in functional programming languages like Lisp that are available in Perl as well, but less known. It is about functional programming techniques in Perl. It is about how to write functions that can modify and manufacture other functions.

• Recursion and callbacks
• Dispatch tables
• Caching and memoization
• Iterators
• From recursion to iterators
• Infinite streams
• Higher-order functions and currying
• Parsing
• Declarative programming
''','2005'),
('Impatient Perl','Perl','Greg London','pdf','http://blob.perl.org/books/impatient-perl/iperl.pdf',
'''
You write code for a living, and your inherit a legacy program written in Perl. You can program in your native language in your sleep. But you don't know Perl at all, or you've only dabbled with it. Your deadline doesn't give you enough time to rewrite the legacy program in your native language, but it needs new features. You need to learn Perl, and you need to learn it NOW. "Impatient Perl" was written for you.

The Impatient Introduction to Perl
This document is for people who either want to learn Perl or are already programming in Perl and just don't have the patience to scrounge for information to learn and use Perl. This document should also find use as a handy desk reference for some of the more common perl related questions.

The history of Perl in 100 words or less
In the mid 1980's, Larry Wall was working as a sysadmin and found that he needed to do a number of common, yet oddball functions over and over again. And he didn't like any of the scripting languages that were around at the time, so he invented Perl. Version 1 was released circa 1987. A few changes have occurred between then and now. The current version of Perl has exceeded 5.8.0 and is a highly recommended upgrade.
''','2010'),
('Multivariate Statistics with R','R','Paul J. Hewson','pdf','http://knowledgeforge.net/opentextbook/svn/multivariatestatistics/notes.pdf',
'''
Many of the statistical analyses encountered to date consist of a single response variable and one or more explanatory variables. In this latter case, multiple regression, we regressed a single response (dependent) variable on a number of explanatory (independent) variables. This is occasionally referred to as \multivariate regression" which is all rather unfortunate. There isn't an entirely clear "canon" of what is a multivariate technique and what isn't (one could argue that discriminant analysis involves a single dependent variable). However, we are going to consider the simultaneous analysis of a number of related variables. We may approach this in one of two ways. The rst group of problems relates to classification, where attention is focussed on individuals who are more alike.

The other group of problems concerns inter-relationships between variables. Again, we may be interested in lower dimension that help us visualise a given dataset. Alternatively, we may be interested to see how one group of variables is correlated with another group of variables. Finally, we may be interested in models for the interrelationships between variables.
''','2009'),
('Haskell No Panic','Haskell','Conrad Barski','pdf','http://lisperati.com/haskell/hasktut.pdf',
'''
There's other tutorials out there, but you'll like this one the best for sure: You can just cut and paste the code from this tutorial bit by bit, and in the process, your new program will create magically create more and more cool graphics along the way... The final program will have less than 100 lines of Haskell[1] and will organize a mass picnic in an arbitrarily-shaped public park map and will print pretty pictures showing where everyone should sit! (Here's what the final product will look like, if you're curious...)
''',''),
('Hacking Secret Ciphers with Python','Python','Al Sweigart','pdf','http://inventwithpython.com/hackingciphers.pdf',
'''
'Hacking Secret Ciphers with Python' teaches complete beginners how to program in the Python programming language. The reader not only learns about several classical ciphers, but also how to write programs that encrypt and hack these ciphers. The full source code is given and explained line-by-line for ciphers such as the Caesar cipher, transposition cipher, simple substitution cipher, multiplicative & affine ciphers, Vigenere cipher, and hacking programs for each of these ciphers. The final chapters cover public key cryptography and the modern RSA cipher.
''','2013'),
('Python for Informatics: Exploring Information','Python','Charles Severance','pdf','http://www.pythonlearn.com/book_006.pdf',
'''
The goal of this book is to provide an Informatics-oriented introduction to programming. The primary difference between a computer science approach and the Informatics approach taken in this book is a greater focus on using Python to solve data analysis problems common in the world of Informatics.
''','2010'),
('Computer Science From the Bottom Up','Computer Science','Ian Wienand','pdf','http://www.bottomupcs.com/csbu.pdf',
'''
In a nutshell, what you are reading is intended to be a shop class for computer science. Young computer science students are taught to "drive" the computer; but where do you go to learn what is under the hood? Trying to understand the operating system is unfortunately not as easy as just opening the bonnet. The current Linux kernel runs into the millions of lines of code, add to that the other critical parts of a modern operating system (the compiler, assembler and system libraries) and your code base becomes unimaginable. 

Not everyone wants to attend shop class. Most people only want to drive the car, not know how to build one from scratch. Obviously any general computing curriculum has to take this into account else it won’t be relevant to its students. So computer science is taught from the "top down"; applications, high level programming, software design and development theory, possibly data structures. Students will probably be exposed to binary, hopefully binary logic, possibly even some low level concepts such as registers, opcodes and the like at a superﬁcial level.

This book aims to move in completely the opposite direction, working from operating systems fundamentals through to how those applications are complied and executed.
''','2013'),
('Speeding Through Haskell','Haskell','Mihai Radu Popescu','pdf','http://www.sthaskell.com/haskell-book.pdf?attredirects=0',
'''
Welcome to Speeding Through Haskell, home of the newest Haskell programming book. It's so new, it's not even finished yet!

Haskell is an awesome programming language. It's a lot more mathematically rigorous than others, which means that programs can be proven to be correct and in most cases, if they compile, they will run just fine too. This involves new challenges, however. For instance, you can't change even a single "variable". Everything is done via recursion and other tricks. Don't worry, it'll seem very natural once you try it out.

You can take a look, but keep in mind that it's a work in progress. Some things may be inaccurate; many will be incomplete. Things marked [fixme] are broken; [xref] tags indicate missing cross-references. I'm aiming for about 15-20 chapters for the finished book --- it's going to take a while.
''',''),
('Economics in One Lesson','Economics','Henry Hazlitt','pdf','https://mises.org/books/economics_in_one_lesson_hazlitt.pdf',
'''
This primer on economic principles brilliantly analyzes the seen and unseen consequences of political and economic actions. In the words of F.A. Hayek, there is "no other modern book from which the intelligent layman can learn so much about the basic truths of economics in so short a time.
''','1946'),
('The Cathedral and the Bazaar','Development','Eric Raymond', 'pdf','http://www.unterstein.net/su/docs/CathBaz.pdf',
'''
Open source provides the competitive advantage in the Internet Age. According to the August Forrester Report, 56 percent of IT managers interviewed at Global 2,500 companies are already using some type of open source software in their infrastructure and another 6 percent will install it in the next two years. This revolutionary model for collaborative software development is being embraced and studied by many of the biggest players in the high-tech industry, from Sun Microsystems to IBM to Intel.

The Cathedral & the Bazaar is a must for anyone who cares about the future of the computer industry or the dynamics of the information economy. Already, billions of dollars have been made and lost based on the ideas in this book. Its conclusions will be studied, debated, and implemented for years to come. According to Bob Young, "This is Eric Raymond's great contribution to the success of the open source revolution, to the adoption of Linux-based operating systems, and to the success of open source users and the companies that supply them.
''','1999'),
('The Haskell Road to Logic, Math and Programming','Haskell','Kees Doets (more)','pdf','http://fldit-www.cs.uni-dortmund.de/~peter/PS07/HR.pdf',
'''
The textbook by Doets and van Eijck puts the Haskell programming language systematically to work for presenting a major piece of logic and mathematics. The reader is taken through chapters on basic logic, proof recipes, sets and lists, relations and functions, recursion and co-recursion, the number systems, polynomials and power series, ending with Cantor's infinities. The book uses Haskell for the executable and strongly typed manifestation of various mathematical notions at the level of declarative programming. The book adopts a systematic but relaxed mathematical style (definition, example, exercise, ...); the text is very pleasant to read due to a small amount of anecdotal information, and due to the fact that definitions are fluently integrated in the running text. An important goal of the book is to get the reader acquainted with reasoning about programs.
''','2004'),
('Winning the Zero Moment of Truth','Marketing','Jim Lecinski','pdf','http://www.zeromomentoftruth.com/assets/files/google-zmot.pdf',
'''
The way we shop is changing and marketing strategies are simply not keeping pace. Whether we're shopping for corn flakes, concert tickets or a honeymoon in Paris, the Internet has changed how we decide what to buy. Today we're all digital explorers, seeking out online ratings, social media-based peer reviews, videos, and in-depth product details as we move down the path to purchase. Marketing has evolved and modern marketing strategies have to evolve with the changing shape of shopping. At Google, we call this online decision-making moment the Zero Moment of Truth -- or simply ZMOT.

Winning the Zero Moment of Truth is a powerful new eBook by Jim Lecinski, Google's Managing Director of US Sales & Service and Chief ZMOT Evangelist. Jim shares how to get ahead at this critical new marketing moment, supported by exclusive market research, personal stories, and insights from C-level executives at global leaders like General Electric, Johnson & Johnson, and VivaKi.
''','2011'),
('The ZMOT HandBook','Marketing','Google','pdf','http://www.zeromomentoftruth.com/assets/files/ZMOT_Handbook.pdf',
'''
The Handbook from 2012 to read with the ZMOT book from 2011.
''','2012'),
('The Future of the Internet','Internet','Jonathan L. Zittrain','pdf','http://futureoftheinternet.org/files/2013/06/ZittrainTheFutureoftheInternet.pdf',
'''
IPods, iPhones, Xboxes, and TiVos represent the first wave of Internet-centered products that can’t be easily modified by anyone except their vendors or selected partners. These “tethered appliances” have already been used in remarkable but little-known ways: car GPS systems have been reconfigured at the demand of law enforcement to eavesdrop on the occupants at all times, and digital video recorders have been ordered to self-destruct thanks to a lawsuit against the manufacturer thousands of miles away. New Web 2.0 platforms like Google mash-ups and Facebook are rightly touted—but their applications can be similarly monitored and eliminated from a central source. As tethered appliances and applications eclipse the PC, the very nature of the Internet—its “generativity,” or innovative character—is at risk.
''','2008'),
('Hacking the Xbox','Xbox Hacking','''Andrew "bunnie" Huang''','pdf','http://bunniefoo.com/nostarch/HackingTheXbox_Free.pdf',
'''
Hacking the Xbox begins with a few step-by-step tutorials on hardware modifications that teach basic hacking techniques as well as essential reverse-engineering skills. It progresses into a discussion of the Xbox security mechanisms and other advanced hacking topics, emphasizing the important subjects of computer security and reverse engineering. The book includes numerous practical guides, such as where to get hacking gear, soldering techniques, debugging tips, and an Xbox hardware reference guide.

Hacking the Xbox confronts the social and political issues facing today's hacker, and introduces readers to the humans behind the hacks through several interviews with master hackers. It looks at the potential impact of today's legal challenges to legitimate reverse-engineering activites, whcih are further examined in a chapter contributed by Lee Tien of the Electronic Frontier Foundation (EFF) about the rights and responsibilities of hackers. The book concludes with a discussion of the latest trends and vulnerabilities in secure PC platforms.
''','2013'),
('Essentials of Metaheuristics','Metaheuristics','Sean Luke','pdf','http://cs.gmu.edu/~sean/book/metaheuristics/Essentials.pdf',
'''
This is an open set of lecture notes on metaheuristics algorithms, intended for undergraduate students, practitioners, programmers, and other non-experts. It was developed as a series of lecture notes for an undergraduate course I taught at GMU. The chapters are designed to be printable separately if necessary. As it's lecture notes, the topics are short and light on examples and theory. It's best when complementing other texts. With time, I might remedy this.

What is a Metaheuristic? A common but unfortunate name for any stochastic optimization algorithm intended to be the last resort before giving up and using random or brute-force search. Such algorithms are used for problems where you don't know how to find a good solution, but if shown a candidate solution, you can give it a grade. The algorithmic family includes genetic algorithms, hill-climbing, simulated annealing, ant colony optimization, particle swarm optimization, and so on.
''','2013'),
('Mathematics for Computer Science','Computer Science','Eric Lehman (more)','pdf','http://courses.csail.mit.edu/6.042/fall13/mcs.pdf',
'''
This text explains how to use mathematical models and methods to analyze problems that arise in computer science. Proofs play a central role in this work because the authors share a belief with most mathematicians that proofs are essential for genuine understanding. Proofs also play a growing role in computer science; they are used to certify that software and hardware will always behave correctly, something that no amount of testing can do. Simply put, a proof is a method of establishing truth. Like beauty, “truth” sometimes depends on the eye of the beholder, and it should not be surprising that what constitutes a proof differs among ﬁelds. For example, in the judicial system, legal truth is decided by a jury based on the allowable evidence presented at trial. 
In the business world, authoritative truth is speciﬁed by a trusted person or organization, or maybe just your boss. In ﬁelds such as physics or biology, scientiﬁc truth1 is conﬁrmed by experiment. In statistics, probable truth is established by statistical analysis of sample data. Philosophical proof involves careful exposition and persuasion typically based on a series of small, plausible arguments. 
''','2013'),
('The Wealth of Networks','Networks','Yochai Benkler','pdf','http://www.benkler.org/Benkler_Wealth_Of_Networks.pdf',
'''
Production is shifting from physical products like blue jeans, to decentralized information goods, like articles on the Internet. This gives users more power (they can publish instead of just reading), creates more opportunities for democratic participation, lowers costs for developing countries, and democratizes the creation of our culture.

This book will analyze these changes by looking at what new technologies make easy, applying an individualist economic model, and examining the effects on human beings. As the state's role has largely been to support big companies, this book will largely ignore it, even though it could be used as a force for good.
''','2006'),
('Open Government','Politics','Daniel Lathrop (more)','pdf','https://github.com/oreillymedia/open_government/raw/master/open_government.pdf',
'''
What is open government? In the most basic sense, it’s the notion that the people have the right to access the documents and proceedings of government. The idea that the public has a right to scrutinize and participate in government dates at least to the Enlightenment, and is enshrined in both the U.S. Declaration of Independence and U.S. Constitution. Its principles are recognized in virtually every democratic country on the planet. But the very meaning of the term continues to evolve. The concept of open government has been influenced—for the better—by the open source software movement, and taken on a greater focus for allowing participation in the procedures of government. Just as open source software allows users to change and contribute to the source code of their software, open government now means government where citizens not only have access to information, documents, and proceedings, but can also become participants in a meaningful way. 

Open government also means improved communication and operations within the various branches and levels of government. More sharing internally can lead to greater efficiency and accountability.

''','2010'),
('Vi iMproved (VIM)','VIM','Steve Oualline','pdf','http://www.truth.sk/vim/vimbook-OPL.pdf',
'''
This book is especially recommended for beginners and those who use Vim for a short while and would like to learn more. The most often used commands are explained with many figures and examples. Steve has a writing style that is very easy to read. Advanced Vim users will find many hints for useful features. The more advanced items are not explained in detail though.
At the end there is a quick reference for the most often used commands. The text was written for Vim version 5.7.
The book has been published in April 2001. It is about 600 pages. 
''','2001'),
('Computer Networking: Principles, Protocols and Practice','Networking','Olivier Bonaventure (more)','pdf','http://cnp3book.info.ucl.ac.be/static/_downloads/cnp3.pdf',
'''
This open textbook aims to fill the gap between the open-source implementations and the open-source network specifications by providing a detailed but pedagogical description of the key principles that guide the operation of the Internet. The book is released under a creative commons licence. Such an open-source license is motivated by two reasons. The first is that we hope that this will allow many students to use the book to learn computer networks. The second is that I hope that other teachers will reuse, adapt and improve it. Time will tell if it is possible to build a community of contributors to improve and develop the book further. As a starting point, the first release contains all the material for a one-semester first upper undergraduate or a graduate networking course.
''','2011'),
('Programming Forth','Forth','Stephen Pelc','pdf','http://www.mpeforth.com/arena/ProgramForth.pdf',
'''
Programming Forth introduces you to modern Forth systems. In 1994 the ANS Forth standard was released and unleashed a wave of creativity among Forth compiler writers. Because the ANS standard, unlike the previous informal Forth-83 standard, avoids specifying implementation details, implementers took full advantage. The result has been what I choose to call modern Forths, which are available from a range of sources both commercial and open-source.

This book concentrates on introducing people who already know some programming to ANS Forth systems. Apart from the introduction of ANS Forth itself, Programming Forth includes examples of varying sizes, exercises, some advanced topics, how to take best advantage of Forth and project management. 
''','2011'),
('And So Forth...','Forth','J.L. Bezemer','pdf','http://ficl.sourceforge.net/pdf/Forth_Primer.pdf',
'''
Don’t you hate it? You’ve just got a new programming language and you’re trying to write your ﬁrst program. You want to use a certain feature (you know it’s got to be there) and you can’t ﬁnd it in the manual. I’ve had that experience many times. So in this manual you will ﬁnd many short features on all kind of topics. How to input a number from the keyboard, what a cell is, etc. 

I hope this will enable you to get quickly on your way. If it didn’t, email me at ’hansoft@bigfoot.com’. You will not only get an answer, but you will help future Forth users as well. You can use this manual two ways. You can either just getwhat you need or work yourway through. Every section builds on the knowledge you obtained in the previous sections. All sections are grouped into levels. We advise you to use what you’ve learned after you’ve worked your way through a level. If this isn’t enough to teach you Forth you can always get a real good textbook on Forth, like "Starting Forth" by Leo Brodie. Have fun!
''','2001'),
('CIML: A Course in Machine Learning','Machine Learning','Hal Daumé III','pdf','http://ciml.info/dl/v0_8/ciml-v0_8-all.pdf',
'''
Machine learning is the study of algorithms that learn from data and experience. It is applied in a vast variety of application areas, from medicine to advertising, from military to pedestrian. Any area in which you need to make sense of data is a potential consumer of machine learning.

CIML is a set of introductory materials that covers most major aspects of modern machine learning (supervised learning, unsupervised learning, large margin methods, probabilistic modeling, learning theory, etc.). It's focus is on broad applications with a rigorous backbone. A subset can be used for an undergraduate course; a graduate course could probably cover the entire material and then some.
''','2012'),
#('Game Programming Patterns','Game Programming','Bob Nystrom','html',['all_links','http://gameprogrammingpatterns.com/'],
#'''
#There are already dozens of game programming books out there. Why write another? I’ll explain by analogy.
#
#Imagine a game codebase as a house. Graphics and sound are the appliances and fixtures: a nice chandelier, kitchen sink, big picture windows. This is the kind of stuff you can find in other books. These things matter, of course, but this book aims at something a bit more humble and fundamental: the framing. Other books can teach you about windows and fixtures, faucets and tubs. What I hope to cover in this book is the joist and the arch, plumbing and wiring — techniques that will let you build an elegant and maintainable structure out of a few simple parts. Use them to frame the house, then crack open those other books to build it out.
#
#It’s easy to underappreciate this. After all, friends won’t look at your home and say, “Wow, nice wiring!” But without it, I can guarantee they will notice when you flip the lightswitch and your beautiful chandelier doesn’t turn on.
#'''),
('Foundations of Databases','Databases','Serge Abiteboul (more)','pdf','http://webdam.inria.fr/Alice/pdfs/all.pdf',
'''
Computers are now used in almost all aspects of human activity. One of their main uses is to manage information, which in some cases involves simply holding data for future retrieval and in other cases serving as the backbone for managing the life cycle of complex ﬁnancial or engineering processes. A large amount of data stored in a computer is called a database. The basic software that supports the management of this data is called a database management system (dbms). The dbms is typically accompanied by a large and evergrowing body of application software that accesses and modiﬁes the stored information. The primary focus in this book is to present part of the theory underlying the design and use of these systems.
''','1995'),
('The Probabiliy and Statistics Cookbook','Statistics','Matthias Vallentin','pdf','http://matthias.vallentin.net/probability-and-statistics-cookbook/cookbook-en.pdf',
'''
This cookbook integrates a variety of topics in probability theory and statistics. It is based on literature and in-class material from courses of the statistics department at the University of California in Berkeley but also influenced by other sources.
''','2012'),
('Culture & Empire: Digital Revolution','Digital Culture','Pieter Hintjens','pdf','https://github.com/cultureandempire/cultureandempire.github.io/raw/master/pdf/cande-2013-11-01.pdf',
'''
The whole planet is getting connected, and building vast new communities. The on-line world thinks faster, and thinks different. Smart, fast, and creative, these new communities are a real challenge to old power and old money. And old money, after its War on Drugs, and War on Terror, is now launching its War on the Internet. What is going on, and where will this lead us? Pieter Hintjens, campaigner, writer, and programmer, tells all in this vast, absorbing story of the Digital Revolution.
''','2013'),
('R Practicals Book','R','Charles DiMaggio','pdf','http://www.columbia.edu/~cjd11/charles_dimaggio/DIRE/resources/R/practicalsBookNoAns.pdf',
'''
The best way to start getting comfortable with a new language is to use it. This series of exercises reviews some of the content we’ve discussed during lecture, and introduces some other basic concepts about working with data in R. It’s important that you actively type in the commands and review the results rather than just read. Try to brieﬂy answer the questions that come up along the way. Don’t worry if everything doesn’t make a lot of sense during the earlier exercises. It will. And there’s an answer key available if you become too frustrated. '''
,'2013'),
('Introduction to Reverse Engineering','Reverse Engineering','Dennis Yurichev','pdf','http://yurichev.com/writings/RE_for_beginners-en.pdf',
'''
Q: Should one learn to understand assembly language these days?
A: Yes: in order to have deeper understanding of the internals and to debug your software better and faster.
Q: Should one learn to write in assembly language these days?
A: Unless one writes low-level OS6 code, probably no.
Q: But what about writing highly optimized routines?
A: No, modern C/C++ compilers do this job better.
Q: Should I learn microprocessor internals?
A: Modern CPU7-s are very complex. If you do not plan to write highly optimized code or if you do not work on compiler’s code generator then you may still learn internals in bare outlines. 8. At the same time, in order to understand and analyze compiled code it is enough to know only ISA9, register’s descriptions, i.e., the “outside” part of a CPU that is available to an application programmer.
''','2014'),
('OpenIntro Statistics','Statistics','David M. Diez (more)','pdf','https://dl.dropboxusercontent.com/s/tokfd9t86rbbstp/os2.pdf?dl=1&token_hash=AAGbVmzSU7kH6VyPtF9sdMO52pXTjVTBAO-UOuJoYexMgw',
'''
Scientists seek to answer questions using rigorous methods and careful observations. These observations – collected from the likes of field notes, surveys, and experiments – form the backbone of a statistical investigation and are called data. Statistics is the study of how best to collect, analyze, and draw conclusions from data. It is helpful to put statistics in the context of a general process of investigation: 
1. Identify a question or problem.
2. Collect relevant data on the topic.
3. Analyze the data.
4. Form a conclusion.
Statistics as a subject focuses on making stages 2-4 objective, rigorous, and efficient. That is, statistics has three primary components: How best can we collect data? How should it be analyzed? And what can we infer from the analysis?
''','2012'),
('Git Reference','Git','GitHub Team','html','http://gitref.org/index.html',
'''
The Git Reference site was put together by the GitHub team.
''',"2014"),
('Unix-Linux tools Reference','Linux Tools','Bruce Barnett','html','http://www.grymoire.com/Unix/index.html',
'''
This page includes Bruce Barnett's tutorials on UNIX shell programming and various other arcane subjects of interest to wizards.
These tutorials were originally Solaris-specific, and originally contained a lot of references to OpenWindows. Times have changed, but I hope the basic information will still be helpful. I do try to update the information. Corrections are helpful. Please be patient.
''','2013'),
('Advanced Bash Scripting Guide','Bash','Mendel Cooper','html','http://tldp.org/LDP/abs/html/index.html',
'''
This tutorial assumes no previous knowledge of scripting or programming, but progresses rapidly toward an intermediate/advanced level of instruction . . . all the while sneaking in little nuggets of UNIX® wisdom and lore. It serves as a textbook, a manual for self-study, and as a reference and source of knowledge on shell scripting techniques. The exercises and heavily-commented examples invite active reader participation, under the premise that the only way to really learn scripting is to write scripts.

This book is suitable for classroom use as a general introduction to programming concepts.
''','2012'),
('The Command Line Crash Course','Command Line','Zed A Shaw','html','http://learncodethehardway.org/cli/book/index.html',
'''
This book is a quick super fast course in using the command line. It is intended to be done rapidly in about a day or two, and not meant to teach you advanced shell usage.
''','2010'),
('Programming in Lua','Lua','Roberto Ierusalimschy','html','http://www.lua.org/pil/',
'''
This book is a detailed and authoritative introduction to all aspects of Lua programming written by Lua's chief architect.

Programming in Lua gives a solid base for any programmer who wants to use Lua. It covers all aspects of Lua—from the basics to its API with C—explaining how to make good use of its features and giving numerous code examples. The book is targeted at people with some programming background, but it does not assume any prior knowledge about Lua or other scripting languages. 
''','2013'),
('Learn Python the Hard Way','Python','Zed A Shaw','html','http://learnpythonthehardway.org/book/',
'''
This simple book is meant to get you started in programming. The title says it's the hard way to learn to write code but it's actually not. It's only the "hard" way because it uses a technique called instruction. Instruction is where I tell you to do a sequence of controlled exercises designed to build a skill through repetition. This technique works very well with beginners who know nothing and need to acquire basic skills before they can understand more complex topics. It's used in everything from martial arts to music to even basic math and reading skills.

This book instructs you in Python by slowly building and establishing skills through techniques like practice and memorization, then applying them to increasingly difficult problems. By the end of the book you will have the tools needed to begin learning more complex programming topics. I like to tell people that my book gives you your "programming black belt." What this means is that you know the basics well enough to now start learning programming.

If you work hard, take your time, and build these skills, you will learn to code.
''','2010'),
('Djen of Django','Django','Agiliq','html','http://agiliq.com/books/djenofdjango/',
'''
This book shows through several examples how to build applications with Django.
''','2010')#,
#('Ruby on Rails Tutorial','Ruby on Rails','Michael Hartl','html','http://ruby.railstutorial.org/ruby-on-rails-tutorial-book',
#'''
#"Welcome to the Ruby on Rails Tutorial. The goal of this book is to be the best answer to the question, “If I want to learn web development with Ruby on Rails, where should I start?” By the time you finish the Ruby on Rails Tutorial, you will have all the skills you need to develop and deploy your own custom web applications with Rails. You will also be ready to benefit from the many more advanced books, blogs, and screencasts that are part of the thriving Rails educational ecosystem. Finally, since the Ruby on Rails Tutorial uses Rails 4, the knowledge you gain here represents the state of the art in web development.
#''','2013')

]
