from os import system, environ
def load_env(filename='.env'):

  proceed = False
  
  try: 
    open(filename)

    proceed=True
  except: raise ValueError("Invalid filename")
  if proceed==True:
    data = open(filename).read()
    parsed_data = data.split('\n')
    
    for i in range(len(parsed_data)):

      current = parsed_data[i].split('=')

      system(current[0]+'='+current[1])
