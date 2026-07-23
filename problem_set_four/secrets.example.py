#Example of how to hide an API key
YOUR_API_KEY = "sk-0123456789"
#Once you get an API key from https://pro.coincap.io/signup , you COULD just use it in the file as is.
#But it is industry standard to hide it in a .venv/.env (or for me a py file) so that no one else can make use of your tokens
#In my case I used a py file because I could not resolve an issue with importing dotenv. 
#Meaning I can't use it to load any environment variables