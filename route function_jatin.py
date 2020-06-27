def route_status(sensor):
  
  if ( sensor[2]==sensor[4]==sensor[6]==sensor[8]==1 and sensor[0]==sensor[1]==sensor[3]==sensor[5]==0):
    print ("t_point")   
   # return 
        
  if( sensor[0]==sensor[2]==sensor[4]==sensor[6]==sensor[8]==1 and sensor[1]==sensor[3]==sensor[5]==sensor[7]==0):
    print ("intersecton")
    #return 
      
  #left_turn
  if (sensor[0]==sensor[4]==sensor[7]==sensor[8]==1 and sensor[1]==sensor[2]==sensor[3]==sensor[6]==sensor[5]==0):
    print("left_turn_starting")
   # return
  if (sensor[4]==sensor[6]==sensor[8]==1 and sensor[0]==sensor[1]==sensor[2]==sensor[3]==sensor[5]==sensor[7]==0): #sensor[2]==0
    print("left_center")
    #return
                      
  #right turn
  if( sensor[0]==sensor[1]==sensor[4]==sensor[8]==1 and sensor[2]==sensor[3]==sensor[5]==sensor[6]==sensor[7]==0):
    print("right _starting")
    #return 
  if (sensor[2]==sensor[4]==sensor[8]==1 and sensor[6]==sensor[0]==sensor[1]==sensor[3]==sensor[5]==sensor[7]==0):# sensor[6]==0
    print("right_center")
    #return 
      
  # left_diversion
  if (sensor[0]==sensor[7]==sensor[8]==1 and sensor[1]==sensor[2]==sensor[3]==sensor[4]==sensor[5]==sensor[6]==0): # sensor[4]x
    print("left_diversion_starting")
    #return
  if ( sensor[0]==sensor[4]==sensor[6]==sensor[8]==1 and sensor[1]==sensor[2]==sensor[3]==sensor[5]==sensor[7]==0):
    print("left_diversion_center")
    #return
  if(sensor[0]==sensor[8]==sensor[5]==1 and sensor[1]==sensor[2]==sensor[3]==sensor[4]==sensor[6]==sensor[7]==0):
    print("left_diversion_ending")
    #return

  #right_diversion
  if (sensor[0]==sensor[1]==sensor[8]==1 and sensor[2]==sensor[3]==sensor[4]==sensor[5]==sensor[6]==sensor[7]==0): # sensor[4]x
    print("right_diversion_starting")
    #return
  if(sensor[0]==sensor[2]==sensor[4]==sensor[8]==1 and sensor[1]==sensor[3]==sensor[5]==sensor[6]==sensor[7]==0):
    print("right_diversion_center")
    #return
  if(sensor[0]==sensor[4]==sensor[5]==sensor[8]==1 and sensor[1]==sensor[2]==sensor[3]==sensor[6]==sensor[7]==0):
    print("right_diversion_ending")
    #return


  #only_backward
  if (sensor[0]==0 and sensor[8]==0 and sensor[1]==sensor[2]==sensor[3]==sensor[4]==sensor[5]==sensor[6]==sensor[7]==1):
    print("out_only_backwards")
    #return

  #only_forward
  if (sensor[0]==sensor[8]==sensor[4]==1 and sensor[1]==sensor[2]==sensor[3]==sensor[5]==sensor[6]==sensor[7]==0): # sensor[4]*
    print("out_only_forwards")
    #return

  #only_right
  if (sensor[0]==sensor[6]==sensor[3]==sensor[4]==sensor[5]==sensor[1]==sensor[7]==0 and sensor[2]==sensor[8]==1):# sensor[6]==0
    print("out_only_right")
    #return

  #only_left
  if (sensor[0]==sensor[2]==sensor[1]==sensor[3]==sensor[4]==sensor[5]==sensor[7]==0 and sensor[6]==sensor[8]==1):# sensor[2]==0
    print("out_only_left")
    #return

  #drifted_right
  if ( sensor[1]==sensor[3]==1 and sensor[0]==sensor[4]==sensor[8]==sensor[2]==sensor[5]==sensor[6]==sensor[7]==0):
    print("drifted_right")
    #return

  #drifted_left
  if ( sensor[5]==sensor[7]==1 and sensor[0]==sensor[4]==sensor[8]==sensor[2]==sensor[3]==sensor[1]==sensor[6]==0):
    print("drifted_left")
    #return

  '''
  #no_backward
  if (sensor[4]==sensor[8]==0 and sensor[1]==sensor[2]==sensor[3]==sensor[5]==sensor[6]==sensor[0]==sensor[7]==1):
    print("no_backward")
    #return
  '''




      
