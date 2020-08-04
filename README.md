# emailer

# Hi all, Janek here. Just wanted to let you know how to work about this piece:

        1. Fill secrets.py with credentials to your mail's account (;
		
        2. Research (MPS) your mail provider's port, SMTP port. FYI We're going to also include ssl socket;
		
        3. Now's the time for Database feed! That's basically the first lines of code:
            - connecting pandas to database of your choosing (be that, e.g. excel file or cloud hostage);
            - initiating pandas method to iterate through your mail within correct port coordinates;
			
	4. Now we can create desired message along with it's subject. Also assign its both receving and delivering ends. 
		
	5. Last part's about scripting the message and to deliver to the appropriate customer:
		- attaching message to MIMEMultipart ( it makes sense for library, 
		check out more here: https://docs.python.org/3/library/email.mime.html );
		- text var is to ensure that we're going to pass it all as a String type;
		- creating context for SSL socket;
		- connecting to server via SMTP;
			
						***Finished with console log of receipent and process ending.***
			
			
								Thanks for stopping by! 
			If you're kind enough, feel free to leave a construct feedback - dully noted and appreciated. 
								Have a nice day!
