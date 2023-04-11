
def getPreffix(symbol):
  if symbol =='99':
    return 'surface'
  elif symbol =='00':
    return '1000mb'
  elif symbol =='77':
    return 'tropopause'
  elif symbol =='92':
    return '925mb'
  elif symbol =='85':
    return '850mb'
  elif symbol =='70':
    return '700mb'
  elif symbol =='50':
    return '500mb'
  elif symbol =='40':
    return '400mb'
  elif symbol =='30':
    return '300mb'
  elif symbol =='25':
    return '250mb'
  elif symbol =='20':
    return '200mb'
  elif symbol =='15':
    return '150mb'
  elif symbol =='10':
    return '100mb'
  return 'unkn'

def decode(message):
  if message[0:4] == 'TTAA':
    decodeTTAA(message[5:])
  else:
    print("Unknown message type")

def decodeTTAA(message):
  data = message.split(' ')
  res = {}
  preffix = '--'
  for idx in range(len(data)):
    if idx == 0:
      res['dayOfMonth'] = int(data[idx][0:2])-50
      res['hour'] = data[idx][2:4]
      res['windUpTo'] = data[idx][4:]+'00mb'
    elif idx == 1:
      res['station'] = data[idx]
    else:
      if (idx-2) % 3 == 0:
        preffix = getPreffix(data[idx][0:2])
        res[preffix+'Pressure'] = ( '1' if int(data[idx][2:])<200 else '' )+data[idx][2:]+'mb'
      elif (idx-2) % 3 == 1:
        if data[idx].isnumeric():
          res[preffix+'Temperature'] = (-1 if int(data[idx][2:3])%2==1 else 1) * int(data[idx][0:3])/10
          res[preffix+'DewpointDepression'] = ( int(data[idx][3:])/10 if int(data[idx][3:]) < 50 else int(data[idx][3:]) - 50 )
          res[preffix+'Dewpoint'] = res[preffix+'Temperature'] - res[preffix+'DewpointDepression']
        else:
          res[preffix+'Temperature'] = '///'
          res[preffix+'DewpointDepression'] = '///'
          res[preffix+'Dewpoint'] = '///'
      elif (idx-2) % 3 == 2:
        if data[idx].isnumeric():
          res[preffix+'WindDirection'] = data[idx][0:2]+'0' if data[idx][3:3] == '1' else data[idx][0:3]
          res[preffix+'WindSpeed'] = (data[idx][3:] if data[idx][3:3] == '1' else data[idx][4:])+'kt'
        else:
          res[preffix+'WindDirection'] = '///'
          res[preffix+'WindSpeed'] = '///'
  print (res)


def __main__():
  decode("TTAA 73001 83746 99017 25838 15003 00156 25643 10003 92838 20421 16503 85567 17013 08508 70204 08630 32507 50592 07356 02010 40762 16725 30012 30972 32530 29014 25098 43138 29025 20244 56350 30529 15421 67160 29033 10659 71165 27521 88999 77999 31313 42308 82356=")

if __name__ == "__main__":
  __main__()