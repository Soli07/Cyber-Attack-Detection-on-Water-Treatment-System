html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Water Treatment</title>
    </head>
    <body>
    <?php include 'data.php'; ?>
    
    
        <img src="water treatment images/water tank.jpeg" alt="Water Tank" style="position: absolute; top: 130px; left: 145px; width: 100px; height: 100px;">
        <p style="position: absolute; top: 220px; left:150px; color: darkblue;"> Raw Water Tank</p>

        <img src="water treatment images/raw water pump.jpeg" alt="Pump 1" style="position: absolute; top: 50px; left: 300px; width: 100px; height: 100px;">
        <div id="p101" style="position: absolute; top:60px; left:300px; color: darkblue; font-size:10px"></div>

        <img src="water treatment images/raw water pump.jpeg" alt="Pump 2" style="position: absolute; top: 200px; left: 300px; width: 100px; height: 100px;">
        <div id="p102" style="position: absolute; top:205px; left:380px; color: darkblue; font-size:10px"></div>
        <p style="position: absolute; top: 280px; left: 300px; color: darkblue;">Raw Water Pumps</p>


        <img src="water treatment images/chemical tank.jpeg" alt="chemicals tank 1" style="position: absolute; top: 240px; left: 500px; width: 100px; height: 100px;">
        <p style="position: absolute; top: 330px; left: 520px; color: darkblue;">NaCl Tank</p>

        <img src="water treatment images/chemical tank.jpeg" alt="chemicals tank 2" style="position: absolute; top: 240px; left: 605px; width: 100px; height: 100px;">
        <p style="position: absolute; top: 330px; left: 630px; color: darkblue;">HCL Tank</p>

        <img src="water treatment images/chemical tank.jpeg" alt="chemicals tank 3" style="position: absolute; top: 240px; left: 710px; width: 100px; height: 100px;">
        <p style="position: absolute; top: 330px; left: 740px; color: darkblue;">NaOCl Tank</p>

         <img src="water treatment images/chem dosing valve.jpeg" alt="valve with actuator" style="position: absolute; top: 40px; left:30px; width: 100px; height: 100px;">
         <p style="position: absolute; top:55px; left:6px; color: darkblue;">Feed<br> Water</p>
         <p style="position: absolute; top:110px; left:50px; color: darkblue;font-size: 12px">Raw water<br>Inlet valve</p>
        <div id="mv101" style="position: absolute; top:95px; left:60px; color: darkblue; font-size:10px"></div>
        
        
        <img src="water treatment images/uf level meter 1012.png" alt="sensor reading" style="position: absolute; top:48px; left:175px; width: 100px; height: 100px;">
        <p style="position: absolute; top:43px; left:200px; color: darkblue;font-size: 9px">Raw water<br>Level Meter</p>
        <div id="lit101" style="position: absolute; top:63px; left:205px; color: darkblue; font-size:10px"></div>

        <img src= "water treatment images/static mixer.jpeg" alt="static mixer 1" style="position: absolute; top:130px; left:810px; width: 100px; height: 100px;">
        <p style="position: absolute; top:180px; left:841px; color: darkblue;font-size:12px">Static Mixer</p>

        <img src="water treatment images/chem dosing valve.jpeg" alt="valve with actuator 2" style="position: absolute; top:120px; left:890px; width: 100px; height: 100px;">
        <div id="mv201" style="position: absolute; top:175px; left:925px; color: darkblue; font-size:10px"></div>

         <p style="position: absolute; top:185px; left:927px; color: darkblue;font-size:10px">Chem<br>Dosing <br>Valve</p>


         <img src= "water treatment images/water tank.jpeg" alt="UFFeed WaterTank" style="position: absolute; top:210px; left: 950px; width: 100px; height: 100px;">
         <p style="position: absolute; top:300px; left:973px; color: darkblue;font-size:15px">UF Feed<br>Water Tank</p>


          <img src="water treatment images/uf level meter 1012.png" alt="sensor reading 2" style="position: absolute; top:100px; left: 970px; width: 100px; height: 100px;">
          <p style="position: absolute; top:80px; left:1000px; color: darkblue;font-size:10px">UF Feed<br>Level Meter</p>
        <div id="lit301" style="position: absolute; top:105px; left:1005px; color: darkblue; font-size:10px"></div>
        <img src="water treatment images/raw water pump.jpeg" alt="Pump 3" style="position: absolute; top:166px; left:1100px; width: 100px; height: 100px;">
        <div id="p301" style="position: absolute; top:176px; left:1179px; color: darkblue;font-size:15px"></div>


         <img src="water treatment images/raw water pump.jpeg" alt="Pump 4" style="position: absolute; top:267px; left:1100px; width: 100px; height: 100px;">
         <div id="p302" style="position: absolute; top:277px; left:1179px; color: darkblue;font-size:15px"></div>
         <p style="position: absolute; top:340px; left:1110px; color: darkblue;">UF Feed Pumps</p>


        <img src="water treatment images/uf membrane.jpeg" alt="uf membrane" style="position: absolute; top:168px; left:1291px; width: 100px; height: 100px;">
         <p style="position: absolute; top:230px; left:1355px; color: darkblue;font-size:10px">UF<br> Membrane</p>


        <img src="water treatment images/chem dosing valve.jpeg" alt="Valve with actuator 3" style="position: absolute; top:95px; left:1340px; width: 100px; height: 100px;">
         <div id="mv302" style="position: absolute; top:150px; left:1373px; color: darkblue;font-size:10px"></div>
         <p style="position: absolute; top:160px; left:1373px; color: darkblue;font-size:10px">RO Feed<br>Valve</p>


        <img src="water treatment images/water tank.jpeg" alt="RO feed water tank" style="position: absolute; top:190px; left:1410px; width: 100px; height: 100px;">
        <p style="position: absolute; top:276px; left:1432px; color: darkblue;font-size:15px">RO Feed<br>WaterTank</p>


        <img src="water treatment images/raw water pump.jpeg" alt="pump 5" style="position: absolute; top:247px; left:1589px; width: 100px; height: 100px;">
         <div id="p401" style="position: absolute; top:257px; left:1671px; color:darkblue;font-size:15px"></div>



        <img src="water treatment images/raw water pump.jpeg" alt="pump 6" style="position: absolute; top:147px; left:1589px; width: 100px; height: 100px;">
         <div id="p402" style="position: absolute; top:157px; left:1671px; color: darkblue;font-size:15px"></div>


        <img src="water treatment images/rofeed level meter 1008.jpeg" alt="sensor reading 3" style="position: absolute; top:90px; left:1426px; width: 100px; height: 100px;">
         <p style="position: absolute; top:63px; left:1460px; color: darkblue;font-size:10px">ROFeed<br>LevelMeter</p>
         <div id="lit401" style="position: absolute; top:87px; left:1463px; color: darkblue;font-size:10px"></div>


        <img src="water treatment images/uv dechlor.jpeg" alt="uv dechlorinator" style="position: absolute; top:494px; left:1740px; width: 100px; height: 100px;">
        <p style="position: absolute; top:540px; left:1750px; color: darkblue;font-size:13px">UV_Dechlorinator</p>

        <img src="water treatment images/static mixer.jpeg" alt="static mixer 2" style="position: absolute; top:440px; left:1610px; width: 100px; height: 100px;">
         <p style="position: absolute; top:486px; left:1650px; color: darkblue;font-size:14px">Static Mixer</p>


        <img src="water treatment images/chemical tank.jpeg" alt="chemicals tank 4" style="position: absolute;top:607px;left:1680px; width: 100px; height: 100px;">
        <p style="position: absolute; top:695px; left:1695px; color: darkblue;font-size:14px">NAHSO3_Tank</p>


         <img src="water treatment images/filter.jpeg" alt="filter tank" style="position: absolute;top:515px;left:1562px; width: 100px; height: 100px;">
         <p style="position: absolute; top:583px; left:1597px; color: darkblue;font-size:14px">Filter</p>


         <img src="water treatment images/raw water pump.jpeg" alt="pump 7" style="position: absolute;top:465px;left:1353px; width: 100px; height: 100px;">
         <div id="p501" style="position: absolute; top:475px; left:1435px; color: darkblue;font-size:14px"></div>


         <img src="water treatment images/raw water pump.jpeg" alt="pump 8" style="position: absolute;top:563px; left:1353px; width: 100px; height: 100px;">
         <div id="p502" style="position: absolute; top:575px; left:1435px; color: darkblue;font-size:14px"></div>

         <img src="water treatment images/vessels.jpeg" alt="RO Vessels 1" style="position: absolute;top:550px; left:1149px; width: 100px; height: 100px;">


         <img src="water treatment images/vessels.jpeg" alt="RO Vessels 2" style="position: absolute;top:620px; left:1149px; width: 100px; height: 100px;">


         <img src="water treatment images/vessels.jpeg" alt="RO Vessels 3" style="position: absolute;top:690px; left:1149px; width: 100px; height: 100px;">

          <img src="water treatment images/chem dosing valve.jpeg" alt="Valve with actuator 4" style="position: absolute; top:605px; left:690px; width: 100px; height: 100px;">
          <p style="position: absolute; top:660px; left:725px; color: darkblue;font-size:10px">MV-501</p>
          <p style="position: absolute; top:670px; left:725px; color: darkblue;font-size:10px">RO Permeate<br>Valve</p>
        
          <img src="water treatment images/blue tank.jpeg" alt="RO Permeate Tank" style="position: absolute; top:625px; left:448px; width: 100px; height: 100px;">
           <p style="position: absolute; top:670px; left:540px; color: darkblue;font-size:15px">RO Permeate<br>Tank</p>
        
          <img src="water treatment images/blue tank.jpeg" alt="CIP Tank" style="position: absolute; top:490px; left:448px; width: 100px; height: 100px;">
          <p style="position: absolute; top:540px; left:540px; color: darkblue;font-size:15px">CIP Tank</p>
          
          
          <img src="water treatment images/raw water pump.jpeg" alt="CIP Pump" style="position: absolute;top:505px; left:313px; width: 100px; height: 100px;">
           <p style="position: absolute; top:515px; left:395px; color: darkblue;font-size:14px">P-603</p>
            <p style="position: absolute; top:575px; left:335px; color: darkblue;font-size:14px">CIP Pump</p>
           
          
          <img src="water treatment images/raw water pump.jpeg" alt="RO Permeate Pump" style="position: absolute;top:635px; left:313px; width: 100px; height: 100px;">
           <p style="position: absolute; top:645px; left:395px; color: darkblue;font-size:14px">P-601</p>
           <p style="position: absolute; top:705px; left:335px; color: darkblue;font-size:14px">RO Permeate<br>Pump</p>
        
         <img src="water treatment images/blue tank.jpeg" alt="UF Backwash Tank" style="position: absolute; top:800px; left:248px; width: 100px; height: 100px;">
         <p style="position: absolute; top:850px; left:340px; color:darkblue;font-size:15px">UF Backwash<br>Tank</p>
         
        
         <img src="water treatment images/raw water pump.jpeg"  alt="UF Backwash Pump" style="position: absolute; top:810px; left:138px; width: 100px; height: 100px;">
         <p style="position: absolute; top:818px; left:220px; color: darkblue;font-size:14px">P-601</p>
        <p style="position: absolute; top:792px; left:100px; color:darkblue;font-size:15px">UF Backwash<br>Pump</p>
         
         
         <img src="water treatment images/chem dosing valve.jpeg" alt="Valve with actuator 5" style="position: absolute; top:95px; left:1245px; width: 100px; height: 100px;">
         <p style="position: absolute; top:150px; left:1280px; color: darkblue;font-size:10px">MV-301</p>
         <p style="position: absolute; top:160px; left:1280px; color: darkblue;font-size:10px">UF Backwash<br>Valve</p>
         
         
          <img src="water treatment images/chem dosing valve.jpeg" alt="Valve with actuator 6" style="position: absolute;top:780px; left:900px; width: 100px; height: 100px;">
         <p style="position: absolute; top:835px; left:935px; color: darkblue;font-size:10px">MV-502</p>
         <p style="position: absolute; top:845px; left:935px; color: darkblue;font-size:10px">BackWash<br>Valve</p>
         
         
         <img src="water treatment images/WhatsApp Image 2024-03-02 at 8.08.45 PM.jpeg"alt="Valve with actuator 7" style="position: absolute;top:680px; left:820px; width: 100px; height: 100px;">
         <p style="position: absolute; top:705px; left:884px; color: darkblue;font-size:10px">MV-503</p>
         <p style="position: absolute; top:715px; left:884px; color: darkblue;font-size:10px">RO Permeate<br>Valve</p>


        <p style="position: absolute; top:65px; left:140px; color: darkblue;font-size:10px">FIT-101</p>
         <p style="position: absolute; top: 150px; left: 600px; color: darkblue;font-size:13px">FIT-201</p>
         <p style="position: absolute; top: 150px; left: 670px; color: darkblue;font-size:13px">ALT-201</p>
         <p style="position: absolute; top:130px; left:925px; color: darkblue;font-size:10px">ALT-202</p>
         <p style="position: absolute; top:155px; left:965px; color: darkblue;font-size:10px">ALT-203</p>
         <p style="position: absolute; top:215px; left:1740px; color:darkblue;font-size:15px">FIT_401</p>
          <p style="position: absolute; top:465px; left:1605px; color: darkblue;font-size:10px">ALT_402</p>
         <p style="position: absolute; top:540px; left:1515px; color: darkblue;font-size:12px">ALT_503</p>
         <p style="position: absolute; top:635px; left:650px; color: darkblue;font-size:12px">ALT_504</p>
